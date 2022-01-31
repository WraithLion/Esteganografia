# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz
from Imagen import Imagen
#Importa la clase Imagen para ocultar el texto en la imagen
from tkinter import filedialog
#Importa tkinter una biblioteca gráfica que permite implementar una interfaz gráfica
from tkinter import messagebox
#Importa de la misma biblioteca una seccion que permite enviar cuadros de mensajes
from Mensaje import Mensaje
#Importa la clase Mensaje para cargar el texto a ocultar en la imagen

class Ocultamiento:

    def ocultar(self):
        '''Crea y asigna una variable de tipo Mensaje'''
        mensaje=Mensaje()

        '''Inicia la carga del archivo'''

        texto=mensaje.abrirarchivo()

        '''Regresa una lista con el mensaje separado por letras'''

        lista=mensaje.obtenerletraporletra(texto)

        '''Obtiene el tamaño de pixeles necesarios'''

        tamaño= int(len(lista)/3)

        '''Crea y asigna a una variable de tipo Imagen'''

        imagen= Imagen()

        '''Obtiene los datos de la imagen'''

        datosImagen=imagen.cargarimagen()

        '''Obtiene las dimensiones de la imagen'''

        dimensiones=imagen.obtenerdimensiones(datosImagen)

        '''Obtiene el ancho de la imagen'''

        ancho=imagen.obtenerancho(dimensiones)

        '''Obtiene el largo de la imagen'''

        largo=imagen.obtenerlargo(dimensiones)

        '''Obtiene los pixeles de la imagen'''

        Pixeles=imagen.obtenerpixeles(datosImagen)

        '''En una lista obtiene los pixeles necesarios para ocultar el texto'''

        Lista= imagen.PixelesNecesarios(tamaño,Pixeles,largo)

        '''Convierte la lista anterior en forma Binaria'''

        ListaRGBBinaria=imagen.PixelEnBinario(Lista)

        '''Obtiene cuantos pixeles de ancho se necesitan para poder guardar el texto'''

        AnchoNecesitado=imagen.AnchoRequerido(tamaño,largo)

        '''Obtiene el tamaño de la lista RGB en binario'''

        longitud=len(ListaRGBBinaria)

        '''Almacenará el byte con la modificacion del ultimo bit'''

        Nuevo=[]

        for i in range(longitud):

            '''Modifica el último bite para poder guardar la informacion'''

            bytemodificado=ListaRGBBinaria[i][:-1]+str(lista[i])

            '''Guarda el elemento modificado en la nueva lista'''

            Nuevo.append(bytemodificado)

        '''Convierte la lista binaria RGB a decimal'''

        ListaModificadaRGB=imagen.PixelDecimal(Nuevo)

        '''Auxiliar que sirve si alcanza al ancho necesario'''# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz


        contador=0

        '''Indica los elementos faltantes de modificar'''

        limite=0

        '''Obtiene el tamaño de la lista RGB'''

        LongitudRGB=len(Lista)

        '''Se crean Tres listas para almacenar el respectivo color para despues modificar el Pixel'''

        ListaRoja=[]

        ListaVerde=[]

        ListaAzul=[]

        limite=tamaño

        while limite>largo:
            limite=limite-largo
        while contador < AnchoNecesitado+1:
            if tamaño>largo:
                tamaño=largo
            if contador==AnchoNecesitado:
                tamaño=limite
            for i in range(0,longitud,3):
                '''Agrega el elemento al color Rojo'''
                ListaRoja.append(ListaModificadaRGB[i])

            for i in range(1,longitud,3):
                '''Agrega el elemento al color Verde'''
                ListaVerde.append(ListaModificadaRGB[i])

            for i in range(2,longitud,3):
                '''Agrega el elemento al color Azul'''
                ListaAzul.append(ListaModificadaRGB[i])

            for i in range(tamaño):
                '''Modifica los Pixeles con los valores de las tres listas en su respectiva posicion'''
                Pixeles[contador,i]=(ListaRoja[i],ListaVerde[i],ListaAzul[i])
            contador=contador+1

        global guardarImagen

        '''Variable que guardará la imagen'''

        guardarImagen=None

        while guardarImagen is None:
            try:

                '''Se le solicitará al usuario que escoja el lugar y nombre para su nueva imagen con la modificacion'''

                guardarImagen = filedialog.asksaveasfilename(defaultextension='.png',filetypes = [("Formato png", ".png")],title="¿Dónde te gustaria guardar la imagen?")
            except:
                '''En caso contrario envía un mensaje indicando que es necesario realizar el guardado'''

                messagebox.showinfo(message="Debes guardar la imagen", title="Aviso")

                '''Continua solicitando hasta que el usuario brinde la informacion solicitada para guardar el archivo'''

                guardarImagen = filedialog.asksaveasfilename(defaultextension='.png',filetypes = [("Formato png", ".png")],title="¿Dónde te gustaria guardar la imagen?")
                pass

            '''Guarda la imagen en la ruta especificada por el usuario'''
            datosImagen.save(guardarImagen)



        return Pixeles

