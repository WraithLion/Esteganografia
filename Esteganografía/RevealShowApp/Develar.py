from Imagen import Imagen
from Mensaje import Mensaje
class Develar:

    def develar(self):

        imagen= Imagen()

        datosImagen=imagen.cargarimagen()

        dimensiones=imagen.obtenerdimensiones(datosImagen)

        ancho=imagen.obtenerancho(dimensiones)

        largo=imagen.obtenerlargo(dimensiones)

        Pixeles=imagen.obtenerpixeles(datosImagen)

        Lista=imagen.PixelesNecesarios(960,Pixeles,largo)

        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        mensaje=Mensaje()

        BytesExtraidos=mensaje.extraerBit(ListaRGBBinaria)

        BytesExtraidos=mensaje.BinarioAdecimal(BytesExtraidos)

        BytesExtraidos=mensaje.ConvertirEnChar(BytesExtraidos)


        textoDescifrado=mensaje.EscribirMensaje(BytesExtraidos)


