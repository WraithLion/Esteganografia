# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz
from Imagen import Imagen
#Importa la clase Imagen
from Mensaje import Mensaje
#Importa la clase Mensaje
"""Clase para mostrar un mensaje dada una imagen"""
class Develar:

    def develar(self):

        '''Crea y asigna una variable de tipo Imagen'''

        imagen= Imagen()

        '''Carga los datos de la imagen'''

        datosImagen=imagen.cargarimagen()

        '''Obtiene el largo y ancho de la imagen'''

        dimensiones=imagen.obtenerdimensiones(datosImagen)

        '''Obtiene el ancho de la imagen'''

        ancho=imagen.obtenerancho(dimensiones)

        '''Obtiene el largo de una imagen'''

        largo=imagen.obtenerlargo(dimensiones)

        '''Obtiene los pixeles de la imagen'''

        Pixeles=imagen.obtenerpixeles(datosImagen)

        '''Obtiene los pixeles necesarios para leer una imagen'''

        Lista=imagen.PixelesNecesarios(1800,Pixeles,largo)

        '''Lista que convierte a su forma binaria'''

        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        '''Crea y asigna una variable de tipo Mensaje'''

        mensaje=Mensaje()

        '''Extrae los ultimos bits de la Lista RGB para construir una lista de bytes'''

        BytesExtraidos=mensaje.extraerBit(ListaRGBBinaria)

        '''Convierte la lista de bytes en una lista decimal'''

        BytesExtraidos=mensaje.BinarioAdecimal(BytesExtraidos)

        '''Convierte los bytes decimales en su forma ASCII caracter'''

        BytesExtraidos=mensaje.ConvertirEnChar(BytesExtraidos)

        '''Construye el texto y lo guarda en un archivo de texto'''


        textoDescifrado=mensaje.EscribirMensaje(BytesExtraidos)


