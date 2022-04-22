# Interfaz grafica para PyInstaller

![image](https://user-images.githubusercontent.com/54257745/164465515-703d385c-2a22-4534-9d27-06cd0c8ef253.png)

## [Pagina PyInstaller](https://pypi.org/project/pyinstaller/)


## Funcionamiento

El programa utiliza el ejecutable original de PyInstaller por lo que es necesario acompañar al archivo de Python con un ejecutable.

Se podria decir que esta haciendo de interprete para el archivo.


## Carpetas

### Proyecto Python

En esta carpeta se encuentra el archivo python que crea la interfaz y el ejecutable `pyinstaller.exe` para ejecutarlo.

### Ejecutable

En esta carpeta se encuentra el resultado de convertir en ejecutable el archivo de Python de la carpeta de **Proyecto Python** y copiar manualmente el ejecutable `pyinstaller.exe`.

## Partes de la interfaz del programa

**Icono**

![image](https://user-images.githubusercontent.com/54257745/164698163-fc6285ab-7f63-43f1-9020-f3a7ef17a48e.png)

Archivo de python que se desea convertir en ejecutable.

`-i` o `--icon=RUTA` Añade un icono personalizado al .exe RUTA es la ubicación de la imagen.ico.

**Generar**

![image](https://user-images.githubusercontent.com/54257745/164698361-14db4768-3af0-4f08-a536-683dcd6e5d6a.png)

`-D` o `--onedir` (predeterminado) agrupa la salida en una única carpeta.

`-F` o `--onefile` El resultante es un único archivo `.exe`.

![image](https://user-images.githubusercontent.com/54257745/164698444-a0e78f59-8d88-4dfa-8c5f-6bba08f2418e.png)

`-c`, `--console` o `--nowindowed` (predeterminado) Abre la terminal al ejecutar (solo válido para Windows).

**Permisos**

![image](https://user-images.githubusercontent.com/54257745/164698656-743caca6-016b-4c0c-b26d-096f7801fced.png)

`--uac-admin` Pedir permisos de administrador al ejecutar el exe generado.

`--uac-uiaccess` Permite que el exe administrador funcione con escritorio remoto. Requiere permisos de administrador.

**Extras**

![image](https://user-images.githubusercontent.com/54257745/164698734-015d0997-c39d-48a9-b803-9411203ad385.png)

`-K` o `--tk` Incluye la librería TCL / TK durante la implementación.

`--clean` Limpie los archivos temporales y en cache antes de compilar.


