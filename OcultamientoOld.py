from Imagen import Imagen
from Mensaje import Mensaje
class Ocultamiento:

    def ocultar(self):
        mensaje=Mensaje()
        texto=mensaje.abrirarchivo()
        lista=mensaje.obtenerletraporletra(texto)
        tamaño= int(len(lista)/3)
        tamaño1= int(len(lista))
        tamañoreal=len(lista)/3
        if tamaño<tamañoreal:
            tamaño=tamaño+1

        imagen= Imagen()
        datosImagen=imagen.cargarimagen()
        dimensiones=imagen.obtenerdimensiones(datosImagen)
        ancho=imagen.obtenerancho(dimensiones)
        largo=imagen.obtenerlargo(dimensiones)
        Pixeles=imagen.obtenerpixeles(datosImagen)
        Lista= imagen.PixelesNecesarios(tamaño,Pixeles,largo)
        print(Lista)
        ListaRGBBinaria=imagen.PixelEnBinario(Lista)
        print()
        print(ListaRGBBinaria)
        AnchoNecesitado=imagen.AnchoRequerido(tamaño,largo)
        longitud=len(ListaRGBBinaria)
        print(len(lista))
        Nuevo=[]
        for i in range(longitud-2):
            bytemodificado=ListaRGBBinaria[i][:-1]+str(lista[i])
            Nuevo.append(bytemodificado)
        ListaModificadaRGB=imagen.PixelDecimal(Nuevo)
        print()
        print(Nuevo)
        print()
        print(ListaModificadaRGB)
        contador=0
        limite=0
        LongitudRGB=len(Lista)
        ListaRoja=[]
        ListaVerde=[]
        ListaAzul=[]

        while contador < AnchoNecesitado+1:
            for i in range(0,longitud-2,3):
                ListaRoja.append(ListaModificadaRGB[i])
            for i in range(1,longitud-2,3):
                ListaVerde.append(ListaModificadaRGB[i])
            for i in range(2,longitud-2,3):
                ListaAzul.append(ListaModificadaRGB[i])
            pixel=Pixeles[contador,tamaño]
            contador=contador+1
        if len(ListaVerde)>len(ListaAzul):
            ListaAzul.append(pixel[2])
        else:
            if len(ListaRoja)>len(ListaVerde):
                ListaVerde.append(pixel[1])
                ListaAzul.append(pixel[2])
        for i in range(tamaño):
            #print("ORIGINAL")
            #print(Pixeles[contador,i])
            Pixeles[contador,i]=(ListaRoja[i],ListaVerde[i],ListaAzul[i])
            #print("MODIFICADO")
            print(Pixeles[contador,i])
        datosImagen.save("UlthweChanged.png")
        #print(ListaModificadaRGB)
        #print(ListaRoja)
        #print(ListaVerde)
        #print(ListaAzul)
        return Pixeles
oculto=Ocultamiento()
algo=oculto.ocultar()
#print(int(Nuevo[0],2))
#ListaRGBBinaria[i][7].replace(ListaRGBBinaria[i][7],lista[j][k])
