# Esteganografia por método LSB

Este programa nos permite ocultar información en imágenes usando el bit menos significativo de cada uno de los pixeles que conforman la imagen,
este cambio es imperceptible para el ojo humano, lo cual es útil para esconder información a vista de agentes terceros.

La aplicación contiene los métodos ocultar y develar los cuales, como su nombres lo indican, permiten almacenar y sustraer información dada una imagen
por medio de esteganografía LSB.

# 1. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Esteganografia adjunto a su contenido.

Posteriormente, se ejecutará el archivo Main.pyw localizado en Esteganografia/, éste archivo se puede ejecutar ya sea dando doble click al archivo, dentro de una terminal
(esto se puede realizar utilizando el comando "python3 Main.pyw", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "Main.pyw" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Con lo anterior realizado, usted verá que se iniciará el programa mostrando en pantalla una interfaz en donde se mostrarán las siguientes opciones:

1. Seleccionar imagen: Esta opción permite seleccionar la imagen a modificar, ya sea para esconder u obtener un mensaje oculto.
2. Ocultar: Una vez seleccionado la imagen del apartado anterior, se le pedirá seleccionar el archivo .txt donde se tendrá el mensaje a ocultar para posteriormente solicitar el nombre y localización donde se almacenará la imagen modificada.
3. Develar: Igualmente se requeríra de Seleccionar imagen, su función es la de obtener el mensaje oculto en una imagen, este mensaje se almacenará en forma de un archivo .txt con el nombre que especifique el usuario

# 2. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Estenografía junto a una somera descripción de los mismos:

Estenografía/

1. README.md: Es el archivo que está leyendo en este momento
2. Proyecto_Aguirre_Leonardo_Valencia_Jonathan.pdf: Se trata de un archivo en formato pdf que explica en mayor profundidad lo realizado en el proyecto

Estenografía/RevealShowApp/

1. Main.py: Es el archivo principal para la ejecución del programa
2. Imagen.py: Se almacenan los métodos necesarios para el procesamiento de imágenes
3. Develar.py: En este archivo se encuentra el procedimiento necesario para obtener el mensaje oculto por estenografía LSB de una imagen
4. Ocultamiento.py: Se guarda la clase que se encarga de ocultar un mensaje en una imagen por medio de estenografía LSB

Estenografía/RevealShowApp/Imágenes: Aquí se guardan imágenes de prueba
Estenografía/RevealShowApp/Texto: Se almacenan textos de prueba
