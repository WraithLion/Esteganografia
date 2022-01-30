# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz
from PIL import Image
#Importa PIL una biblioteca que permite la edicion de imágenes
from tkinter import filedialog
#Importa tkinter una biblioteca gráfica que permite implementar una interfaz gráfica
from tkinter import messagebox
#Importa de la misma biblioteca una seccion que permite enviar cuadros de mensajes
"""Clase Imagen para obtener los detalles de la imagen para su respectiva operacion"""
class Imagen:

    def cargarimagen(self):
        '''Funcion que permite cargar la imagen'''
        '''imagen: Almacena los datos de la imagen dada'''
        global imagen
        '''Primero necesita la imagen para ello solicita la ubicacion para cargar los datos y los almacena en la variable rutaImagen'''
        rutaImagen = filedialog.askopenfilename(defaultextension='.png',filetypes = [("Formato png", ".png")],title="Selecciona la imagen que deseas utilizar")
        '''Revisa si la variable rutaImagen tiene informacion'''
        if  len(rutaImagen)==0:
            '''Si está vacia envía un mensaje que el usuario debe seleccionar una imagen'''
            messagebox.showinfo(message="Debes seleccionar una imagen", title="Aviso")
            '''S'''
            self.cargarimagen()
        else:

            imagen= Image.open(rutaImagen)
        '''Regresa los datos de la imagen'''
        return imagen

    def obtenerdimensiones(self,datosImagen):

        tamaño=datosImagen.size

        return tamaño

    def obtenerancho(self,dimensiones):

        ancho=dimensiones[0]

        return ancho

    def obtenerlargo(self,dimensiones):

        largo=dimensiones[1]

        return largo

    def obtenerpixeles(self,datosImagen):

        pixeles=datosImagen.load()

        return pixeles

    def PixelesNecesarios(self,cantidad,pixelesdisponibles,largo):

        espacio=0

        while cantidad > largo:

            cantidad=cantidad-largo

            espacio=espacio+1

        PixelesReservados= []

        veces=0

        while veces<espacio:

            for i in range(largo):

                PixelesReservados.append(pixelesdisponibles[veces,i])

            veces=veces+1

        for i in range(cantidad):

            PixelesReservados.append(pixelesdisponibles[espacio,i])

        return PixelesReservados

    def PixelEnBinario(self,ListaPixeles):

        tamañoLista=len(ListaPixeles)

        ListaBinaria=[]

        for i in range(tamañoLista):

            for j in range(3):

                NumeroBinario=bin(ListaPixeles[i][j])[2:].zfill(8)

                ListaBinaria.append(NumeroBinario)

        return ListaBinaria

    def AnchoRequerido(self,cantidad,largo):

        ancho=0

        while cantidad > largo:

            cantidad=cantidad-largo

            ancho=ancho+1

            return ancho

        return ancho

    def PixelDecimal(self,Lista):

        longitud=len(Lista)

        RGBModificado=[]

        for i in range(longitud):

            valorRGB=int(Lista[i],2)

            RGBModificado.append(valorRGB)

        return RGBModificado


