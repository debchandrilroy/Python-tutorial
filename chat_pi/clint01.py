import socket
from threading import Thread

# Server's IP address
SERVER_HOST = "192.168.0.107"
SERVER_PORT = 8080  # server's port
separator_token = "<SEP>"  # we will use this to separate the client name & message

# Initialize TCP client socket
s = socket.socket()

# Connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# Start listening for messages in a separate thread
Thread(target=listen_for_messages).start()

# Prompt the client for a name
name = input("Enter your name: ")

while True:
    # Input message we want to send to the server
    to_send = input("Enter a message: ")
    # A way to exit the program
    if to_send.lower() == 'q':
        break
    # Add the name and the separator token to the message
    to_send = f"{name}{separator_token}{to_send}"
    # Finally, send the message
    s.send(to_send.encode())

# Close the socket
s.close()
