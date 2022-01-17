# Programa creado y elaborado por Valencia Cruz Jonathan Josué y Leonardo Aguirre Muñoz

# En esta parte importamos Ocultamiento y Develar
from Ocultamiento import Ocultamiento
from Develar import Develar

#Definimos la clase main
def main():
    
    #Llamamos a Ocultamiento y Develar
    oculta=Ocultamiento()
    devela=Develar()
    
    #Se imprime un mensaje en pantalla y sirve como un selector de modalidades a petición del usuario
    opcion=int(input("Bienvenido a RevealShowApp\n\n¿Qué te gustaría hacer?\n\n\n1.-Ocultar texto en una imagen\n\n\n2.- Develar alguna imagen que tenga un mensaje oculto\n\n\n3.-Salir\n\n"))
    
    #Se reedirigirá al usuario a ocultar, develar o salir dependiendo del valor introducido
    if opcion==1:
        oculta.ocultar()
    elif opcion==2:
        devela.develar()
    elif opcion==3:
        print("Gracias por usar nuestra aplicación, vuelve pronto")
    else:
        print("Opción invalida, inténtalo de nuevo")

#Se ejecuta la clase main
main()
