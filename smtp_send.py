#!/usr/bin/env python3

# Include needed libraries. Do _not_ include any libraries not included with
# Python3 (i.e. do not use `pip`).
import socket
import sys

BUFFER_SIZE = 4096

# Parse command-line arguments.
host    = sys.argv[1]
port    = int(sys.argv[2])
from_addr = sys.argv[3]
to_addr   = sys.argv[4]
subject   = sys.argv[5]

# Read the email body from standard input.
body = sys.stdin.read()

# Establish a TCP connection with the SMTP server.


# Read greeting from the server.
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('220'):
    raise Exception('220 reply not received from server.')

# Note: the SMTP spec requires every command to end with \r\n, not just \n.
# This applies to commands (HELO, MAIL FROM, etc.) and to the message headers
# and body sent after DATA.

# Send HELO command and get server response.
s.send('HELO client\r\n'.encode())
response = s.recv(BUFFER_SIZE).decode('utf-8')
if not response.startswith('250'):
    raise Exception('250 reply not received from server.')

# Send MAIL FROM command.


# Send RCPT TO command.


# Send DATA command.


# Send message headers and body.


# End message with a line containing only a period.


# Send QUIT command.


# Close the socket when finished.
s.close()
