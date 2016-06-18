#UNIVERSIDAD DE EL SALVADOR
#FACULTAD DE INGENIERIA Y ARQUITECTURA
#Escuela de Ingenieria Electrica
#Analisis Numerico
#Docente: Msr. Ing. Wilber Calderon
#Tarea final: Metodos de integracion de Simpson
#Tarea realizada por:
#Henry Anselmo Torres Vanegas
#Deiby Josue Moreira Gomez

#  -*- coding: utf-8 -*-

from Tkinter import*
from numpy import *
#from numpy import as no
from matplotlib import*
from math import*


	
v0 = Tk() # Tk() Ventana principal



v0.title("Primera ventana")#titulo de la ventana principal
v0.geometry("350x700")#Tamano de la ventana
v0.resizable(0, 0)
v0.config(bg = "brown")#color de la ventana
etiqueta = Label(v0, text="Metodos de integracion de simpson",relief=SOLID,bg='grey')#Label ventana ppal
etiqueta.grid(padx = 70, pady =0)#Ubicacion ventana ppal

v1=Toplevel(v0)#Ventana Hija Metodo de simpson
v1.title("Metodos de simpson")#Titulo ventana hija
v1.geometry("400x350")#tamano de la ventana hija

v1.config(bg = "brown")#color ventana hija
etiqueta = Label(v1, text="Metodo de simpson 1/3",bg='grey')#Etiqueta de la ventana hija
etiqueta.grid(padx = 70,pady =20)#Ubicacion de la ventana hija
etiqueta1 = Label(v1, text="programa que realiza la integracion\npor los metodos de simpson\npara calcular el valor de la integral\ndefinida de una funcion\ncuya variable independiente es x.\nel metodo da una acertada estimacion del valor real\nde la integral\ndependiendo de los intervalos en los que se divide\nasi sera la exactitud del calculo\npodemos tener los intervalos que deseemos,con la unica\ncondicion de que el valor de n debe ser par.\n",bg='grey')#mensaje
etiqueta1.grid(padx = 15,pady =8)#ubicacion del mensaje
boton3 = Button(v1,text="Cerrar",bg="silver", command=v1.destroy)#boton para cerrar ventana hija
boton3.grid(padx = 70,pady =40)#ubicacion del boton
 
v0.grab_set()
def mostrar (v1) :
    v1.deiconify() 

def destroyed(v1) :
    v1.withdraw()

boton1 = Button(v0, text="Descripcion del metodo", command = lambda : mostrar(v1),relief=SOLID,bg='grey')#boton 1
boton1.grid(padx = 0,pady =16)
v1.withdraw()



v2=Toplevel(v0)#Ventana Hija Metodo de simpson
v2.title("como usar")#Titulo ventana hija
v2.geometry("600x300")#tamano de la ventana hija

v2.config(bg = "brown")#color ventana hija
etiqueta = Label(v2, text="Metodo de simpson 1/3",bg='grey')#Etiqueta de la ventana hija
etiqueta.grid(padx = 70,pady =20)#Ubicacion de la ventana hija
etiqueta2 = Label(v2, text="El metodo de simpson es un metodo numerico el cual realiza\n integraciones definidas,para utilizar el primer metodo\ndebemos introducir los limites y la funcion f\n de la forma x**2+1 . \n y en simpson 1/3 debemos introducir el valor de n que son las subdivisiones delintervalo\npara simpson 3/8 no es necesario introducir n\n porque n siemore vale 3,debe quedar claro\n que en 1/3 n siempre debe ser PAR",bg='grey')#mensaje
etiqueta2.grid(padx = 15,pady =8)#ubicacion del mensaje
boton4 = Button(v2,text="Cerrar",bg="silver", command=v2.destroy)#boton para cerrar ventana hija
boton4.grid(padx = 70,pady =40)#ubicacion del boton
 
v0.grab_set()
def mostrar (v2) :
    v2.deiconify() 

def destroyed(v2) :
    v2.withdraw()

boton2 = Button(v0, text="como usar", command = lambda : mostrar(v2),relief=SOLID,bg='grey')#boton 1
boton2.grid(padx = 0,pady =16)
v2.withdraw()

#y=f(fun1,7)

		
fun1=StringVar()
limi2=IntVar()
lims3=IntVar()
varn4=IntVar()

