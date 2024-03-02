import tkinter as tk 
from tkinter import filedialog, messagebox

# Define una clase SimpleTextEditor para crear una interfaz gráfica de usuario (GUI) de un editor de texto simple.
class SimpleTextEditor:
    # Constructor que inicializa la ventana principal y los componentes del editor de texto.
    def __init__(self, root):
        self.root = root  # La ventana principal de la aplicación.
        self.text_area = tk.Text(self.root)  # Área de texto para la edición.
        self.text_area.pack(fill=tk.BOTH, expand=1)  # Expandir el área de texto para llenar la ventana.
        self.current_open_file = ''  # Rastrear el archivo actualmente abierto o en edición.

    # Función para abrir un archivo existente.
    def open_file(self):
        filename = filedialog.askopenfilename()  # Muestra un diálogo para seleccionar un archivo.

        if filename:
            self.text_area.delete("1.0", tk.END)  # Limpia el área de texto antes de cargar el nuevo archivo.
            with open(filename, 'r') as file:
                self.text_area.insert("1.0", file.read())  # Inserta el contenido del archivo en el área de texto.

            self.current_open_file = filename  # Actualiza el archivo actualmente abierto.

    # Función para confirmar el cierre de la aplicación.
    def quit_confirm(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.root.destroy()  # Cierra la ventana principal y termina la aplicación.

    # Función para crear un nuevo archivo.
    def new_file(self):
        self.text_area.delete("1.0", tk.END)  # Limpia el área de texto.
        self.current_open_file = ''  # Resetea el archivo actualmente abierto.

    # Función para guardar el archivo actual.
    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()  # Muestra un diálogo para guardar el archivo.

            if new_file_path:
                self.current_open_file = new_file_path
            else:
                return  # Sale de la función si no se proporciona una ruta de archivo.
            
        with open(self.current_open_file, 'w') as file:
            file.write(self.text_area.get("1.0", tk.END))  # Escribe el contenido del área de texto en el archivo.

# Configuración inicial de la ventana principal de Tkinter.
root = tk.Tk()
root.geometry("700x500")  # Define el tamaño de la ventana.

editor = SimpleTextEditor(root)  # Crea una instancia del editor de texto.

# Configura la barra de menú y las opciones.
menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

# Añade opciones al menú y enlaza las funciones correspondientes.
menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)

root.config(menu=menu_bar)  # Configura la barra de menú en la ventana principal.
menu_bar.add_cascade(label="Archivo", menu=menu_options)  # Añade el menú de opciones a la barra de menú.

root.mainloop()  # Inicia el bucle principal de Tkinter para mantener abierta la aplicación.
