# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

# En esta parte importamos Imagen y Mensaje
from Imagen import Imagen
from Mensaje import Mensaje

#Definimos la clase ocultamiento que nos servirá para almacenar información en una imagen
class Ocultamiento:

    #Definimos la clase ocultar
    def ocultar(self):

        #Llamamos a la función Mensaje y lo almacenamos en la variable mensaje
        mensaje=Mensaje()
        
        #Almacenamos la dirección del archivo en donde se almacena el mensaje
        texto=mensaje.abrirarchivo()
        
        #Guardamos la información contenida en texto
        lista=mensaje.obtenerletraporletra(texto)
        
        #Obtenemos la longitud de lista
        tamaño= int(len(lista)/3)

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
        Lista= imagen.PixelesNecesarios(tamaño,Pixeles,largo)

        #Transforma la información contenida en Lista a binario
        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        #Calcula el ancho requerido para almacenar la información
        AnchoNecesitado=imagen.AnchoRequerido(tamaño,largo)

        #Se registra la longitud del mensaje convertido en binario
        longitud=len(ListaRGBBinaria)

        #Se crea una matriz
        Nuevo=[]
    
        #A partir de un ciclo for se almacena el mensaje en binario para cada canal RGB
        for i in range(longitud):
            bytemodificado=ListaRGBBinaria[i][:-1]+str(lista[i])
            Nuevo.append(bytemodificado)

        #Se almacena la matriz de pixeles asociada a la imagen en valores decimales
        ListaModificadaRGB=imagen.PixelDecimal(Nuevo)

        #Se inicializan y declaran las variables contador y limite
        contador=0
        limite=0

        #Se guarda la longitud de Lista
        LongitudRGB=len(Lista)

        #Se crea una matriz asociada para cada canal RGB
        ListaRoja=[]
        ListaVerde=[]
        ListaAzul=[]

        #Con un ciclo while se guarda el mensaje en formato binario en los canales RGB de la imagen para al final guardar la imagen modificada en formato png
        while contador < AnchoNecesitado+1:

            for i in range(0,longitud,3):
                ListaRoja.append(ListaModificadaRGB[i])
            for i in range(1,longitud,3):
                ListaVerde.append(ListaModificadaRGB[i])
            for i in range(2,longitud,3):
                ListaAzul.append(ListaModificadaRGB[i])

            pixel=Pixeles[contador,tamaño]

            for i in range(tamaño):
                Pixeles[contador,i]=(ListaRoja[i],ListaVerde[i],ListaAzul[i])

            contador=contador+1
            
        datosImagen.save("UlthweChanged.png")
        return Pixeles
