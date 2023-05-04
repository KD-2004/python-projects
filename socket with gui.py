import tkinter as tk
import socket
import threading

s = socket.socket()

root = tk.Tk()
root.geometry("600x600")

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("300x300")
    label = tk.Label(new_window)
    label.pack()

    def get_ip():
        a = socket.gethostname()
        b = socket.gethostbyname(a)
        label.config(text=b)

    def ip_web():
        entry = tk.Entry(new_window)
        entry.pack()

        def entry_get():
            b = entry.get()
            a = socket.gethostbyname(b)
            label.config(text=a)

        button = tk.Button(new_window, text="submit", command=entry_get)
        button.pack()

    def socket_server():
        host = "127.0.1.1"
        port = 1234
        print("ip is and port is ", host, port)

        s.bind((host, port))
        s.listen()

        print("<<<<<<<<<<<waiting for the connection>>>>>>>>>>")

        conn, addr = s.accept()
        conn.send(b"hi!! ")
        data = conn.recv(1024)
        label.config(text=data.decode())
        conn.close()
        s.close()

    def client_side():
        ip = "127.0.1.1"
        port = 1234
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as b:
            b.connect((ip, port))
            b.sendall(b'Hello, server')
            data = s.recv(1024)
            label.config(text=data)

    button1 = tk.Button(new_window, text="Click here for your IP", command=get_ip)
    button1.pack()
    button2 = tk.Button(new_window, text="Click here for any website IP", command=ip_web)
    button2.pack()
    button3 = tk.Button(new_window, text="Click here for server socket creation", command=lambda: threading.Thread(target=socket_server).start())
    button3.pack()
    button4 = tk.Button(new_window, text="Click here for client socket creation", command=lambda: threading.Thread(target=client_side).start())
    button4.pack()

button = tk.Button(root, text="Open new window", command=open_new_window)
button.pack()

root.mainloop()