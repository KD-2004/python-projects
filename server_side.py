import socket
import os
import threading


def handle_client(client_socket):
    cwd = os.getcwd()

    while True:
        command = client_socket.recv(1024).decode('utf-8')
        if not command:
            break

        if command.startswith('cd '):
            # Change working directory
            directory = command[3:].strip()
            try:
                os.chdir(directory)
                cwd = os.getcwd()
                client_socket.send(f'Changed directory to {cwd}\n'.encode('utf-8'))
            except OSError as e:
                client_socket.send(f'Error: {e}\n'.encode('utf-8'))
        elif command.strip() == 'logout':
            # Exit the loop and close the socket
            client_socket.send('Exiting...'.encode('utf-8'))
            break
        else:
            # Execute command
            with os.popen(f'{command} 2>&1') as output:
                client_socket.send(output.read().encode('utf-8'))

    client_socket.close()


def start_server():
    host = '127.0.0.1'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f'Server listening on {host}:{port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Accepted connection from {addr[0]}:{addr[1]}')

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == '__main__':
    start_server()
