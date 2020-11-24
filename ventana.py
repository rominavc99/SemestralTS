from tkinter import *



ventana = Tk()
ventana.title("Afinador de guitarra")
ventana.geometry("800x600")


def apretar():
    lblCuerda = Label(ventana, text="6ta Cuerda").pack()
    lblFrecuencia = Label(ventana, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(ventana, text="80Hz").pack()
    lblApretar = Label(ventana, text="Es necesario apretar").pack()

def aflojar():
    lblCuerda = Label(ventana, text="6ta Cuerda").pack()
    lblFrecuencia = Label(ventana, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(ventana, text="80Hz").pack()
    lblAflojar = Label(ventana, text="Es necesario aflojar").pack()

def correcto():
    lblCuerda = Label(ventana, text="6ta Cuerda").pack()
    lblFrecuencia = Label(ventana, text="Frecuencia Actual").pack()
    lblFrecuenciaDato = Label(ventana, text="80Hz").pack()
    lblCorreto = Label(ventana, text="La frecuencia es correcta").pack()

def iniciar():
    apretar()
    aflojar()
    correcto()
    

boton = Button(ventana, text="Iniciar", command=iniciar)
boton.pack()

ventana.mainloop()
