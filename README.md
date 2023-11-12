
Las pruebas consisten en probar una aplicacion web para reserva de habitaciones.

Reservación

Pasos para en el archivo de pruebas test_shady_meadows_reservation
1. Abrir la url.
2. Hacer click en el boton "Book this room".
3. Hacer click en el campo Firstname y escribir "John". 
4. Hacer click en el campo Lastname y escribir "Smith". 
5. Hacer click en el campo Email y escribir "johnsmith@hotmail.com". 
6. Hacer click en el campo phone y escribir "+123456789". 
7. Hacer click en el boton "Book". 
8. Esperar 5 segundos y cerrar la pagina.

Pasos para en el archivo de pruebas test_shady_meadows_request
1. Hacer click en el campo Name y escribir "John Smith". 
2. Hacer click en el campo Email y escribir "johnsmith@hotmail.com"
3. Hacer click en el campo Phone y escribir "+123456789.
4. Hacer click en el campo Subject y escribir "Hello"
5. Hacer click en el campo Message y escribir "Quiero una habitación con vista al mar, cómoda, con baño en la habitación y cama extragrande, ¿hay servicio a la habitación?"
6. .Hacer click en el boton Submit.
7. Esperar 5 segundos y cerrar la pagina.



# **Verificación e Instalación de Python y Pytest**

Este archivo detalla los pasos para verificar si Python está instalado en el entorno de desarrollo, cómo instalarlo si no lo está, y luego cómo verificar si pytest está instalado y cómo ejecutar pruebas utilizando pytest.

## Verificar la Instalación de Python

Para verificar si Python está instalado, abrir una terminal y ejecutar el siguiente comando:

Abrir terminal en gitbash Ejecutar el comando 'python --version'
Si Python está instalado, este comando mostrará la versión instalada. Si no está instalado, se mostrará un mensaje de error indicando que 'python' no se reconoce como un comando.

#### **_Instalación de Python_**

Si Python no está instalado, siga estos pasos para instalarlo:

Para Windows:

Ir al sitio web oficial de Python: python.org.
Descargar el instalador adecuado para su sistema operativo.
Ejecutar el instalador y seguir las instrucciones en pantalla.
Para macOS:

Puede instalar Python usando Homebrew o descargando el instalador desde el sitio web oficial de Python.

brew install python

Para Linux:

La mayoría de las distribuciones de Linux ya incluyen Python. Puede instalarlo a través del gestor de paquetes de distribución. Por ejemplo, en Ubuntu y Debian:

sudo apt-get update sudo apt-get install python3

## **Verificar la Instalación de Pytest**

Para verificar si pytest está instalado, en la terminal, ejecutar:

pytest --version

Si pytest está instalado, mostrará la versión instalada. Si no está instalado, se mostrará un mensaje de error indicando que 'pytest' no se reconoce como un comando.

Si pytest no está instalado, puede instalarlo usando pip, el gestor de paquetes de Python.

pip install -U pytest

## **Ejecutar Pruebas con Pytest**

Una vez que pytest esté instalado, puede ejecutar sus pruebas de la siguiente manera:

Asegúrese de que está en el directorio donde se encuentran sus pruebas.
Ejecutar el comando: pytest
Esto ejecutará todas las pruebas en el directorio actual y sus subdirectorios.

Recuerde que este es un ejemplo general. Los pasos pueden variar dependiendo de su sistema operativo y su configuración particular.

** Esto debería proporcionar una guía clara para verificar la presencia de Python, instalarlo si es necesario, verificar la presencia de pytest y cómo ejecutar pruebas utilizando pytest una vez que esté instalado.