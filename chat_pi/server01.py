import socket
from threading import Thread

# Server's IP address
SERVER_HOST = "192.168.0.107"
SERVER_PORT = 8080  # port we want to use
separator_token = "<SEP>"  # we will use this to separate the client name & message

# Initialize list/set of all connected client's sockets
client_sockets = set()

# Create a TCP socket
s = socket.socket()

# Make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))

# Listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    """
    This function keeps listening for a message from `cs` socket.
    Whenever a message is received, broadcast it to all other connected clients.
    """
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
            for client_socket in client_sockets:
                client_socket.send(msg.encode())

def accept_connections():
    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        client_sockets.add(client_socket)
        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    accept_connections()
