# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz
from tkinter import filedialog
#Importa tkinter una biblioteca gráfica que permite implementar una interfaz gráfica
from tkinter import messagebox
#Importa de la misma biblioteca una seccion que permite enviar cuadros de mensajes
"""Clase Mensaje para leer un archivo de texto, modificarlo a manera de que interactue la imagen y se efectué el proceso de ocultamiento o develado"""
class Mensaje:

    def abrirarchivo(self):
        '''Funcion que carga el archivo de texto a utilizar para ocultar'''
        '''mensaje guarda el texto del archivo'''
        global mensaje
        '''rutaTexto es la variable que guarda la direccion en la que se encuentra el archivo para ello se usa una interfaz gráfica que le permite escoger un archivo de texto'''
        rutaTexto = filedialog.askopenfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="Selecciona el archivo de texto que deseas utilizar")
        '''Evalua si la variable tiene la direccion'''
        if  len(rutaTexto)==0:
            '''En caso contrario envía un aviso y le vuelve a mostrar la interfaz para que escoja de nuevo el archivo'''
            messagebox.showinfo(message="Debes seleccionar un archivo de texto", title="Aviso")
            '''Vuelve a llamar el método'''
            self.abrirarchivo()
        else:
            '''Si obtiene la ruta del archivo entonces empieza a leer'''
            texto= open (rutaTexto)
            '''Lee todo el contenido del archivo de texto'''
            mensaje = texto.read()
            '''Cierra la lectura de archivo'''
            texto.close()
        '''Devuelve el contenido del archivo'''
        return mensaje




    def obtenerletraporletra(self,mensaje):
        '''Funcion que separa las palabras en letras y obtiene su conversion binaria'''
        self.mensaje=mensaje
        '''ListaBinaria guardará las letras en su forma binaria'''
        ListaBinaria=[]
        '''Itera sobre cada caracter del mensaje'''
        for char in mensaje:
            '''Asigna cada letra como elemento de una misma lista'''
            listaletras=list(mensaje)
            '''Obtiene el número de elementos que constituye la lista'''
            tamaño= len(listaletras)

        '''Inicia su iteracion para poder realizar la conversion binaria de cada letra'''
        for x in range(tamaño):

            '''Obtiene su representacion en código ASCII del elemento de la lista'''

            letraASCII=ord(listaletras[x])

            '''Se procede realizar su conversion decimal a binario'''

            LetraBinaria=bin(letraASCII)[2:].zfill(8)

            '''Agrega cada bit como elemento de la ListaBinaria'''

            ListaBinaria.extend(LetraBinaria)

        '''Obtiene el número de bits que contiene la lista'''

        tamaño=len(ListaBinaria)

        '''Se verifica que la cantidad sea un multiplo de 3 esto con motivo de facilitar el número de pixeles a ocupar para la imagen'''

        while len(ListaBinaria) % 3 !=0:
            '''En caso de que no sea múltipĺo se le agrega un cero al elemento siendo un bit'''
            ListaBinaria.extend('0')
        '''Devuelve la lista con los ajustes realizados'''
        return ListaBinaria

    def extraerBit(self,ListaRGB):
        """Funcion que permite descifrar el contenido de una imagen mediante los pixeles

        Parámetros

        ListaRGB Siendo la lista que se obtiene de la imagen para poder realizar los respectivos procedimientos de develado

        """
        '''byte constituye ocho bits para obtener su representacion en ASCII'''
        byte=""

        '''Lista que almacena los bits extraídos de cada byte de los colores RGB'''

        ListaBitsExtraidos=[]

        '''Obtiene la dimension de la lista'''

        longitud=len(ListaRGB)


        '''Realiza una iteracion para extraer el ultimo bit de cada byte para cada tripleta de su respectivo pixel'''

        for i in range(longitud):
            '''Extrae el ultimo bit del byte siendo el menos significativo (LSB)'''
            bitExtraido=ListaRGB[i][7]

            '''Concatena el bit a la variable byte'''

            byte=byte+str(bitExtraido)

            '''Verifica que haya alcanzado los bits necesarios para conformar el byte'''

            if len(byte)%8==0:

                '''Si se cumple agrega el byte a la lista'''

                ListaBitsExtraidos.append(byte)

                '''Inicializa la variable para repetir el procedimiento'''
                byte=""
        '''Devuelve la lista de bytes'''
        return ListaBitsExtraidos

    def BinarioAdecimal(self,ListaBinaria):

        """Funcion que convierte su expresion binaria a decimal es decir en código ASCII"""

        '''Obtiene la dimension de la lista'''

        longitud=len(ListaBinaria)

        '''Itera el tamaño de la lista para poder realizar la conversion'''

        for i in range(longitud):

            '''Obtiene su representacion binaria en ASCII'''

            NumeroASCII=int(ListaBinaria[i],2)

            '''Sustituye su representacion binaria por ASCII'''

            ListaBinaria[i]=NumeroASCII

        '''Regresa la lista con la conversion hecha'''

        return ListaBinaria

    def ConvertirEnChar(self,ListaDecimal):
        """Funcion que convierte su forma ASCII en caractér

        Parámetros

        ListaDecimal Representacion en ASCII para obtener su forma en caracter

        """

        '''Obtiene el tamaño de la lista'''
        longitud=len(ListaDecimal)

        '''Itera sobre cada elemento de la lista para poder realizar su conversion en caracter'''

        for i in range(longitud):

            '''Convierte su valor en la letra que representa en ASCII'''

            LetraASCII=chr(ListaDecimal[i])

            '''Sustituye su valor por la letra que lo representa de la lista'''

            ListaDecimal[i]=LetraASCII

        '''Devuelve la lista convertida en caracteres'''

        return ListaDecimal

    def EscribirMensaje(self,ListaChar):

        """Funcion que guarda el mensaje dada la lista de caracteres

        Parámetros

        ListaChar es la que almacena la informacion para poder convertir en mensaje

        """

        '''Obtiene el tamaño de la lista'''

        longitud=len(ListaChar)

        '''texto es el mensaje que se ha de descifrado'''

        texto=""

        '''Itera sobre cada elemento de la lista para unirlo en una sola cadena de texto'''

        for i in range(longitud):

            '''Asigna el elemento de la lista en la variable letra'''

            letra=ListaChar[i]

            '''Concatena la letra al texto a fin de construir el mensaje'''

            texto=texto+letra


        global nombreArchivo
        '''nombreArchivo es el nuevo texto que se guardará y el usuario podrá nombrar'''
        nombreArchivo=None

        '''Entra en un ciclo revisando que se realice el guardado del texto recuperado de la imagen'''

        while nombreArchivo is None:
            try:
                '''Se le solicita el usuario el lugar y nombre que le desee dar al texto'''
                nombreArchivo = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="¿Cómo se llamará el archivo en el que se guardara el mensaje?")
            except:
                '''En caso de ignorar se le enviará un mensaje que debe asignar un nombre y guardar el archivo'''
                messagebox.showinfo(message="Debes nombrar el archivo para guardarlo", title="Aviso")
                '''Vuelve a solicitar el usuario los datos antes mencionados'''
                nombreArchivo = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("Formato txt", ".txt")],title="¿Cómo se llamará el archivo en el que se guardara el mensaje?")
            pass
            '''Una vez que el usuario haya especificado el lugar y nombre del archivo se procede a guardar'''
            Archivo= open(nombreArchivo,"a")
            '''Escribe el texto en el archivo que el usuario ha solicitado'''
            Archivo.write(texto)
            '''Cierra el archivo'''
            Archivo.close()
        '''Regresa el texto recuperado de la imagen'''
        return texto

