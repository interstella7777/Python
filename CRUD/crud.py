from tkinter import * #import libraries
from tkinter import messagebox
import sqlite3

#---------- Funciones - Functions ----------------------
def conexionBBDD():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))       
            ''')
        
        messagebox.showinfo("Conectar", "Conexión realizada con éxito")
    except:
        messagebox.showwarning("Alerta", "La Base de datos ya existe!")

def salirAplicacion():  #Funcion
    valor=messagebox.askquestion("Salir", "Desea Salir de la Aplicacion?")
    if valor == "yes":
        root.destroy()

#------- Funcion limpiar campos - Clean fields --------
def LimpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)


#------- Funcion limpiar campos - Clean fields --------
def borrar_campos():
    cuadroID.delete(0, END)
    cuadroNombre.delete(0, END)
    cuadroPass.delete(0, END)
    cuadroApellido.delete(0, END)
    cuadroDireccion.delete(0, END)
    textoComentario.delete("1.0", END)

#------- Funcion crear registro en base de datos - Create --------
def crear():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get() +
        "','"+ miPass.get() +
        "','"+ miApellido.get() +
        "','"+ miDireccion.get() + 
        "','"+ textoComentario.get("1.0", END) +  "')")
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Insertado con Exito!")


#------- Funcion leer registro de base de datos - Read --------
def leer():
    messagebox.showinfo("CRUD", "Función Leer ejecutada")

#------- Funcion actualizar registro de base de datos - Update --------
def actualizar():
    messagebox.showinfo("CRUD", "Función Actualizar ejecutada")

#------- Funcion borrar registro de base de datos - Erase --------
def borrar():
    messagebox.showinfo("CRUD", "Función Borrar ejecutada")

#------- Funcion para mostrar mensaje - Show a message --------
def licencia():
    messagebox.showinfo("Licencia", "Producto con fines educativos. Basic CRUD app created by Samir Vivas | 2025 | bryansamir@gmail.com")

def acerca_de():
    messagebox.showinfo("Acerca de", "Ejemplo de aplicación con Tkinter y SQLite3")

# ---------- Ventana principal - Main window----------------------
root = Tk()
root.title("Aplicación CRUD con Tkinter")
root.geometry("400x400")
root.config(width=400, height=400)

# ---------- Menú ----------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=400, height=400)

# Menú BBDD
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

# Menú Borrar - Erase
borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrar_campos)
borrarMenu.add_command(label="Limpiar campos", command=LimpiarCampos)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)



# Menú CRUD
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=borrar)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

# Menú Ayuda - Help
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=licencia)
ayudaMenu.add_command(label="Acerca de…", command=acerca_de)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------- Comienzo de campos - Entry ----------------------
miFrame = Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

# Campo ID - Entry ID
cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

# Campo Nombre - Field Name
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

# Campo Contraseña - Field Password
cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

# Campo Apellido - Field Surname
cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

# Campo Dirección - Field Address
cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# Campo Comentarios - Field Comments
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

# Scrollbar para comentarios
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# ------- Aqui comienza los Label - Labels----------------------
idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# -------- Aqui van los Botones - Buttons----------------------
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


# -------- Loop principal - Main Loop ----------------------
root.mainloop()

#Basic CRUD app created by Samir Vivas | 2025 | bryansamir@gmail.com
