import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog

#interfaz
def CrearWidgets():
    etiquetaGuardar = Label(vn,text="Guardar como: ", font=("",10,"bold"))
    etiquetaGuardar.grid(row=1, column=0, pady=5, padx=5)
    #ventana
    vn.textoGuardar=Entry(vn,width=30)
    vn.textoGuardar.grid(row=1,column=1,pady=5,padx=5)
    #botonGuardar
    botonGuardar=Button(vn,text="Navegar",width=10,command = navegar)
    botonGuardar.grid(row=1,column=2,pady=5,padx=5)
    #botonCaptura
    botonCaptura=Button(vn,text="Captura",width=10,command = captura)
    botonCaptura.grid(row=2,column=1,pady=5,padx=5)
#Funcion para nevegar y guardar la imagen
def navegar():
    vn.archivoNombre=filedialog.asksaveasfilename(title="Guardar como",
                                                  initialdir="C:\\Users\\raynier\\Desktop",  #tienen que ir con 2 \\ si no da error
                                                  defaultextension=".png",
                                                  filetypes=(("Archivos png","*.png"),("Todos los Archivos","*.*")))
    vn.textoGuardar.insert("1",vn.archivoNombre)
#Funcion de Screenshot
def captura():
    captura=pyautogui.screenshot()
    captura.save(vn.archivoNombre)
    messagebox.showinfo("Exito","Captura Guardada")


vn=tk.Tk()
vn.title("Captura de Pantalla")
CrearWidgets()
vn.mainloop()


