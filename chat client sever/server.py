import socket

def start_chat_server():
    # Configuración del servidor para aceptar conexiones.
    host = 'localhost'
    port = 12345

    # Creación del socket del servidor y enlace a la dirección y puerto.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reutilizar la dirección rápidamente.
    server_socket.bind((host, port))
    server_socket.listen(1)  # El servidor escucha y permite una conexión pendiente.

    print(f"\n[+] Servidor listo para aceptar una conexión...")
    connection, client_addr = server_socket.accept()  # Aceptación de la conexión del cliente.
    print(f"\n[+] Se ha conectado el cliente {client_addr}")

    while True:
        # Recepción y muestra de mensajes del cliente.
        client_message = connection.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del cliente: {client_message}")

        # Condicional para terminar la sesión si el cliente dice 'bye'.
        if client_message == 'bye':
            break

        # Captura y envío de respuestas al cliente.
        server_message = input(f"\n[+] Mensaje para enviar al cliente:")
        connection.send(server_message.encode())

    # Cierre de la conexión con el cliente.
    connection.close()

start_chat_server()
