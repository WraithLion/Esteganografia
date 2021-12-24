print("Prueba 1")
textoprueba= open ('Apoyo.txt')
mensaje = textoprueba.read()
print(mensaje)
textoprueba.close()

print ("*** Prueba ***")
datos = []
with open("Apoyo.txt") as fname:
	for lineas in fname:
		datos.extend(lineas.split())
print (datos)
palabras=len(datos)
print("Hay un total de "+str(palabras)+" palabras")
print ("***")
# LA lista en bits
# 3 palabras
# algo mas de
# n= numero de palabras
# m_{n}= numero de letras que contiene la n-palabra
# T= suma total de las letras de todas las palabras
# L= Lista para asignar cada letra a su forma binario en ASCII
# L=8*T
# P= Total de pixeles a ocupar
# P=L/3
# hola
#byte 0101010101
#R 11100011
#G 00111100
#B 01011101



# Ejemplo
# n=3
# m_{1}=4
# m_{2}=3
# m_{3}=2
# T=m_{1}+m_{2}+m_{3}
# T=4+3+2
# T=9
# L=8*9
# L=72
