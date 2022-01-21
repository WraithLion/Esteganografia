# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

#Se realiza la clase Mensaje
class Mensaje:

    #Obtiene el contenido de un archivo .txt
    def abrirarchivo(self, ruta):
        
        #Se abre el archivo .txt
        texto = open(ruta)
        
        #Se lee el contenido de texto
        mensaje = texto.read()

        #Se cierra el archivo
        texto.close()

        #Regresa el contenido del archivo .txt
        return mensaje

    #Regresa la lista de las letras obtenidas en el archivo .txt en formato binario a partir de su código ASCII
    def obtenerletraporletra(self,mensaje):

        #Instanciamos a la clase mensaje
        self.mensaje=mensaje

        #Se crea una matriz para almacenar la información en binario
        ListaBinaria=[]

        #Se realiza una lista de las letras contenidas en mensaje
        for char in mensaje:
            listaletras=list(mensaje)
            tamaño= len(listaletras)

        #Se obtiene el valor binario de cada letra contenida en listaletras a partir de su código ASCII
        for x in range(tamaño):
            letraASCII=ord(listaletras[x])
            LetraBinaria=bin(letraASCII)[2:].zfill(8)
            ListaBinaria.extend(LetraBinaria)

        #Registra la longitud de ListaBinaria en tamaño
        tamaño=len(ListaBinaria)

        #Se le agrega '0' al final de cada elemento contenido en ListaBinaria
        while len(ListaBinaria) % 3 !=0:
            ListaBinaria.extend('0')

        #Regresa ListaBinaria
        return ListaBinaria

    #Regresa un arreglo que contiene los bits que conforman a ListaRGB en cadenas de 8 bits
    def extraerBit(self,ListaRGB):
        
        #Se inicializa una cadena
        byte=""

        #Se declara un arreglo para almacenar los bits en ListaBinaria
        ListaBitsExtraidos=[]

        #Se obtiene la longitud de ListaRGB
        longitud=len(ListaRGB)

        #Agrupa los bits en cadenas de 8
        for i in range(longitud):

            bitExtraido=ListaRGB[i][7]
            byte=byte+str(bitExtraido)

            if len(byte)%8==0:

                ListaBitsExtraidos.append(byte)
                byte=""

        return ListaBitsExtraidos

    #Convierte los valores binarios a decimales dada una lista
    def BinarioAdecimal(self,ListaBinaria):

        #Obtiene la longitud de la lista
        longitud=len(ListaBinaria)

        #Traduce cada cadena de números binarios a números decimales
        for i in range(longitud):

            NumeroASCII=int(ListaBinaria[i],2)
            ListaBinaria[i]=NumeroASCII

        #Regresa la lista de números en formato decimal
        return ListaBinaria

    #Traduce los números decimales a carácteres a partir del código ASCII
    def ConvertirEnChar(self,ListaDecimal):

        #Obtiene la longitud de ListaDecimal
        longitud=len(ListaDecimal)

        #Traduce cada número decimal a carácteres ASCII
        for i in range(longitud):

            LetraASCII=chr(ListaDecimal[i])
            ListaDecimal[i]=LetraASCII

        #Regresa ListaDecimal
        return ListaDecimal

    #Imprime en pantalla el texto develado adjunto a un texto, además de almacenarlo en formato .txt a petición del usuario
    def EscribirMensaje(self,ListaChar):

        #Se almacena la longitud de la lista de carácteres del mensaje develado
        longitud=len(ListaChar)
        
        #Se declara una cadena vacía
        texto=""

        #Adjunta los carácteres de la lista en una cadena de texto
        for i in range(longitud):

            letra=ListaChar[i]
            texto=texto+letra

        #Imprime un mensaje previo al mensaje develado
        print("El texto descifrado es:\n\n\n"+str(texto))

        #Imprime un mensaje para preguntar la forma al que se le nombrará al archivo .txt que almacenará el mensaje develado
        nombreArchivo= input("\n\n¿Cómo se llamará el archivo en el que se guardara el mensaje?\n\n")

        #Se crea el archivo .txt con el nombre dado por el usuario y en el se almacena el texto develado 
        Archivo= open(nombreArchivo+str(".txt"),"a")
        Archivo.write(texto)
        Archivo.close()

        #Regresa texto
        return texto


#mensaje=Mensaje()
#texto=mensaje.abrirarchivo()
#lista=mensaje.obtenerletraporletra(texto)
#print(lista)
#print(len(lista))
#tamaño= len(lista)*8/3
#print("Número de letras :{}".format(tamaño))
