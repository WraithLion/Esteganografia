from Ocultamiento import Ocultamiento
from Develar import Develar

def main():
    oculta=Ocultamiento()
    devela=Develar()
    opcion=int(input("Bienvenido a RevealShowApp\n\n¿Qué te gustaría hacer?\n\n\n1.-Ocultar texto en una imagen\n\n\n2.- Develar alguna imagen que tenga un mensaje oculto\n\n\n3.-Salir\n\n"))
    if opcion==1:
        oculta.ocultar()
    elif opcion==2:
        devela.develar()
    elif opcion==3:
        print("Gracias por usar nuestra aplicación, vuelve pronto")
    else:
        print("Opción invalida, inténtalo de nuevo")

main()
