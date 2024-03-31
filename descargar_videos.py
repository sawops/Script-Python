from tkinter import *  # Importa todo desde tkinter para la interfaz gráfica de usuario
from pytube import YouTube  # Importa YouTube desde pytube para descargar videos

# Inicializa la ventana principal de la aplicación
root = Tk()
root.geometry('500x300')  # Define el tamaño de la ventana
root.resizable(0, 0)  # Impide que la ventana sea redimensionable
root.title('Descargador de videos de YouTube')  # Título de la ventana
root.configure(bg='#AACDE2')  # Color de fondo de la ventana

# Etiqueta para el título de la aplicación
Label(root, text='Descarga tus videos !!', font='arial 20 bold', bg='#AACDE2').pack(pady=20)

# Variable para almacenar el enlace del video
link = StringVar()

# Etiqueta para instruir al usuario a pegar el enlace
Label(root, text='Pega el enlace aquí:', font='arial 15', bg='#AACDE2').pack(pady=5)

# Entrada para pegar el enlace del video
link_enter = Entry(root, width=70, textvariable=link).pack(pady=5)

# Función para manejar la descarga
def Downloader():
    url = YouTube(str(link.get()))  # Obtiene el enlace del video y crea un objeto YouTube
    video = url.streams.get_highest_resolution()  # Obtiene la mayor resolución disponible
    video.download()  # Descarga el video
    Label(root, text='DESCARGADO', font='arial 15 bold', bg='#AACDE2', fg='#B57199').pack(pady=20)  # Notifica al usuario que el video ha sido descargado

    link.set("")  # Limpia la barra de entrada después de la descarga

# Botón para iniciar la descarga
Button(root, text='DESCARGAR', font='arial 15 bold', bg='#B57199', pady=10, command=Downloader).pack()

# Bucle principal de tkinter para mantener abierta la interfaz gráfica
root.mainloop()
