import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Server details
HOST = '127.0.0.1'  # Localhost (change to server IP for remote connection)
PORT = 12345         # Port to connect

# Setup the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, "Friend: " + message + '\n')
            chat_box.config(state=tk.DISABLED)
        except:
            break

# Function to send messages to the server
def send_message(event=None):
    message = message_entry.get()
    if message != "":
        client_socket.send(message.encode('utf-8'))
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + '\n')
        chat_box.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)

# GUI for the Client
def client_gui():
    # Create the window
    client_window = tk.Tk()
    client_window.title("Client Chat")
    client_window.geometry("400x400")

    # Text box for showing chat messages
    global chat_box
    chat_box = scrolledtext.ScrolledText(client_window, wrap=tk.WORD, width=50, height=20)
    chat_box.pack(pady=10)
    chat_box.config(state=tk.DISABLED)

    # Entry box to type messages
    global message_entry
    message_entry = tk.Entry(client_window, width=50)
    message_entry.pack(pady=5)
    message_entry.bind("<Return>", send_message)

    # Send message button
    send_button = tk.Button(client_window, text="Send", command=send_message)
    send_button.pack()

    # Start receiving messages in a separate thread
    threading.Thread(target=receive_messages, daemon=True).start()

    # Run the GUI
    client_window.mainloop()

if __name__ == "__main__":
    client_gui()
