import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random, string
from tkinter import *
from datetime import timedelta
from datetime import datetime

# Zona de Funciones

def generar_captcha():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def open_registrar():
    window2.withdraw()
    registro.deiconify()
    titulo_registro.delete(0, tk.END)
    autor_registro.delete(0, tk.END)
    publicacion_registro.delete(0, tk.END)
    genero_registro.delete(0, tk.END)
    combo_box.set("Selecciona una opción")


def volver(ventana):
    global tabla
    global tabla2
    tabla.delete(*tabla.get_children())
    tabla2.delete(*tabla2.get_children())
    ventana.withdraw()
    window2.deiconify()

def registrar_libro():
    opcion = combo_box.get()
    titulo = titulo_registro.get()
    autor = autor_registro.get()
    publicacion = publicacion_registro.get()
    genero = genero_registro.get()
    global Libros
    Libros[titulo] = {'Autor': autor, 'Año de publicación': publicacion, 'Genero': genero, 'Disponibilidad': opcion, 'Cliente': 'Sin cliente', 'fechad': 'Sin reserva'}
    messagebox.showinfo("Registro de Libros", "Libro registrado exitosamente!")
    terminar = messagebox.askquestion("Volver al menú", "Deseas salir al menú de opciones?")
    if terminar == "yes":
        registro.withdraw()
        window2.deiconify()
    else:
        titulo_registro.delete(0, tk.END)
        autor_registro.delete(0, tk.END)
        publicacion_registro.delete(0, tk.END)
        genero_registro.delete(0, tk.END)
        combo_box.set("Selecciona una opción")

def open_prestar():
    window2.withdraw()
    prestado.deiconify()
    global tabla
    global Libros
    L = list(Libros)
    for x in range(0, len(L)):
        A = [Libros[L[x]]['Autor']]
        B = [Libros[L[x]]['Año de publicación']]
        C = [Libros[L[x]]['Genero']]
        D = [Libros[L[x]]['Disponibilidad']]
        tabla.insert("", END, text=L[x], values=(A, B, C, D))
        
    

def prestar_libro():
    global fechad
    global tabla
    global Libros
    cliente = quien_entrada.get()
    prestado_titulo = prestado_entrada.get()
    Libros[prestado_titulo]['Disponibilidad'] = "No Disponible"
    Libros[prestado_titulo]['Cliente'] = cliente
    Libros[prestado_titulo]['fechad'] = fechad
    messagebox.showinfo("Prestado de Libros", "Libro prestado exitosamente!")
    terminar2 = messagebox.askquestion("Volver al menú", "Deseas salir al menú de opciones?")
    tabla.delete(*tabla.get_children())
    if terminar2 == "yes":
        prestado.withdraw()
        window2.deiconify()
    else:
        prestado_entrada.delete(0, tk.END)
        open_prestar()

    
    

def open_devolver():
    window2.withdraw()
    devolver.deiconify()
    global tabla2
    global Libros
    L2 = list(Libros)
    for x2 in range(0, len(L2)):
        A2 = [Libros[L2[x2]]['Autor']]
        B2 = [Libros[L2[x2]]['Año de publicación']]
        C2 = [Libros[L2[x2]]['Genero']]
        D2 = [Libros[L2[x2]]['Disponibilidad']]
        E2 = [Libros[L2[x2]]['Cliente']]
        F2 = [Libros[L2[x2]]['fechad']]
        tabla2.insert("", END, text=L2[x2], values=(A2, B2, C2, D2, E2, F2))

def devolver_libro():
    global tabla2
    global Libros
    devolver_titulo = devolver_entrada.get()
    Libros[devolver_titulo]['Disponibilidad'] = "Disponible"
    Libros[devolver_titulo]['Cliente'] = "Sin cliente"
    Libros[devolver_titulo]['fechad'] = "Sin reserva/Devuelto"
    messagebox.showinfo("Devolución de Libros", "Libro devuelto exitosamente!")
    terminar3 = messagebox.askquestion("Volver al menú", "Deseas salir al menú de opciones?")
    tabla2.delete(*tabla2.get_children())
    if terminar3 == "yes":
        devolver.withdraw()
        window2.deiconify()
    else:
        devolver_entrada.delete(0, tk.END)
        open_devolver()

     

def close():
    cerrar = messagebox.askquestion("Cerrar cesión", "Estas seguro de cerrar sesión?")
    if cerrar == "yes":
        window2.withdraw()
        window.deiconify()
    

