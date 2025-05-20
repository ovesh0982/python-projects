import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Server details
HOST = '127.0.0.1'  # Localhost
PORT = 12345         # Port to bind

# Setup the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                broadcast(msg, client_socket)
            else:
                remove(client_socket)
        except:
            continue

# Function to broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Function to remove client from the list
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# GUI for the Server
def server_gui():
    # Create the window
    server_window = tk.Tk()
    server_window.title("Server Chat")
    server_window.geometry("400x400")

    # Text box for showing chat messages
    chat_box = scrolledtext.ScrolledText(server_window, wrap=tk.WORD, width=50, height=20)
    chat_box.pack(pady=10)
    chat_box.config(state=tk.DISABLED)

    # Accept client connection and create a thread to handle them
    def accept_connections():
        while True:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, f"New connection from {client_address}\n")
            chat_box.config(state=tk.DISABLED)
            threading.Thread(target=handle_client, args=(client_socket,)).start()

    threading.Thread(target=accept_connections, daemon=True).start()

    # Run the GUI
    server_window.mainloop()

if __name__ == "__main__":
    server_gui()
