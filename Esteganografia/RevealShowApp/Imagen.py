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
        '''Funcion que permite obtener el tamaño de la imagen'''
        '''tamaño Alamcena el largo y ancho de la imagen'''
        tamaño=datosImagen.size
        '''Regresa las dimensiones de la imagen'''
        return tamaño

    def obtenerancho(self,dimensiones):
        '''Funcion que permite obtener el ancho de la imagen'''
        ancho=dimensiones[0]
        '''Regresa el ancho de la imagen'''
        return ancho

    def obtenerlargo(self,dimensiones):
        '''Funcion que permite obtener el largo de la imagen'''
        largo=dimensiones[1]
        '''Regresa el largo de la imagen'''
        return largo

    def obtenerpixeles(self,datosImagen):
        '''Funcion que permite obtener los pixeles que constituyen a la imagen'''
        pixeles=datosImagen.load()
        '''Regresa los pixeles'''
        return pixeles

    def PixelesNecesarios(self,cantidad,pixelesdisponibles,largo):
        """Funcion que obtiene la cantidad e pixeles necesarios

        Notemos que, un pixel está compuesto de una tripleta, siendo los colores Rojo Verde y Azul en inglés RGB entonces se tiene que...

        Parámetros

        cantidad El número de pixeles necesarios para poder almacenar el mensaje ya convertido en binario.

        pixelesdisponibles El número de pixeles disponibles para almacenar la informacion binaria

        largo Número que se necesita para conocer el límite de pixeles y poder pasar al siguiente pixel de ancho.

        """

        '''espacio Almacena el ancho necesitado si hacen falta una vez ocupados del primer espacio'''
        espacio=0

        '''Si los pixeles necesarios sobrepasan al largo de la imagen'''
        while cantidad > largo:
            '''Se obtiene el residuo de las dos variables'''
            cantidad=cantidad-largo
            '''Aumenta en uno el espacio para ocupar en ancho'''
            espacio=espacio+1
            '''Una vez realizado evalua de nuevo la condición hasta que la variable cantidad sea menor que los pixeles disponibles siendo el largo'''

        '''Pixeles Reservados guarda los pixeles a ocupar en una lista'''
        PixelesReservados= []

        '''veces Auxiliar para ocupar los pixeles en ancho necesarios de acuerdo a la variable espacio'''
        veces=0

        '''Teniendo en cuenta que espacio es el ancho necesario evalúa si veces es menor a la variable antes mencionada'''
        while veces<espacio:
            '''Entra en un ciclo para agregar los pixeles a la lista'''
            for i in range(largo):
                '''Agrega el pixel a la lista'''
                PixelesReservados.append(pixelesdisponibles[veces,i])
            '''Aumenta en uno veces y revalua la condicion'''
            veces=veces+1

        '''Entra en un último ciclo para guardar los pixeles faltantes necesarios siendo el residuo de la variable cantidad que se había efectuado con anterioridad'''

        for i in range(cantidad):

            '''Agrega los pixeles a la lista'''

            PixelesReservados.append(pixelesdisponibles[espacio,i])

        '''Regresa la lista con los pixeles a ocupar para ocultar la informacion'''
        return PixelesReservados

    def PixelEnBinario(self,ListaPixeles):

        """Funcion que convierte la lista de pixeles a utilizar en binario

        Parámetros

        ListaPixeles Lista obtenida del metodo anterior de los pixeles para realizar la conversion binaria

        """

        '''tamañoLista Guarda el tamaño de la lista'''

        tamañoLista=len(ListaPixeles)

        '''ListaBinaria Guarda su representacion de cada pixel en Binario es decir para Rojo, Azul y Verde tienen su respectiva equivalencia en binario'''
        ListaBinaria=[]

        '''Entra en un ciclo para poder realizar su conversion binaria'''

        for i in range(tamañoLista):
            '''Itera en cada espacio de la tripleta del pixel es decir Rojo,Verde y Azul'''
            for j in range(3):

                '''Accede a cada elemento de la tripleta para realizar su conversion binaria'''
                NumeroBinario=bin(ListaPixeles[i][j])[2:].zfill(8)
                '''Una vez realizada la conversion lo agrega a ListaBinaria'''
                ListaBinaria.append(NumeroBinario)
        '''Regresa la lista con la conversion realizada de todos los pixeles'''
        return ListaBinaria

    def AnchoRequerido(self,cantidad,largo):
        """Funcion que obtiene el ancho necesitado para guardar los pixeles en la lista para una funcion que se ocupará más adelante"""
        global ancho
        ancho=0
        '''Entra en un ciclo evaluando que la cantidad sea menor a largo en caso contrario realiza lo siguiente'''
        while cantidad > largo:

            '''Obtiene la diferencia de cantidad y largo'''

            cantidad=cantidad-largo

            '''Aumenta en uno el ancho necesitado'''

            ancho=ancho+1

            '''Regresa el ancho requerido'''


        '''Almacena el total de ancho a usar'''

        return ancho

    def PixelDecimal(self,Lista):
        """Funcion que convierte la lista Binaria en Decimal

        Parámetros

        Lista Recupera la Lista Binaria con el método LSB ya aplicado

        """

        '''longitud Obtiene el numero de elementos que tiene la lista'''

        longitud=len(Lista)

        '''RGBModificado es una lista que guardará el valor modificado de cada pixel'''

        RGBModificado=[]

        '''Inicia un ciclo para poder acceder a los elementos de la lista'''

        for i in range(longitud):

            '''Realiza la conversion binaria a decimal'''

            valorRGB=int(Lista[i],2)

            '''Agrega el valor decimal de color RGB obtenido a la lista'''

            RGBModificado.append(valorRGB)

        '''Regresa la lista RGB con la modificacion y su conversion a decimal listo para realizar los últimos pasos ocultar el texto en la imagen'''
        return RGBModificado


