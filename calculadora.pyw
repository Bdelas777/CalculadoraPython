from tkinter import *
raiz=Tk()
raiz.title("Calculadora con Python")
raiz.config(bg="white")
miFrame=Frame(raiz)
miFrame.pack()
operacion="" 
# al inicio de programa operacion vale cadena vacia y aqui lo dejamos vacio para poder meter el valor
reset_pantalla=False
resultado=0

#-------------pantalla---------------------------------------
numeroPantalla=StringVar()#StringVar es un string de caracteres
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1,padx=10,pady=10 ,columnspan=4)#damos posicion y espacio
#columnspan hace que una columna sea mas grande dependiendo de la posiciones que quieras
pantalla.config(bg="black",fg="#03f943", justify="right")#bg es elcolor de la pantalla y fg de los numeros, 
#justify es para poner en que posicion lo queremos en este caso a la derecha

#-------------------pulsaciones teclado--------------------------
#funciones lambda o funciones anonimas son funciones para simplificar sintaxsis en ciertas circustancias
def numeroPulsado(num):
	global operacion #global es que accesible en cualquier funcion o metodo del programa
	global reset_pantalla
	if reset_pantalla!=False:
		numeroPantalla.set(num)
		reset_pantalla=False
	else:
		numeroPantalla.set(numeroPantalla.get() + num) #metodo set establece un valor en pantalla 
	#metodo get obtiene la informacion que hay en pantalla aqui ve que tenemos y le suma un lo que haya

#funcion suma
def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	resultado+=float(num) #resultado=resultado+int(num)
	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)#aqui le decimos que salga el resultado

#---------------funcion resta------------------------------
num1=0
contador_resta=0
def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla
	if contador_resta==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-float(num)
		else:
			resultado=float(resultado)-float(num)	
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True

#-------------funcion multiplicacion---------------------
contador_multi=0
def multiplica(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla
	if contador_multi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*float(num)
		else:
			resultado=float(resultado)*float(num)	
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_multi=contador_multi+1
	operacion="multiplicacion"
	reset_pantalla=True

#-----------------funcion division---------------------
contador_divi=0
def divide(num):
	global operacion
	global resultado
	global num1
	global contador_divi
	global reset_pantalla
	if contador_divi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_divi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)	
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_divi=contador_divi+1
	operacion="division"
	reset_pantalla=True

#-------------funcion potencia---------------------
contador_pot=0
def potencia(num):
	global operacion
	global resultado
	global num1
	global reset_pantalla
	global contador_pot
	global reset_pantalla
	if contador_pot==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_pot==1:
			resultado=num1**float(num)
		else:
			resultado=float(resultado)**float(num)	
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_pot=contador_pot+1
	operacion="potencia"
	reset_pantalla=True

#-------------funcion raiz---------------------
contador_rai=0
def rai(num):
	global operacion
	global resultado
	global num1
	global reset_pantalla
	global contador_rai
	global reset_pantalla
	if contador_pot==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_rai==1:
			resultado=num1**.5
		else:
			resultado=float(resultado)**.5
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_rai=contador_rai+1
	operacion="rai"
	reset_pantalla=True

#-------------clean---------------------
def clean():
	numeroPantalla.set("")
	
#----------------funcion el_resultado----------------
def el_resultado():
	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi
	global contador_pot
	if operacion=="suma":
		numeroPantalla.set(resultado+float(numeroPantalla.get()))
		resultado=0
	elif operacion=="resta":
		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
		resultado=0
		contador_resta=0
	elif operacion=="multiplicacion":
		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
		resultado=0
		contador_multi=0
	elif operacion=="division":
		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		resultado=0
		contador_divi=0
	elif operacion=="potencia":
		numeroPantalla.set(float(resultado)**float(numeroPantalla.get()))
		resultado=0
		contador_pot=0
	elif operacion=="rai":
		numeroPantalla.set(float(resultado)**.5)
		resultado=0
		contador_rai=0

#-------------fila 1---------------------------------------------
botonPot=Button(miFrame, text="^", width=3, command=lambda:potencia(numeroPantalla.get()))#Establecemos el boton y su anchura
botonPot.grid(row=2,column=1)
botonRai=Button(miFrame, text="√", width=3, command=lambda:rai(numeroPantalla.get()))#Establecemos el boton y su anchura
botonRai.grid(row=2,column=2)
botonPi=Button(miFrame, text="π", width=3,command=lambda:numeroPulsado("3.1416"))#Establecemos el boton y su anchura
botonPi.grid(row=2,column=3,)
botonClean=Button(miFrame, text="AC", width=3, command=clean)#Establecemos el boton y su anchura
botonClean.grid(row=2,column=4)

#-------------fila 2---------------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))#Establecemos el boton y su anchura
boton7.grid(row=3,column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))#Establecemos el boton y su anchura
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))#Establecemos el boton y su anchura
boton9.grid(row=3, column=3)
botondiv=Button(miFrame, text="÷", width=3, command=lambda:divide(numeroPantalla.get()))#Establecemos el boton y su anchura
botondiv.grid(row=3,column=4)

#-------------fila 3---------------------------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))#Establecemos el boton y su anchura y usamos command para llamar a la funcion
#Usar los parentesis hace una llamada automatica sin que el usuario lo pida
#Parentesis en funcion es ejecutar codigo funcion y almacenarlo en command
boton4.grid(row=4,column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))#Establecemos el boton y su anchura
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3,command=lambda:numeroPulsado("6"))#Establecemos el boton y su anchura
boton6.grid(row=4, column=3)
botonmulti=Button(miFrame, text="×", width=3, command=lambda:multiplica(numeroPantalla.get()))#Establecemos el boton y su anchura
botonmulti.grid(row=4,column=4)

#-------------fila 4---------------------------------------------
boton1=Button(miFrame, text="1", width=3,command=lambda:numeroPulsado("1"))#Establecemos el boton y su anchura
boton1.grid(row=5,column=1)
boton2=Button(miFrame, text="2", width=3,command=lambda:numeroPulsado("2"))#Establecemos el boton y su anchura
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3,command=lambda:numeroPulsado("3"))#Establecemos el boton y su anchura
boton3.grid(row=5, column=3)
botonmenos=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))#Establecemos el boton y su anchura
botonmenos.grid(row=5,column=4)

#-------------fila 5---------------------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))#Establecemos el boton y su anchura
boton0.grid(row=6,column=1)
botonpunto=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))#Establecemos el boton y su anchura
botonpunto.grid(row=6, column=2)
botonmas=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))#Establecemos el boton y su anchura
botonmas.grid(row=6, column=4)
botonigual=Button(miFrame, text="=", width=3,command=lambda:el_resultado())#Establecemos el boton y su anchura
botonigual.grid(row=6,column=3)

raiz.mainloop()