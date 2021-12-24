class Mensaje:

    def abrirarchivo(self):

        texto= open ('Apoyo.txt')

        mensaje = texto.read()

        texto.close()

        return mensaje

    def obtenerletraporletra(self,mensaje):

        self.mensaje=mensaje

        ListaBinaria=[]

        for char in mensaje:

            listaletras=list(mensaje)

            tamaño= len(listaletras)

        for x in range(tamaño):

            letraASCII=ord(listaletras[x])

            LetraBinaria=bin(letraASCII)[2:].zfill(8)

            ListaBinaria.extend(LetraBinaria)

        tamaño=len(ListaBinaria)

        while len(ListaBinaria) % 3 !=0:

            ListaBinaria.extend('0')

        return ListaBinaria

    def extraerBit(self,ListaRGB):

        byte=""

        ListaBitsExtraidos=[]

        longitud=len(ListaRGB)

        for i in range(longitud):

            bitExtraido=ListaRGB[i][7]

            byte=byte+str(bitExtraido)

            if len(byte)%8==0:

                ListaBitsExtraidos.append(byte)

                byte=""

        return ListaBitsExtraidos

    def BinarioAdecimal(self,ListaBinaria):

        longitud=len(ListaBinaria)

        for i in range(longitud):

            NumeroASCII=int(ListaBinaria[i],2)

            ListaBinaria[i]=NumeroASCII

        return ListaBinaria

    def ConvertirEnChar(self,ListaDecimal):

        longitud=len(ListaDecimal)

        for i in range(longitud):

            LetraASCII=chr(ListaDecimal[i])

            ListaDecimal[i]=LetraASCII

        return ListaDecimal

    def EscribirMensaje(self,ListaChar):

        longitud=len(ListaChar)

        texto=""

        for i in range(longitud):

            letra=ListaChar[i]

            texto=texto+letra

        print("El texto descifrado es:\n\n\n"+str(texto))


        nombreArchivo= input("\n\n¿Cómo se llamará el archivo en el que se guardara el mensaje?\n\n")

        Archivo= open(nombreArchivo+str(".txt"),"a")

        Archivo.write(texto)

        Archivo.close()

        return texto


#mensaje=Mensaje()
#texto=mensaje.abrirarchivo()
#lista=mensaje.obtenerletraporletra(texto)
#print(lista)
#print(len(lista))
#tamaño= len(lista)*8/3
#print("Número de letras :{}".format(tamaño))
