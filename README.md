# 💬 Browser-Based Chat Application

This is a **Python-based socket chat application** with a **Tkinter GUI**, allowing real-time communication between multiple users over a local network (LAN).

Both server and client components are implemented using Python's `socket`, `threading`, and `tkinter` libraries.

---

## 🚀 Features

- 🖥️ Desktop-based GUI for clients (Tkinter)
- 📡 Real-time messaging via TCP sockets
- 👥 Multi-user support (chatroom)
- 🎯 Server runs locally on `127.0.0.1`
- 🔐 Graceful disconnection handling
- 🔄 Threading for non-blocking I/O

---

## 🗂️ Project Structure

-Browser-Based-Chat-Application/
│
├── chat_server.py # Python script for server
├── chat_client.py # Python GUI script for client
├── requirements.txt # (optional) list of dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🛠️ Requirements

All required modules are part of Python's standard library:

- `socket`
- `threading`
- `tkinter`

✅ No external libraries are required.

---

## ⚙️ How to Run

> Make sure you're using **Python 3.x** and run both scripts from the same network/machine.

### 🔵 Step 1: Run the Server

```bash
python chat_server.py
The server will start listening on 127.0.0.1:12345 (or as configured).

🟢 Step 2: Run Clients
In a new terminal (or multiple):

bash
Copy code
python chat_client.py
Enter a username when prompted.

Start chatting in the GUI!

📸 Screenshots
(You can add your own screenshots here)
Example:

💡 Future Enhancements
Add message timestamps

Add user join/leave notifications

Switch to WebSockets for browser-based frontend

Add emoji or file transfer support

📄 License
This project is open source under the MIT License.

👨‍💻 Author
Adarsh Tiwari
🔗 GitHub: @Adarsh-hello
