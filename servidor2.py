import socket
import time  # Agrega esta importación

def server1(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    print(f"Servidor 1 escuchando en el puerto {port}")

    while True:
        client, addr = server_socket.accept()
        message = client.recv(1024)
        print(f"Mensaje recibido en Servidor 1: {message.decode()}")

        # Procesa el mensaje (puedes implementar tu lógica aquí)

        response = "Mensaje procesado por Servidor 1"
        client.sendall(response.encode())

        # Agrega una pausa antes de cerrar la conexión
        time.sleep(1)

        client.close()

if __name__ == "__main__":
    server1(8890)  # Cambia el puerto según tus necesidades
