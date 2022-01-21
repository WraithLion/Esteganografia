# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz
from tkinter import *
from tkinter import filedialog
from pathlib import *
from PIL import Image

class Imagen:

    def cargarimagen(self, nombrefoto):
        
        #nombrefoto = filedialog.askopenfilename(filetypes = [
        #("image", ".jpeg"),
        #("image", ".png"),
        #("image", ".jpg")])
        
        foto = PurePosixPath(nombrefoto).name

        imagen= Image.open(foto)

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

#imagen= Imagen()
#datosImagen=imagen.cargarimagen()
#dimensiones=imagen.obtenerdimensiones(datosImagen)
#ancho=imagen.obtenerancho(dimensiones)
#print(ancho)
#largo=imagen.obtenerlargo(dimensiones)
#print(largo)
#Pixeles=imagen.obtenerpixeles(datosImagen)
#Lista= imagen.PixelesNecesarios(110,Pixeles,largo)
#print(Lista)
#ListaRGBBinaria=imagen.PixelEnBinario(Lista)
#print(ListaRGBBinaria)