lab99=Label(v0, text="Escriba la Funcion",bg="brown",fg="white")
lab99.grid(padx = 0,pady =10)
camp=Entry(v0, textvariable=fun1, bg="white", fg="black")
camp.grid(padx = 0,pady =20)
lab00=Label(v0, text="Escriba el limite inferior", bg="brown",fg="white")
lab00.grid(padx = 0,pady =10)
lim=Entry(v0, textvariable=limi2, bg="white",fg="black")
lim.grid(padx = 0,pady =20)
lab66=Label(v0, text="Escriba el limite superior", bg="brown",fg="white")
lab66.grid(padx = 0,pady =10)
lim3=Entry(v0, textvariable=lims3, bg="white", fg="black")
lim3.grid(padx = 0,pady =20)
lab88=Label(v0, text="Escriba el valor de n, n debe ser PAR",bg="brown",fg="white")
lab88.grid(padx = 0,pady =10)
var4=Entry(v0, textvariable=varn4, bg="white", fg="black")
var4.grid(padx = 0,pady =20)
boton00 = Button(v0, text="Resolver por simpson 1/3",command = lambda : mostrar(v3),relief=SOLID,bg='grey')#boton3
boton00.grid(padx = 0,pady = 6)

#variables de pantalla 3
fun=StringVar()
liminf = IntVar()
limsup = IntVar()

v3=Toplevel(v0)#Ventana Hija Metodo de simpson
v3.title("Simpson")#Titulo ventana hija
v3.geometry("340x300")#tamano de la ventana hija
v3.config(bg = "brown")#color ventana hija
 
v0.grab_set()

def mostrar (v3) :
    v3.deiconify() 
    me=fun1.get()
    mlabel2 = Label(v3,text="SOLUCION POR SIMPSON 1/3",bg="brown",fg="white")
    mlabel2.grid(padx = 0,pady =10)
    
    li=double (limi2.get()) #limite inferior
    ls = double (lims3.get()) #Limite superior
    n= double (varn4.get()) # n 
    res = double ((ls-li)/(3*n)) #primer parte
    suma=0.0
    dif = (ls-li)/n
    nn= int(varn4.get())
    lin=int(limi2.get())
    
    mlabel2 = Label(v3,text="Tu funcion es: "+str(me),bg="brown",fg="white")
    mlabel2.grid(padx = 0,pady = 30)
    
    
    for i in range(1,nn-1):
		
		x=li+ i*dif
		if(i % 2 == 0):
			suma = suma + 2*eval(me)
			
    for i in range(1,nn):
		
		x=li+ i*dif
		
		if(i % 2 != 0):
			suma = suma + 4*eval(me)
			

    x=ls
    suma=suma+eval(me)
    x=li
    suma=suma+eval(me)
    suma=suma*res
    mlab = Label(v3,text="Respuesta: "+str(suma),bg="brown",fg="white")
    mlab.grid(padx = 0,pady =40)
    
    boton4 = Button(v3,text="Cerrar",bg="silver", command = lambda : destroyed (v3) )#boton para cerrar ventana hija
    boton4.grid(padx = 150,pady =50)#ubicacion del boton   
    
    

def destroyed(v3) :
    v3.withdraw()
    camp.delete('0',END)
  
v3.withdraw()



boton4 = Button(v0, text="Resolver por simpson 3/8",command = lambda : mostrar(v4),relief=SOLID,bg='grey')#boton3
boton4.grid(padx = 0,pady = 6)

v4=Toplevel(v0)#Ventana Hija Metodo de simpson
v4.title("Simpson")#Titulo ventana hija
v4.geometry("340x350")#tamano de la ventana hija

v4.config(bg = "brown")#color ventana hija


  


def mostrar (v4) :
    v4.deiconify() 
    me=fun1.get()
    mlabel2 = Label(v3,text="SOLUCION POR SIMPSON 1/3",bg="brown",fg="white")
    mlabel2.grid(padx = 0,pady =10)
    
    li=double (limi2.get()) #limite inferior
    ls = double (lims3.get()) #Limite superior
    mlabel2 = Label(v4,text="Tu funcion es: "+str(me),bg="brown",fg="white")
    mlabel2.grid(padx = 0,pady = 30)
    dif=double((ls-li)/3)
    h=double((ls-li)/8)
    suma=0.0
    x=li
    suma=eval(me)
    x=li+dif
    suma=suma+3*eval(me)
    x=li+2*dif
    suma=suma+3*eval(me)
    x=li+3*dif
    suma=suma+eval(me)
    suma=suma*h
    mlab = Label(v4,text="Respuesta: "+str(suma),bg="brown",fg="white")
    mlab.grid(padx = 0,pady =40)
       
    bo4 = Button(v4,text="Cerrar",bg="silver", command = lambda : destroyed (v4) )#boton para cerrar ventana hija
    bo4.grid(padx = 150,pady =50)#ubicacion del boton

def destroyed(v4) :
    v4.withdraw()
    camp.delete('0',END)


v4.withdraw()

v0.grab_set()


boton8 = Button(v0,text="Salir",bg="silver", command=v0.destroy)#boton para cerrar ventana hija
boton8.grid(padx = 70,pady =20)#ubicacion del boton



v0.mainloop()
