from Ocultamiento import Ocultamiento
from Develar import Develar
from tkinter import filedialog
from tkinter import messagebox
def main():

    oculta=Ocultamiento()

    devela=Develar()
    opcion=None
    print("Bienvenido a RevealShowApp\n\n¿Qué te gustaría hacer?\n\n\n1.-Ocultar texto en una imagen\n\n\n2.-Develar alguna imagen que tenga un mensaje oculto\n\n\n3.-Salir\n\n")
    while opcion is None or opcion>3 or opcion <1:
        try:
            opcion=int(input())
        except:
            messagebox.showinfo(message="Debes ingresar un número de las opciones que están en el menú", title="Advertencia")
            pass

    if opcion==1:
        oculta.ocultar()
        messagebox.showinfo(message="Ocultamiento exitoso")
    elif opcion==2:
        devela.develar()
        messagebox.showinfo(message="Develado exitoso")
    elif opcion==3:
        messagebox.showinfo(message="Gracias por usar nuestra aplicación, vuelve pronto", title="Agradecimiento")
    else:
        messagebox.showinfo(message="Opción invalida, inténtalo de nuevo")

main()
