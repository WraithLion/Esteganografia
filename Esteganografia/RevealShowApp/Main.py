from Ocultamiento import Ocultamiento
from Develar import Develar
from tkinter import filedialog
#Importa tkinter una biblioteca gráfica que permite implementar una interfaz gráfica
from tkinter import messagebox
#Importa de la misma biblioteca una seccion que permite enviar cuadros de mensajes

def menu():
    """Funcion que proyecta un menu para que el usuario pueda escojer una opcion"""
    print("Bienvenido a RevealShowApp\n\n¿Qué te gustaría hacer?\n\n\n1.-Ocultar texto en una imagen\n\n\n2.-Develar alguna imagen que tenga un mensaje oculto\n\n\n3.-Salir\n\n")

def main():
    """Funcion que ejecuta el programa para realizar las funciones de Ocultar y Develar"""

    '''Crea y asigna una variable de tipo Ocultamiento'''

    oculta=Ocultamiento()

    '''Proyecta el menu'''

    menu()
    '''Crea y asigna una variable de tipo Develar'''
    devela=Develar()
    '''Declara una variable para que almacenar la opcion que escoja el usuario'''
    opcion=None

    '''Entra en un ciclo para evaluar la respuesta del usuario'''

    while opcion is None  or opcion <1 or opcion!=3:
        '''Revisa si la respuesta que ingresará el usuario es una de las opciones que muestra en pantalla'''
        try:
            '''El usuario ingresa su respuesta'''
            opcion=int(input())
        except:
            '''Envía un mensaje de aviso si el usuario ingreso una opcion no válida'''
            messagebox.showinfo(message="Debes ingresar un número de las opciones que están en el menú", title="Advertencia")
            pass
        '''Al seleccionar la opcion 1 realiza los procedimientos necesarios para ocultar el texto en una imagen'''
        if opcion==1:
            oculta.ocultar()
            '''Envía un mensaje para notificar que se realizo el ocultamiento'''
            messagebox.showinfo(message="Ocultamiento exitoso")
            '''Le notifica al usuario que regresará al menú principal si desea hacer algo más'''
            messagebox.showinfo(message="Regreando al menú principal", title="Regresando")
            menu()
        elif opcion==2:
            '''Inicia el proceso de develado solicitando al usuario los datos necesarios para su realizacion'''
            devela.develar()
            '''Envía un mensaje que se realizo el procedimiento indicado'''
            messagebox.showinfo(message="Develado exitoso")
            '''Le notifica al usuario que regresará al menú principal si desea hacer algo más'''
            messagebox.showinfo(message="Regreando al menú principal", title="Regresando")
            menu()
        elif opcion==3:
            '''Envía un mensaje de agradecimiento antes de salir de la aplicacion'''
            messagebox.showinfo(message="Gracias por usar nuestra aplicación, vuelve pronto", title="Agradecimiento")
        else:
            '''Le notifica al usuario que debe escoger una opcion de la que se muestra en pantalla'''
            messagebox.showinfo(message="Opción invalida, inténtalo de nuevo")

'''Ejecuta el menú y sus funcionalidades'''
main()
