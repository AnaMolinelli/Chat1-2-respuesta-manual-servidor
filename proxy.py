import socket
import threading

def proxy():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(('localhost', 8888))
    proxy_socket.listen(5)

    print("Proxy escuchando en el puerto 8888")

    while True:
        client, addr = proxy_socket.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    try:
        message = client.recv(1024)
        forward_to_available_server(message)
        client.close()
    except Exception as e:
        print(f"Error en la conexión del proxy: {e}")

def forward_to_available_server(message):
    # Intenta conectarse al Servidor 1
    if try_forward_to_server(message, ('localhost', 8889)):
        return

    # Intenta conectarse al Servidor 2
    if try_forward_to_server(message, ('localhost', 8890)):
        return

    # Ambos servidores están apagados, envía un mensaje de indisponibilidad
    send_unavailable_message()

def try_forward_to_server(message, server_address):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(server_address)
        server_socket.sendall(message)
        server_socket.close()
        return True
    except Exception as e:
        print(f"Error al intentar conectar con el servidor {server_address}: {e}")
        return False

def send_unavailable_message():
    # Conéctate directamente al Cliente 1 y envía un mensaje de indisponibilidad
    client1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1_socket.connect(('localhost', 8889))  # Cambia el puerto según tus necesidades
    client1_socket.sendall("Los servidores no están disponibles en este momento.".encode('utf-8'))
    client1_socket.close()

if __name__ == "__main__":
    proxy()

    proxy()

