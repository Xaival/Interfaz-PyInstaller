
# Aviso
Para usarlo es necesario tener instalado pyinstaller. Puedes usar `pip install pyinstaller` para instalarlo.

Para añadir contenido extra (imagenes) es necesario usar `--add-data` el cual aun no esta añadido.

# Interfaz grafica para PyInstaller

![image](https://user-images.githubusercontent.com/54257745/181665000-6c8d2271-e4fb-4255-9be1-d27544c0b4be.png)


## [Página PyInstaller](https://pypi.org/project/pyinstaller/)


## Funcionamiento

El programa utiliza el ejecutable original de PyInstaller por lo que es necesario acompañar al archivo de Python con un ejecutable.

Se podría decir que está haciendo de intérprete para el archivo.


## Carpetas

### Proyecto Python

En esta carpeta se encuentra el archivo python que crea la interfaz y el ejecutable `pyinstaller.exe` para ejecutarlo.

## Partes de la interfaz del programa

### Icono

![image](https://user-images.githubusercontent.com/54257745/164698163-fc6285ab-7f63-43f1-9020-f3a7ef17a48e.png)

Archivo de python que se desea convertir en ejecutable.

`-i` o `--icon=RUTA` Añade un icono personalizado al .exe RUTA es la ubicación de la imagen.ico.

**Generar**

![image](https://user-images.githubusercontent.com/54257745/181665082-f09c7cae-ca4b-495d-b975-08613d8d0f5e.png)

`-D` o `--onedir` (predeterminado) agrupa la salida en una única carpeta.

`-F` o `--onefile` El resultante es un único archivo `.exe`.

![image](https://user-images.githubusercontent.com/54257745/181665254-df66ec38-9eef-455d-a1cc-3926837d48f0.png)

`-c`, `--console` o `--nowindowed` (predeterminado) Abre la terminal al ejecutar (solo válido para Windows).

![image](https://user-images.githubusercontent.com/54257745/181665336-00f92082-07ad-4e59-878f-9f08f0105609.png)

`--add-data` Permite añadir contenido dentro del ejecutable. Imágenes, base de datos o lo que sea.

'--add-data "E:/.../Programa/datos; datos/"' para acceder a estos datos desde el archivo py hay que poner la ruta así 'os.path.dirname(__file__)+"/datos/logo.ico"'. Para esto debe de crearse una carpeta llamada datos en la misma ruta que en la que está el archivo de python.

### Permisos

![image](https://user-images.githubusercontent.com/54257745/164698656-743caca6-016b-4c0c-b26d-096f7801fced.png)

`--uac-admin` Pedir permisos de administrador al ejecutar el exe generado.

`--uac-uiaccess` Permite que el exe administrador funcione con escritorio remoto. Requiere permisos de administrador.

### Extras

![image](https://user-images.githubusercontent.com/54257745/164698734-015d0997-c39d-48a9-b803-9411203ad385.png)

`-K` o `--tk` Incluye la librería TCL / TK durante la implementación.

`--clean` Limpie los archivos temporales y en caché antes de compilar.


