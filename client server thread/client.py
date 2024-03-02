import socket

def start_client():
    # Configura el host y el puerto para conectarse al servidor
    host = 'localhost'
    port = 1234

    # Crea un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Se conecta al servidor definido por host y port
        s.connect((host, port))

        # Bucle infinito para enviar mensajes al servidor
        while True:
            message = input("\n[+] Introduce tu mensaje: ")  # Solicita al usuario un mensaje
            s.sendall(message.encode())  # Envía el mensaje codificado al servidor

            if message == 'bye':  # Si el mensaje es 'bye', termina el bucle
                break
            
            data = s.recv(1024)  # Recibe la respuesta del servidor
            print(f"\n[+] Mensaje de respuesta del servidor: {data.decode()}")  # Imprime la respuesta

start_client()  # Inicia la función del cliente
