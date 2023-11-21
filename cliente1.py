import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            if not response:
                break  # Salir del bucle si la respuesta está vacía
            root.after(10, lambda: chat_box.insert(tk.END, f"Recibido desde Servidor: {response}\n"))
        except ConnectionAbortedError:
            break
        except Exception as e:
            print(f"Error al recibir mensajes: {e}")
            break

# Función para enviar mensajes al servidor
def send_message():
    message = entry.get()
    chat_box.insert(tk.END, f"Enviado desde Cliente 1: {message}\n")
    client_socket.sendall(message.encode())
    entry.delete(0, tk.END)

# Interfaz gráfica
root = tk.Tk()
root.title("Chat Cliente 1")
root.geometry("400x300")

chat_box = scrolledtext.ScrolledText(root, width=40, height=10)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Configura el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

# Inicia un hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
