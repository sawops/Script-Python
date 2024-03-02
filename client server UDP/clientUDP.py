import socket

def start_udp_client():
    # Configuración de la dirección IP y puerto del servidor al que se enviarán los mensajes
    host = 'localhost'  # IP del servidor
    port = 1234  # Puerto en el que el servidor está escuchando

    # Creación de un socket UDP
    # AF_INET especifica el uso de IPv4
    # SOCK_DGRAM indica que este será un socket de tipo Datagram, usado por UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = "Hola, se está tensando muchísimo".encode("utf-8")  # El mensaje a enviar, codificado a bytes
        s.sendto(message, (host, port))  # Envío del mensaje al servidor

start_udp_client()  # Invocación de la función para iniciar el cliente
