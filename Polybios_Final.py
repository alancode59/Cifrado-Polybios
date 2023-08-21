#Programa metodo de cifrado y descifrado Polybios con interfaz

#Alan Zaid Hernandez Cruz
#9c


import tkinter as tk
from PIL import ImageTk, Image
import string

# Paleta de colores
COLOR_BG = "#000000"  #fondo negro
COLOR_PRIMARY = "#F44336"  #color rojo
COLOR_SECONDARY = "#4CAF50"  #color verde
COLOR_ACCENT = "#673AB7"  #color purpura

INTERFAZ_ANCHO = 480
INTERFAZ_ALTO = 800

#Definimos una función llamada polybios que crea y almacena la matriz de 5x5
def polybios():
    #Definimos la variable abecedario para almacenar el alfabeto sin la letra "W"
    abecedario = string.ascii_uppercase.replace('W', '')
    
    tablaPoly = [['' for _ in range(5)] for _ in range(5)]  # Inicializamos la matriz vacía
    indice = 0  #Inicializamos el índice para recorrer el abecedario

    #Recorremos la fila de la matriz
    for i in range(5):
        for j in range(5):  #Recorremos las columnas de la matriz
            if i == 4 and j == 4:  #si llegamos a la última posición, asignamos la última letra a la tabla
                tablaPoly[i][j] = 'Z'  #ultima letra
            else:
                tablaPoly[i][j] = abecedario[indice]  #asignamos la letra correspondiente al abecedario
                indice += 1  #incrementamos el índice

    #retornamos la matriz completa
    return tablaPoly


#creamos una función para cifrar el mensaje, a la cual le pasamos el mensaje y la tabla Polybios
def cifrar(mensaje, tablaPoly):
    #definimos la variable para almacenar el mensaje cifrado
    mensaje_cifrado = ''
    
    #convertimos el mensaje a mayúsculas y reemplazamos 'W' por 'V' según el método Polybios
    mensaje = mensaje.upper().replace('W', 'V')

    #iteramos en cada uno de los caracteres del mensaje
    for caracter in mensaje:
        #si el caracter es un espacio, se añade un espacio al mensaje cifrado y se continúa con el siguiente caracter
        if caracter == ' ':
            mensaje_cifrado += ' '
            continue
        
        for i in range(5):  #iteramos sobre las filas de la tabla Polybios
            for j in range(5):  #iteramos sobre las columnas de la tabla Polybios
                #si el caracter coincide con el elemento en la posición (i, j) de la tablaPoly
                if caracter == tablaPoly[i][j]:
                    #agregamos las coordenadas (j+1, i+1) al mensaje cifrado
                    mensaje_cifrado += str(j+1) + str(i+1)
                    break

    #retornamos el mensaje cifrado
    return mensaje_cifrado


#creamos una función para descifrar el mensaje, a la cual le pasamos el mensaje cifrado y la tabla Polybios
def descifrar(mensaje_cifrado, tablaPoly):
    #definimos la variable para almacenar el mensaje descifrado
    mensaje_descifrado = ''
    
    i = 0  #inicializamos el contador para recorrer el mensaje cifrado
    
    #iteramos hasta llegar al final del mensaje cifrado
    while i < len(mensaje_cifrado):
        #si el carácter actual es un espacio, se añade un espacio al mensaje descifrado y se pasa al siguiente carácter
        if mensaje_cifrado[i] == ' ':
            mensaje_descifrado += ' '
            i += 1
            continue
        
        #asignamos la variable "columna" para obtener el número de columna a partir del primer dígito del par de coordenadas
        columna = int(mensaje_cifrado[i]) - 1
        #asignamos la variable "fila" para obtener el número de fila a partir del segundo dígito del par de coordenadas
        fila = int(mensaje_cifrado[i+1]) - 1

        #añadimos el carácter correspondiente a las coordenadas fila y columna al mensaje descifrado
        mensaje_descifrado += tablaPoly[fila][columna]
        #avanzamos dos posiciones para pasar al siguiente par de coordenadas
        i += 2
    
    #retornamos la funcion del mensaje descifrado
    return mensaje_descifrado


