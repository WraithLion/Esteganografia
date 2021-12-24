from Imagen import Imagen

from Mensaje import Mensaje

class Ocultamiento:

    def ocultar(self):

        mensaje=Mensaje()

        texto=mensaje.abrirarchivo()

        lista=mensaje.obtenerletraporletra(texto)

        tamaño= int(len(lista)/3)

        imagen= Imagen()

        datosImagen=imagen.cargarimagen()

        dimensiones=imagen.obtenerdimensiones(datosImagen)

        ancho=imagen.obtenerancho(dimensiones)

        largo=imagen.obtenerlargo(dimensiones)

        Pixeles=imagen.obtenerpixeles(datosImagen)

        Lista= imagen.PixelesNecesarios(tamaño,Pixeles,largo)

        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        AnchoNecesitado=imagen.AnchoRequerido(tamaño,largo)

        longitud=len(ListaRGBBinaria)

        Nuevo=[]

        for i in range(longitud):

            bytemodificado=ListaRGBBinaria[i][:-1]+str(lista[i])

            Nuevo.append(bytemodificado)

        ListaModificadaRGB=imagen.PixelDecimal(Nuevo)

        contador=0

        limite=0

        LongitudRGB=len(Lista)

        ListaRoja=[]

        ListaVerde=[]

        ListaAzul=[]

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

