#!/usr/bin/env python3

# Include needed libraries. Do _not_ include any libraries not included with
# Python3 (i.e. do not use `pip`).
import socket
import sys

BUFFER_SIZE = 4096
PASSWORD = 'password'

# Parse command-line arguments.
host     = sys.argv[1]
port     = int(sys.argv[2])
username = sys.argv[3]

# Establish a TCP connection with the POP3 server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


# Read greeting from the server.
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('+OK'):
    raise Exception('+OK not received from server.')

# Note: the POP3 spec requires every command to end with \r\n, not just \n.

# Log in with USER and PASS commands.
s.send(f'USER {username}\r\n'.encode())
s.recv(BUFFER_SIZE)
 
s.send(f'PASS {PASSWORD}\r\n'.encode())
s.recv(BUFFER_SIZE)


# Get the number of messages with the LIST command.
# Note: the LIST response spans multiple lines and ends with a line
# containing only '.'. Do not assume a fixed number of recv() calls will
# capture the full response — depending on the network, the entire response
# may arrive in a single recv() or be split across several. Accumulate data
# until you have seen the terminator.
s.send('LIST\r\n'.encode())
data = ""
while True:
    chunk = s.recv(BUFFER_SIZE).decode('utf-8')
    data += chunk
    if '\r\n.\r\n' in data:
        break

message_numbers = []
for line in data.splitlines()[1:-1]:
    message_numbers.append(line.split()[0])


# Retrieve and print each message with the RETR command.
# The same caveat about multi-line responses applies here.
# Print messages separated by a line containing only '---'.

for i in range(len(message_numbers)):
    s.send(f'RETR {message_numbers[i]}\r\n'.encode())
 
    msg_data = ""
    while True:
        chunk = s.recv(BUFFER_SIZE).decode('utf-8')
        msg_data += chunk
        if '\r\n.\r\n' in msg_data:
            break
        
    print(msg_data.replace('\r\n.\r\n', '').strip())

    if i < len(message_numbers) - 1:
            print("---")

# Close the socket when finished.
s.close()
