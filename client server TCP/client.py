import socket

def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hola, servidor!")
        data = s.recv(1024)
        
        
    print(f"\n[+] Mesaje recibido del servidor:{data.decode()}")