def verify(usuarios, contrasenas, usuario, contrasena, capy):
    if usuario in usuarios and contrasena in contrasenas:
        if usuario == usuarios[0] and contrasena == contrasenas[0] or usuario == usuarios[1] and contrasena == contrasenas[1] or usuario == usuarios[2] and contrasena == contrasenas[2]:
            if cap_r == capy:
                messagebox.showinfo("Inicio de Sesion", "Credenciales correctas!")
                window.withdraw()
                window2.deiconify()
                captcha.config(text=generar_captcha())
                user_entrada.delete(0, tk.END)
                contrasena_entrada.delete(0, tk.END)
                captcha_entrada.delete(0, tk.END)
            else:
                messagebox.showerror("Inicio de Sesion", "Credenciales incorrectas!")
                captcha.config(text=generar_captcha())
                user_entrada.delete(0, tk.END)
                contrasena_entrada.delete(0, tk.END)
                captcha_entrada.delete(0, tk.END)
        else:

            messagebox.showerror("Inicio de Sesion", "Credenciales incorrectas!")
            captcha.config(text=generar_captcha())
            user_entrada.delete(0, tk.END)
            contrasena_entrada.delete(0, tk.END)
            captcha_entrada.delete(0, tk.END)
    else:
        messagebox.showerror("Inicio de Sesion", "Credenciales incorrectas!")
        captcha.config(text=generar_captcha())
        user_entrada.delete(0, tk.END)
        contrasena_entrada.delete(0, tk.END)
        captcha_entrada.delete(0, tk.END)

#Zona del Codigo sin funciones

usuarios = ['Quintero', "Steiner", "Llanos"]
contrasenas = ['1234', "mosquera", "n1"]

Libros = {}
window = tk.Tk()
window.title("Inicio de sesión")
window.configure(background='#FB12A2')
window.geometry("500x300")
label_user = tk.Label(window, text="Ingresa el nombre del bibliotecario:", bg='#FB12A2')
user_entrada = tk.Entry(window)
label_con = tk.Label(window, text="Ingresa el contraseña del bibliotecario:", bg='#FB12A2')
contrasena_entrada = tk.Entry(window, show="*")
cap_r = generar_captcha()
captcha = tk.Label(window, text=cap_r, font=("monospace", 25), bg='#FB12A2')
captcha_entrada = tk.Entry(window)
enviar = ttk.Button(text="Iniciar", command=lambda:verify(usuarios, contrasenas, user_entrada.get(), contrasena_entrada.get(), captcha_entrada.get()))
label_user.pack(pady= 10)
user_entrada.pack(pady=5, padx=20)
label_con.pack(pady= 10)
contrasena_entrada.pack(pady=5, padx=20)
captcha.pack(pady=10)
captcha_entrada.pack(pady=5, padx=20)
enviar.pack(pady=10)

window2 = tk.Tk()
window2.title("Menú Principal")
window2.geometry("500x300")
window2.configure(background='#FB12A2')
menu_label = tk.Label(window2, text="Bienvenido al MENÚ", font=("Comic Sans MS", 20, "bold"), bg='#FB12A2')
menu_label.pack(pady=5, padx=5)
registro = tk.Button(window2, text="Registrar Un Libro", command=open_registrar).pack(pady=10, padx=10)
prestamo = tk.Button(window2, text="Prestar Un Libro", command=open_prestar).pack(pady=10, padx=10)
devolucion = tk.Button(window2, text="Devolver Un Libro", command=open_devolver).pack(pady=10, padx=10)
close = tk.Button(window2, text="Cerrar Cesión", command=close).pack(pady=15, padx=10)
window2.withdraw()

registro = tk.Tk()
registro.title("Registro de Libros")
registro.geometry("500x500")
registro.configure(background='#FB12A2')
registro.withdraw()

