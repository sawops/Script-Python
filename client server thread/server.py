import socket
import threading

# Define una clase para manejar cada conexión de cliente en un hilo separado
class ClientThread(threading.Thread):
    # Constructor que inicializa el socket del cliente y su dirección
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr
        print(f"\n[+] Nuevo cliente conectado: {client_addr}")

    # Método que se ejecuta cuando el hilo comienza
    def run(self):
        message = ''

        while True:
            data = self.client_sock.recv(1024)  # Recibe datos del cliente
            message = data.decode()

            if message.strip() == 'bye':  # Cierra la conexión si el mensaje es 'bye'
                break

            print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
            self.client_sock.send(data)  # Envía de vuelta el mismo mensaje al cliente

        print(f"\n[+] Cliente {self.client_addr} desconectado")
        self.client_sock.close()  # Cierra el socket del cliente

HOST = 'localhost'
PORT = 1234

# Crea un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reutilizar la dirección IP
    server_socket.bind((HOST, PORT))  # Enlaza el socket al puerto

    print(f"\n[+] En espera de conexiones entrantes...")

    while True:
        server_socket.listen()  # Escucha por conexiones entrantes
        client_sock, client_addr = server_socket.accept()  # Acepta una nueva conexión

        # Crea un nuevo hilo para manejar la conexión del cliente
        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start()  # Inicia el hilo
