import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui_done = False

        self.root = tk.Tk()
        self.root.title("Chat App")
        self.chat_label = tk.Label(self.root, text="Chat:", font=("Arial", 14))
        self.chat_label.pack(padx=10, pady=5)

        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled')
        self.chat_area.pack(padx=10, pady=5)

        self.entry = tk.Entry(self.root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

        self.gui_done = True

        self.username = simpledialog.askstring("Username", "Enter your username", parent=self.root)
        self.client.connect(('127.0.0.1', 6060))  # make sure server is running on port 6060
        self.client.send(self.username.encode())

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.daemon = True
        receive_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        self.root.mainloop()

    def send_message(self):
        message = self.entry.get()
        if message:
            try:
                self.client.send(message.encode())
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, f"You: {message}\n")
                self.chat_area.yview(tk.END)
                self.chat_area.config(state='disabled')
                self.entry.delete(0, tk.END)
            except:
                self.chat_area.insert(tk.END, "Error sending message\n")

    def receive(self):
        while True:
            try:
                msg = self.client.recv(1024).decode()
                if self.gui_done:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, msg + "\n")
                    self.chat_area.yview(tk.END)
                    self.chat_area.config(state='disabled')
            except:
                break

    def stop(self):
        self.client.close()
        self.root.destroy()

if __name__ == "__main__":
    ChatClient()