titulo_label = tk.Label(registro, text="Titulo:", bg='#FB12A2').pack(pady=5, padx=10)
titulo_registro = tk.Entry(registro)
titulo_registro.pack(pady=10, padx=10)
autor_label = tk.Label(registro, text="Autor:", bg='#FB12A2').pack(pady=5, padx=10)
autor_registro = tk.Entry(registro)
autor_registro.pack(pady=10, padx=10)
publicacion_label = tk.Label(registro, text="Año de publicación:", bg='#FB12A2').pack(pady=5, padx=10)
publicacion_registro = tk.Entry(registro)
publicacion_registro.pack(pady=10, padx=10)
genero_label = tk.Label(registro, text="Género:", bg='#FB12A2').pack(pady=5, padx=10)
genero_registro = tk.Entry(registro)
genero_registro.pack(pady=10, padx=10)
disponible_label = tk.Label(registro, text="Disponibilidad:", bg='#FB12A2').pack(pady=5, padx=10)
opciones = ['Disponible', 'No Disponible']
combo_box = ttk.Combobox(registro, values=opciones, state="readonly")
combo_box.pack(pady = 10)
combo_box.set("Selecciona una opción")
boton_enviar = tk.Button(registro, text="Registrar", command=registrar_libro).pack(pady=10, padx=10)
registro_volver = tk.Button(registro, text="Volver", command=lambda: volver(registro)).pack(pady=10, padx=10)
prestado = tk.Tk()
prestado.title("Prestado de Libros")
prestado.geometry("600x600")
prestado.withdraw()
prestado.configure(background='#FB12A2')
tabla = ttk.Treeview(prestado, columns=("col1", "col2", "col3", "col4"))
tabla.column("#0", width=100)
tabla.column("col1", width=100)
tabla.column("col2", width=120)
tabla.column("col3", width=100)
tabla.column("col4", width=100)
tabla.heading("#0", text="Titulo", anchor=CENTER)
tabla.heading("col1", text="Autor", anchor=CENTER)
tabla.heading("col2", text="Año de publicación", anchor=CENTER)
tabla.heading("col3", text="Género", anchor=CENTER)
tabla.heading("col4", text="Disponibilidad", anchor=CENTER)
style2 = ttk.Style(prestado)
style2.theme_use("clam")
style2.configure("Treeview.Heading", background="#FA82B4", foreground="white")
tabla.pack()

quien_prestar = tk.Label(prestado, text="Nombre de la persona que desea prestarlo:", bg='#FB12A2').pack(pady=5)
quien_entrada = tk.Entry(prestado)
quien_entrada.pack(pady=10, padx=10)

nombre_prestar = tk.Label(prestado, text="Nombre del libro que desea prestar:", bg='#FB12A2').pack(pady=5)
prestado_entrada =tk.Entry(prestado)
prestado_entrada.pack(pady=10, padx=10)

fecha = datetime.now()
fechaentrega = fecha + timedelta(days=5)
format = fecha.strftime('%d del %m de %Y')
label_fecha = tk.Label(prestado, text='Dia actual: '+format, bg='#FA82B4')
label_fecha.pack()
format = fechaentrega.strftime('%d del %m de %Y')
label_fechaentrega = tk.Label(prestado, text='Fecha de entrega del libro: '+format, bg= '#FA82B4')
label_fechaentrega.pack()
fechad = format

prestado_boton = tk.Button(prestado, text="Pedir Prestado", command=prestar_libro)
prestado_boton.pack(pady= 5, padx=10)
prestado_volver = tk.Button(prestado, text="Volver", command=lambda: volver(prestado))
prestado_volver.pack(pady=10, padx=10)

devolver = tk.Tk()
devolver.title("Devoluciòn de Libros")
devolver.geometry("750x600")
devolver.withdraw()
devolver.configure(background='#FB12A2')
tabla2 = ttk.Treeview(devolver, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
tabla2.column("#0", width=100)
tabla2.column("col1", width=100)
tabla2.column("col2", width=120)
tabla2.column("col3", width=100)
tabla2.column("col4", width=100)
tabla2.column("col5", width=110)
tabla2.column("col6", width=170)
tabla2.heading("#0", text="Titulo", anchor=CENTER)
tabla2.heading("col1", text="Autor", anchor=CENTER)
tabla2.heading("col2", text="Año de publicación", anchor=CENTER)
tabla2.heading("col3", text="Género", anchor=CENTER)
tabla2.heading("col4", text="Disponibilidad", anchor=CENTER)
tabla2.heading("col5", text="En posesión de", anchor=CENTER)
tabla2.heading("col6", text="Fecha de devolución", anchor=CENTER)
style = ttk.Style(devolver)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#FA82B4", foreground="white")
tabla2.pack()

nombre_devolver = tk.Label(devolver, text="Nombre del libro que vas a devolver:", bg='#FB12A2').pack(pady=5)
devolver_entrada =tk.Entry(devolver)
devolver_entrada.pack(pady=10, padx=10)
devolver_boton = tk.Button(devolver, text="Devolver", command=devolver_libro)
devolver_boton.pack(pady= 5, padx=10)

devolver_volver = tk.Button(devolver, text="Volver", command=lambda: volver(devolver))
devolver_volver.pack(pady=10, padx=10)

devolver.mainloop()

prestado.mainloop()

registro.mainloop()


window2.mainloop()

window.mainloop()
