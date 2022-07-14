# Tkinter para interfaz gráfica
import tkinter as tk
from tkinter import ttk
# Ventanas de diálogo
from tkinter import filedialog # Abrir y guardar un archivo
from tkinter import messagebox # Cuadros de mensaje y alerta
# Manejo de directorios y archivos
import os
from os.path import exists # Comprueba si existe el archivo o directorio
from os.path import basename  # Extrae nombre de una ruta absoluta
from os.path import splitext # Divide en un array el nombre y extensión del archivo
from shutil import rmtree # Mover árbol de directorios o archivos
from tempfile import TemporaryDirectory # Crear carpeta temporal
# Lanzar ejecutable
from subprocess import Popen
# Tiempo de espera
from time import sleep

# Declarar clase
class Ventana(tk.Tk):
    # Inicializar los atributos del objeto
    def __init__(self):
        super().__init__() # Inicializa Tk y la deja accesible desde self

        self.title("Conversor Python a ejecutable") # Título de la ventana
        self.config(padx=10, pady=10) # Poner fondo negro
        self.minsize(width=500, height=300) # Tamaño mínimo de pantalla
        self.geometry(str(500)+"x"+str(300)+"+"+str(self.winfo_screenwidth()//2-500//2)+"+"+str(self.winfo_screenheight()//2-300//2)) # Centra en pantalla
        
        self.create_widgets() # Ejecutar función


    # Crear elementos
    def create_widgets(self):

        # Variables
        self.Entry_A1B1_1 = tk.StringVar()

        self.Entry_A1B1_2 = tk.StringVar()

        self.Checkbutton_C1_1 = tk.BooleanVar(self)
        self.Checkbutton_C1_1.set(True)

        self.Checkbutton_A2_1 = tk.BooleanVar(self)
        self.Checkbutton_A2_1.set(False)

        self.Checkbutton_A2_2 = tk.BooleanVar(self)
        self.Checkbutton_A2_2.set(False)

        self.Checkbutton_B2_1 = tk.BooleanVar(self)
        self.Checkbutton_B2_1.set(False)

        self.Checkbutton_B2_2 = tk.BooleanVar(self)
        self.Checkbutton_B2_2.set(False)


        # Hacer que la tabla de la raíz ocupe todo el espacio disponible
        self.columnconfigure(0, weight=True)
        self.columnconfigure(1, weight=True)
        self.columnconfigure(2, weight=True)
        self.rowconfigure(0,weight=True)
        self.rowconfigure(1,weight=True)


        # A1-B1 _____________________________________________________________________
        Frame_A1B1=tk.Frame(self) # Declarar y configurar
        Frame_A1B1.grid(row="0", column="0", sticky="nsew", padx=10, pady=10, columnspan="2")
        Frame_A1B1.columnconfigure(0, weight=True, pad=20)

        # Ruta del archivo
        tk.Label(Frame_A1B1, text="Ruta del archivo").grid(row="0", column="0", sticky="nw", padx=5, pady=5, columnspan="2")
        ttk.Entry(Frame_A1B1, textvariable=self.Entry_A1B1_1).grid(row="1", column="0", sticky="nsew", padx=5, pady=5)
        ttk.Button(Frame_A1B1, text="...", width=5, command= self.explorador1).grid(row="1", column="1", sticky="nsew", padx=0, pady=5)

        # Icono
        tk.Label(Frame_A1B1, text="Icono").grid(row="2", column="0", sticky="nw", padx=5, pady=5, columnspan="2")
        ttk.Entry(Frame_A1B1, textvariable=self.Entry_A1B1_2).grid(row="3", column="0", sticky="nsew", padx=5, pady=5)
        ttk.Button(Frame_A1B1, text="...", width=5, command= self.explorador2).grid(row="3", column="1", sticky="nsew", padx=0, pady=5)


        # C1 ________________________________________________________________________
        Frame_C1=tk.Frame(self) # Declarar y configurar
        Frame_C1.grid(row="0", column="2", sticky="nsew", padx=10, pady=10)

        # Generar
        tk.Label(Frame_C1, text="Generar").grid(row="0", column="0", sticky="nw", padx=5, pady=5)

        self.Combobox_C1_1=ttk.Combobox(Frame_C1, state="readonly", values=["Carpeta", "Archivo.exe"])
        self.Combobox_C1_1.grid(row="1", column="0", sticky="nsw", padx=5, pady=5)
        self.Combobox_C1_1.current(0) # Definir opción predeterminada

        # Terminal
        ttk.Checkbutton(Frame_C1, text="Con terminal", variable=self.Checkbutton_C1_1).grid(row="2", column="0", sticky="nsw", padx=5, pady=15)


        # A2 ________________________________________________________________________
        Frame_A2=tk.Frame(self) # Declarar y configurar
        Frame_A2.grid(row="1", column="0", sticky="nsew", padx=10, pady=10)

        # Permisos
        tk.Label(Frame_A2, text="Permisos").grid(row="0", column="0", sticky="nw", padx=5, pady=5)
        ttk.Checkbutton(Frame_A2, text="Administrador", variable=self.Checkbutton_A2_1, command= self.permiso1).grid(row="1", column="0", sticky="nsw", padx=5, pady=5)
        ttk.Checkbutton(Frame_A2, text="Escritorio remoto", variable=self.Checkbutton_A2_2, command= self.permiso2).grid(row="2", column="0", sticky="nsw", padx=5, pady=5)


        # B2 ________________________________________________________________________
        Frame_B2=tk.Frame(self) # Declarar y configurar
        Frame_B2.grid(row="1", column="1", sticky="nsew", padx=10, pady=10)

        # Extras
        tk.Label(Frame_B2, text="Extras").grid(row="0", column="0", sticky="nw", padx=5, pady=5)
        ttk.Checkbutton(Frame_B2, text="Importar TCL / TK", variable=self.Checkbutton_B2_1).grid(row="1", column="0", sticky="nsw", padx=5, pady=5)
        ttk.Checkbutton(Frame_B2, text="Limpiar caché", variable=self.Checkbutton_B2_2).grid(row="2", column="0", sticky="nsw", padx=5, pady=5)


        # C2 ________________________________________________________________________
        Frame_C2=tk.Frame(self) # Declarar y configurar
        Frame_C2.grid(row="1", column="2", sticky="nsew", padx=10, pady=10) # Mostrar
        Frame_C2.columnconfigure(0, weight=True)
        Frame_C2.rowconfigure(0,weight=True)

        # Crear
        tk.Button(Frame_C2, text="Crear", padx=20, command=self.ejecutar).grid(row="0", column="0", sticky="se", padx=5, pady=5)
    


    # Buscar archivo de Python
    def explorador1(self):
        # Abrir ventana de explorador de archivos y guardar ruta seleccionada
        self.Entry_A1B1_1.set(filedialog.askopenfilename(title="Archivo Python", filetypes = [("Python", "*.py"), ("Python", "*.pyw")]))
        
    # Buscar icono
    def explorador2(self):
        # Abrir ventana de explorador de archivos y guardar ruta seleccionada
        self.Entry_A1B1_2.set(filedialog.askopenfilename(title="Icono de la extensión", filetypes = [("JPEG Image", "*.jpg"), ("PNG Image", "*.png"),("Cualquiera","*.*")]))



    # Desactivar permiso inferior si está desactivado el de arriba
    def permiso1(self):
        if not self.Checkbutton_A2_1.get(): self.Checkbutton_A2_2.set(False)
        
    # Activar permiso superior si está activado el de abajo
    def permiso2(self):
        if self.Checkbutton_A2_2.get(): self.Checkbutton_A2_1.set(True)



    # Ejecución final
    def ejecutar(self):

        # Comprobar que la ruta se haya escrito la ruta del archivo
        if self.Entry_A1B1_1.get() != "":
            # Comprobar que el archivo es .py o .pyw
            if splitext(basename(self.Entry_A1B1_1.get()))[1] in [".py", ".pyw"]:
                # Comprobar que el archivo exista
                if exists(self.Entry_A1B1_1.get()):
                    
                    # Seleccionar carpeta destino
                    RutaDestino = filedialog.askdirectory(title="Seleccionar carpeta")

                    # Comprobar que se halla especificado una ruta
                    if RutaDestino != "": 
                        # Comprobar que la ruta existe
                        if exists(RutaDestino):
                           # Si ya hay una carpeta o si ya hay un ejecutable que no haya uno creado
                            if not (self.Combobox_C1_1.current() == 0 and exists(RutaDestino+"/"+splitext(basename(self.Entry_A1B1_1.get()))[0]) or self.Combobox_C1_1.current() != 0 and exists(RutaDestino+"/"+splitext(basename(self.Entry_A1B1_1.get()))[0]+".exe")):
                                # Prueba que todo el siguiente código funcione
                                try: 
                                
                                    # Variables para guarda atributos para la ejecución del programa
                                    CodigoEjecucion='pyinstaller.exe'
                                    
                                    # Generar - Comprueba el valor asignado en el desplegable y dependiendo del cual sea se asigna
                                    if self.Combobox_C1_1.current() == 0:
                                        CodigoEjecucion+=" -D" # -D (predeterminado) agrupa la salida en una carpeta.
                                        GeneraCarpeta=True # Guarda variable para saber si el resultado será una carpeta
                                    else:
                                        CodigoEjecucion+=" -F" # -F El resultante es un único archivo `.exe`.
                                        GeneraCarpeta=False # Guarda variable para saber si el resultado será un archivo

                                    # Con terminal - Comprueba si Checkbutton esté seleccionado
                                    # -c (predeterminado) Abre la terminal al ejecutar (únicamente válido para Windows).
                                    if self.Checkbutton_C1_1.get(): CodigoEjecucion+=" -c"
                                    # -w Al abrir el ejecutable no abrirá la terminal (únicamente válido para Windows).
                                    else: CodigoEjecucion+=" -w"

                                    # Permisos - Comprueba si Checkbutton esté seleccionado
                                    # --uac-admin Pedir permisos de administrador al ejecutar el exe generado.
                                    if self.Checkbutton_A2_1.get(): CodigoEjecucion+=" --uac-admin"
                                    # --uac-uiaccess Permite que el exe administrador funcione con escritorio remoto. Requiere permisos de administrador.
                                    if self.Checkbutton_A2_2.get(): CodigoEjecucion+=" --uac-uiaccess"

                                    # Extras - Comprueba si Checkbutton esté seleccionado
                                    # -K Incluye la librería TCL / TK durante la implementación.
                                    if self.Checkbutton_B2_1.get(): CodigoEjecucion+=" -K"
                                    # --clean Limpie los archivos temporales y en caché antes de compilar.
                                    if self.Checkbutton_B2_2.get(): CodigoEjecucion+=" --clean"

                                    # Icono - Comprueba que tenga escrito algo
                                    # -i=RUTA    Añade un icono personalizado al .exe RUTA es la ubicación de la imagen.ico.
                                    if self.Entry_A1B1_2.get() != "": CodigoEjecucion+=" -i="+'"'+self.Entry_A1B1_2.get()+'"'

                                    # Guardar como - Comprobar si el directorio existe y no dejar que sobrescriba nada
                                    # -n NAME Especificar un nombre para la carpeta o el ejecutable.
                                    CodigoEjecucion+=' -n "'+splitext(basename(self.Entry_A1B1_1.get()))[0]+'"'
                                    # Ruta de instalacion temporal
                                    CarpetaTemporal = TemporaryDirectory(prefix="pyinstaller_")
                                    CodigoEjecucion+=" --specpath "+'"'+CarpetaTemporal.name.replace("\\", "/")+'"' # --specpath NAME Archivo de especificaciones
                                    CodigoEjecucion+=" --workpath "+'"'+CarpetaTemporal.name.replace("\\", "/")+'"' # --workpath NAME Datos temporales
                                    # --distpath NAME Ruta del resultado
                                    CodigoEjecucion+=" --distpath "+'"'+RutaDestino+'"'

                                    # Ubicación del archivo (Debe ponerse lo último)
                                    if self.Entry_A1B1_1.get() != "": CodigoEjecucion+=' "'+self.Entry_A1B1_1.get()+'"'

                                    # Lanzar ejecutable de conversor
                                    Popen(CodigoEjecucion, shell=True)

                                    # Esperar a que se cree el contenido
                                    if GeneraCarpeta: # Comprobar cada 1s si está la carpeta resultante
                                        while(not exists(RutaDestino+"/"+splitext(basename(self.Entry_A1B1_1.get()))[0])): sleep(1)
                                    else: # Comprobar cada 1s si está el archivo ejecutable
                                        while(not exists(RutaDestino+"/"+splitext(basename(self.Entry_A1B1_1.get()))[0]+".exe")): sleep(1)

                                    # Borrar carpeta temporal
                                    CarpetaTemporal = None
                                    # Borrar carpeta __pycache__ generada donde está el ejecutable
                                    if exists(os.path.dirname(self.Entry_A1B1_1.get())+'/__pycache__'):
                                        rmtree(os.path.dirname(self.Entry_A1B1_1.get())+'/__pycache__')

                                    # Mensaje de que se ha completado con éxito
                                    messagebox.showinfo(title="Completado", message="El archivo se ha creado correctamente")

        # En caso de que algo de error
                                except: messagebox.showwarning(title="Error", message='Ha habido un error inesperado durante la ejecución')
                            else: messagebox.showinfo(title="Cancelado", message="El archivo que se va a crear ya existe")
                        else: messagebox.showwarning(title="Aviso", message='La ruta especificada no ha sido encontrada')
                else: messagebox.showwarning(title="Aviso", message='El tipo del archivo no es .py ni .pyw')
            else: messagebox.showwarning(title="Aviso", message='La ruta del archivo no existe')
        else: messagebox.showwarning(title="Aviso", message='El campo "Ruta del archivo" es obligatoria')

# Llamar a clase y abrir ventana
Ventana().mainloop()
