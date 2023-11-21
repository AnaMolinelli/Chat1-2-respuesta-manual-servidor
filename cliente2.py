import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

def receive_messages(socket):
    while True:
        try:
            response = socket.recv(1024).decode()
            if not response:
                break  # Salir del bucle si la respuesta está vacía
            root.after(10, lambda: chat_box.insert(tk.END, f"Recibido: {response}\n"))
        except ConnectionAbortedError:
            break
        except Exception as e:
            print(f"Error al recibir mensajes: {e}")
            break

# Función para enviar mensajes al proxy
def send_message():
    message = entry.get()
    chat_box.insert(tk.END, f"Enviado: {message}\n")
    proxy_socket.sendall(message.encode())
    entry.delete(0, tk.END)

# Interfaz gráfica
root = tk.Tk()
root.title("Chat Cliente 2")
root.geometry("400x300")

chat_box = scrolledtext.ScrolledText(root, width=40, height=10)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Configura el socket del cliente para el proxy
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.connect(('localhost', 8888))  # Cambia el puerto según tus necesidades

# Inicia hilos para recibir mensajes de ambos servidores
receive_thread1 = threading.Thread(target=receive_messages, args=(proxy_socket,))
receive_thread1.start()

root.mainloop()
