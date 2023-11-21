import socket
import threading
import time

def server1(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    print(f"Servidor 1 escuchando en el puerto {port}")

    while True:
        client, addr = server_socket.accept()
        message = client.recv(1024)
        print(f"Mensaje recibido en Servidor 1: {message.decode()}")

        # Simula algún procesamiento en el servidor
        time.sleep(1)

        # Envia el mensaje al Cliente 2
        forward_to_client2(message)

        response = "Mensaje procesado por Servidor 1"
        client.sendall(response.encode())

        client.close()

def forward_to_client2(message):
    # Conéctate directamente al Cliente 2 y envía el mensaje
    client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2_socket.connect(('localhost', 8891))  # Cambia el puerto según tus necesidades
    client2_socket.sendall(message)
    client2_socket.close()

if __name__ == "__main__":
    server1(8889)  # Cambia el puerto según tus necesidades


