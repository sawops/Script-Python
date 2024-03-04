import tkinter as tk

class Calculadora:
    # Inicialización de la calculadora
    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        # Creación y configuración de la pantalla de la calculadora
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, background="#CAD2FC", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        # Variables para controlar operaciones y entradas
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0

        # Posicionamiento inicial para los botones
        row = 1
        col = 0
        # Lista de botones a ser creados
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", "="
        ]

        # Creación de botones a partir de la lista definida
        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            # Ajuste para cambiar de fila después de 4 botones
            if col > 3:
                col = 0
                row += 1

        # Configuración de evento de teclado
        self.master.bind("<Key>", self.key_press)

    # Método para gestionar la pulsación de teclas
    def key_press(self, event):
        key = event.char
        
        # Acciones especiales para Enter, Backspace y Esc
        if key == "\r":
            self.calculate()
            return
        elif key == "\x08":
            self.clear_display()
            return
        elif key == "\x1b":
            self.master.quit()
            return
        
        # Procesar la tecla presionada
        self.click(key)

    # Método para limpiar la pantalla
    def clear_display(self):
        self.display.delete(0, tk.END)
        # Reinicio de variables
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0

    # Método para realizar el cálculo
    def calculate(self):
        # Realiza la operación según el operador almacenado
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)
        
        # Muestra el resultado
        self.display.delete(0, "end")
        self.display.insert("end", round(self.total, 3))

    # Método para procesar la pulsación de los botones
    def click(self, key):
        if self.op_verification:
            self.op_verification = False
            
        self.display.insert("end", key)

        # Actualización de la entrada actual o del operador
        if key in "0123456789" or key == ".":
            self.current += key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)

            self.current = ''
            self.op_verification = True
            self.op = key

    # Método para construir los botones
    def build_button(self, button, row, col):
        # Configuración especial para botones 'C' y '='
        if button == "C":
            b = tk.Button(self.master, text=button, width=7, command=lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=7, command=lambda: self.calculate())    
        else:
            # Configuración para el resto de botones
            b = tk.Button(self.master, text=button, width=7, command=lambda: self.click(button))
        b.grid(row=row, column=col)

# Inicialización y ejecución de la calculadora
root = tk.Tk()
my_gui = Calculadora(root)
root.mainloop()