def abrir_ventana1():
    ventana1 = tk.Toplevel()
    ventana1.title("Cifrar")
    ventana1.configure(bg=COLOR_BG)
    ventana1.geometry(f"{INTERFAZ_ANCHO}x{INTERFAZ_ALTO}")

    def obtener_texto():
        mensaje = entry.get()
        mensaje_cifrado = cifrar(mensaje, tablaPoly)
        resultado.config(text=f"El mensaje cifrado es: {mensaje_cifrado}")

    label = tk.Label(ventana1, text="Ingresa el Mensaje a Cifrar", bg=COLOR_BG, fg="white", font=("Arial", 14, "bold"))
    label.pack(pady=20)
    
    #cargamos la imagen
    imagen1 = Image.open("imgs/matrizPoly.png")
    imagen1 = imagen1.resize((200, 200))  # Ajustar el tamaño de la imagen si es necesario
    imagen1 = ImageTk.PhotoImage(imagen1)

    #mostramos la imagen en un widget Label
    label_imagen1 = tk.Label(ventana1, image=imagen1, bg=COLOR_BG)
    label_imagen1.pack(pady=20)

    entry = tk.Entry(ventana1)
    entry.pack()

    button_frame = tk.Frame(ventana1, bg=COLOR_BG)
    button_frame.pack(pady=20)

    button_aceptar = tk.Button(button_frame, text="Aceptar", command=obtener_texto, bg=COLOR_PRIMARY, fg="white", width=15)
    button_aceptar.pack(side=tk.LEFT, padx=15)

    button_regresar = tk.Button(button_frame, text="Regresar", command=ventana1.destroy, bg=COLOR_SECONDARY, fg="white", width=15)
    button_regresar.pack(side=tk.LEFT, padx=15)

    resultado = tk.Label(ventana1, text="", bg=COLOR_BG, fg="white", font=("Arial", 13))
    resultado.pack(pady=15)
    
    ventana1.mainloop()

def abrir_ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title("Descifrar")
    ventana2.configure(bg=COLOR_BG)
    ventana2.geometry(f"{INTERFAZ_ANCHO}x{INTERFAZ_ALTO}")

    def obtener_texto():
        mensaje_cifrado = entry.get()
        mensaje_descifrado = descifrar(mensaje_cifrado, tablaPoly)
        resultado.config(text=f"El mensaje descifrado es: {mensaje_descifrado}")

    label = tk.Label(ventana2, text="Ingresa el Mensaje a Descifrar", bg=COLOR_BG, fg="white", font=("Arial", 14, "bold"))
    label.pack(pady=20)

    #cargar la imagen
    imagen2 = Image.open("imgs/descifradovolf.jpg")
    imagen2 = imagen2.resize((200, 200))  # Ajustar el tamaño de la imagen si es necesario
    imagen2 = ImageTk.PhotoImage(imagen2)

    #mostrar la imagen en un widget Label
    label_imagen2 = tk.Label(ventana2, image=imagen2, bg=COLOR_BG)
    label_imagen2.pack(pady=20)

    entry = tk.Entry(ventana2)
    entry.pack()

    button_frame = tk.Frame(ventana2, bg=COLOR_BG)
    button_frame.pack(pady=20)

    button_aceptar = tk.Button(button_frame, text="Aceptar", command=obtener_texto, bg=COLOR_PRIMARY, fg="white", width=15)
    button_aceptar.pack(side=tk.LEFT, padx=15)

    button_regresar = tk.Button(button_frame, text="Regresar", command=ventana2.destroy, bg=COLOR_SECONDARY, fg="white", width=15)
    button_regresar.pack(side=tk.LEFT, padx=15)

    resultado = tk.Label(ventana2, text="", bg=COLOR_BG, fg="white", font=("Arial", 13))
    resultado.pack(pady=15)
    
    ventana2.mainloop()

#Crear una ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Polybios")
ventana_principal.geometry(f"{INTERFAZ_ANCHO}x{INTERFAZ_ALTO}")
ventana_principal.configure(bg=COLOR_BG)

etiqueta = tk.Label(ventana_principal, text="Bienvenido al Método de Cifrado Polybios", bg=COLOR_BG, fg="white", font=("Arial", 14, "bold"))
etiqueta.pack(pady=20)

#cargar la imagen
imagen = Image.open("imgs/final.png")
imagen = imagen.resize((200, 200))  # Ajustar el tamaño de la imagen si es necesario
imagen = ImageTk.PhotoImage(imagen)

#mostrar la imagen en un widget Label
label_imagen = tk.Label(ventana_principal, image=imagen, bg=COLOR_BG)
label_imagen.pack(pady=20)

tablaPoly = polybios()  #creamos la tabla Polybios

#crear dos botones
button1 = tk.Button(ventana_principal, text="Cifrar", command=abrir_ventana1, width=15, bg=COLOR_PRIMARY, fg="white")
button1.pack(pady=20)

button2 = tk.Button(ventana_principal, text="Descifrar", command=abrir_ventana2, width=15, bg=COLOR_PRIMARY, fg="white")
button2.pack(pady=20)

#boton para cerrar la ventana principal y todas las ventanas secundarias
button_cerrar = tk.Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy, bg=COLOR_ACCENT, fg="white", width=15)
button_cerrar.pack(pady=20)

#iniciar el bucle principal de la ventana
ventana_principal.mainloop()
