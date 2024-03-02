import socket

def start_udp_server():
    # Configuración de la dirección IP del host y el puerto en el que el servidor escuchará
    host = 'localhost'  # El servidor escuchará en todas las interfaces de red de la máquina local
    port = 1234  # Puerto arbitrario para el servicio UDP

    # Creación de un socket UDP
    # AF_INET especifica que usaremos IPv4
    # SOCK_DGRAM indica que este será un socket de tipo Datagram, usado por UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # El servidor se "enlaza" a la dirección y puerto especificados para empezar a escuchar
        s.bind((host, port))
        print(f"\n[+] Servidor UDP iniciado en {host}:{port}")

        # Bucle infinito para escuchar mensajes entrantes
        while True:
            # Recepción de datos del cliente
            # `recvfrom` bloquea la ejecución hasta que llega un mensaje, retorna los datos y la dirección del remitente
            # 1024 es el tamaño del buffer, en bytes
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Mensaje enviado por el cliente: {data.decode()}")  # Decodifica y muestra el mensaje
            print(f"[+] Informacion del cliente que nos ha enivado el mensaje: {addr}")  # Muestra la dirección del remitente

start_udp_server()  # Invoca la función para iniciar el servidor
