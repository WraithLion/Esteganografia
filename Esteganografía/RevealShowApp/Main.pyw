# En esta parte importamos Ocultamiento, Develar, os, tkinter, PIL, cv2, imutils y numpy
from Ocultamiento import Ocultamiento
from Develar import Develar
from pathlib import *
from tkinter import *
import os
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np

#Este método funciona para seleccionar una imagen y mostrarla en la GUI
def elegir_imagen():
    # Especificar los tipos de archivos, para elegir solo a las imágenes
    global path_image
    path_image = filedialog.askopenfilename(filetypes = [
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])
    if len(path_image) > 0:
        global image
        # Se lee la imagen de entrada y la redimensionamos
        image = cv2.imread(path_image)
        image= imutils.resize(image, height=380)
        # Para visualizar la imagen de entrada en la GUI
        imageToShow= imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)
        lblInputImage.configure(image=img)
        lblInputImage.image = img
        # Muestra en pantalla "Imagen de entrada:"
        lblInfo1 = Label(root, bg='#161b22', fg='#c7cdd3', text="Imagen de entrada:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)
        # Al momento que leemos la imagen de entrada, vaciamos
        # la imagen de salida y se limpia la selección de los
        # radiobutton
        lblOutputImage.image = ""
        selected.set(0)

def ocultar():
    #Llama al método ocultar y regresa la imagen modificada
    oculta = Ocultamiento()
    salidaImagen = oculta.ocultar(path_image)
    # Para visualizar la imagen en la GUI
    im = Image.open(path_image)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img
    
    # Sirve para colocar la etiqueta por encima de la imagen resultado
    lblInfo3 = Label(root, bg='#161b22', fg='#c7cdd3', text="Resultado:", font="bold")
    lblInfo3.grid(column=1, row=0, padx=5, pady=5)
    
    #Le pregunta al usuario la dirección en donde se guardará la imagen además del nombre de la imagen
    guardar = filedialog.asksaveasfilename(
                defaultextension='.png', filetypes=[("Formato png", '*.png')],
                title="Guardar como")
    direccion = PureWindowsPath(guardar)
    os.chdir(direccion.parents[0])
    nombre = PurePosixPath(guardar).name
    salidaImagen.save(nombre)
    
#Llama a la subrutina develar
def recuperar():
   devela=Develar()
   texto = devela.develar(path_image) 
   #guardar = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Formato txt", '*.txt')], title="Guardar como")
   #direccion = PureWindowsPath(guardar)
   #os.chdir(direccion.parents[0])
   #nombre = PurePosixPath(guardar).name
   #texto.write(nombre)  

# Creamos la ventana principal
root = Tk()

# Se presenta en la GUI la imagen de entrada
lblInputImage = Label(root, bg='#161b22')
lblInputImage.grid(column=0, row=2)
# Se presenta en la GUI la imagen de salida
lblOutputImage = Label(root, bg='#161b22')
lblOutputImage.grid(column=1, row=1, rowspan=6)

# Muestra en la GUI un mensaje para el usuario
lblInfo2 = Label(root, relief=RAISED, justify=CENTER, bg='#161b22', fg='#c7cdd3', borderwidth=0, text="Bienvenido a RevealShowApp: \n\n ¿Qué te gustaría hacer?", width=25)
lblInfo2.grid(column=0, row=3, padx=5, pady=5)

# Creamos los radio buttons y la ubicación que estos ocuparán
selected = IntVar()
rad1 = Radiobutton(root, bg='#161b22', fg='#c7cdd3', text='Ocultar', width=25,value=1, variable=selected, command= ocultar)
rad2 = Radiobutton(root, bg='#161b22', fg='#c7cdd3', text='Develar',width=25, value=2, variable=selected, command= recuperar)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)

# Creamos el botón para elegir la imagen de entrada
btn = Button(root, bg='#161b22', fg='#c7cdd3', text="Seleccionar imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5, pady=5)

#Establece algunas configuraciones para la aplicación
#Se modifica el color del fondo, impide que se redimensione la ventana y agrega un título a la ventana
root.config(bg='#161b22')
root.resizable(False, False)
root.title("Estenografía por método LSB")
root.mainloop()