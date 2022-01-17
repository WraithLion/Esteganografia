# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

# En esta parte importamos Imagen y Mensaje
from Imagen import Imagen
from Mensaje import Mensaje

#Definimos la clase ocultamiento que nos servirá para obtener la información oculta en una imagen
class Develar:

    #Definimos el método develar
    def develar(self):

        #Llamamos a la función Imagen y lo almacenamos en la variable imagen
        imagen= Imagen()

        #Se almacena la dirección de la imagen en datosImagen
        datosImagen=imagen.cargarimagen()

        #Obtenemos el tamaño de la imagen
        dimensiones=imagen.obtenerdimensiones(datosImagen)

        #Guardamos el ancho de la imagen
        ancho=imagen.obtenerancho(dimensiones)

        #Guardamos el largo de la imagen
        largo=imagen.obtenerlargo(dimensiones)
        
        #Obtiene los valores de los pixeles encontrados en datosImagen
        Pixeles=imagen.obtenerpixeles(datosImagen)

        #Llamamos a PixelesNecesarios y recoje el resultado en Lista
        Lista=imagen.PixelesNecesarios(960,Pixeles,largo)

        #Transforma la información contenida en Lista a binario
        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        #Imprime el mensaje de Lista a binario
        print(ListaRGBBinaria)
        
        #Imprime la longitud del mensaje de Lista a binario
        print(len(ListaRGBBinaria))

        #Llamamos a la función Mensaje y lo almacenamos en la variable mensaje
        mensaje=Mensaje()

        #Obtenemos el mensaje oculto en la imagen por cada canal en formato binario
        BytesExtraidos=mensaje.extraerBit(ListaRGBBinaria)

        #Convertimos la información a decimal
        print(BytesExtraidos)
        BytesExtraidos=mensaje.BinarioAdecimal(BytesExtraidos)

        #Traducimos los números decimales a código ASCII
        print(BytesExtraidos)
        BytesExtraidos=mensaje.ConvertirEnChar(BytesExtraidos)

        #Se imprime el mensaje en pantalla y se almacenará a petición del usuario con formato .txt
        print(BytesExtraidos)
        textoDescifrado=mensaje.EscribirMensaje(BytesExtraidos)
        
