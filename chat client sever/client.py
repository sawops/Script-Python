import socket

def start_chat_client():
    # Configuración del servidor al cual conectarse.
    host = 'localhost'
    port = 12345

    # Establecimiento de la conexión TCP con el servidor.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))

    while True:
        # Captura y envío de mensajes al servidor.
        client_message = input(f"\n[+] Mensaje para enviar al servidor: ")
        client_socket.send(client_message.encode())

        # Condicional para terminar la conexión si se escribe 'bye'.
        if client_message == 'bye':
            break
        
        # Recepción y muestra de mensajes del servidor.
        server_message = client_socket.recv(1024).strip().decode()
        print(f"\n[+ Mensaje del servidor: {server_message}]")

    # Cierre de la conexión al finalizar.
    client_socket.close()

start_chat_client()
