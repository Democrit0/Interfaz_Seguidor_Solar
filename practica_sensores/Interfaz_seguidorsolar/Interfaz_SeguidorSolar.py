import tkinter
import serial
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Devices.MotorPositionController import *
import time

#8.88 en el motor, se mueve 1 grado
#3200 es para 360
#7.11
#2560 es para 360

ser = None
is_on = True
Hori = None
Vert = None


def switch():
    global is_on
    global ser
    global ns1
    global ns2
    if is_on:
        try:
            """----------------------Motor 1 en canal 0----------------------"""
            ns1 = MotorPositionController()
            ns1.setHubPort(0) #Se declara el Puerto en donde el motor esta conectado al HUB
            ns1.setDeviceSerialNumber(561362) #Número de serie del HUB
            ns1.openWaitForAttachment(5000) #Intenta la comunicación con el HUB y espera 5000 ms ó 5 seg
            ns1.setKd(-40000) #Ganancia Kd [Motor 1]: Amortigua la salida
            ns1.setKi(-5) #Ganancia Ki [Motor 1]: Corrige el error en estado estacionario
            ns1.setKp(-20000) #Ganancia Kp [Motor 1]: Proporciona energía
            """----------------------Motor 2 en canal 1----------------------"""
            """bldcMotor1 = BLDCMotor()
            ns2 = MotorPositionController()
            ns2.setHubPort(1)
            # ns2.setDeviceSerialNumber(561362)
            ns2.openWaitForAttachment(5000)
            ns2.setKd(-40000)
            ns2.setKi(-5)
            ns2.setKp(-20000)"""
            """---------------------- Código de Arduino----------------------"""

        except Exception as e:
            print("Error al conectar:", e)
        boton7.config(image=on)
        is_on = False

    else:
        boton7.config(image=off)
        is_on = True
        try:
            if ser:
                ser.close()
                ns1.close()
                print("desconectado")
                MessageBox.showinfo(message="DESCONECTADO", title="ALERTA")
        except Exception as e:
            print("Error al desconectar:", e)


def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)


def close_window(event):
    window.destroy()


#derecha
def boton_1():
    global Hori
    global ns1
    Hori = True
    ns1.setTargetPosition(0)
    ns1.setEngaged(True)

#izquierda
def boton_2():
    global ns1
    global Hori
    Hori = False
    ns1.setTargetPosition(0)
    ns1.setEngaged(True)

#arriba
def boton_3():
    global Vert
    global ns2
    Vert = True


#abajo
def boton_4():
    global Vert
    global ns2
    Vert = False


#boton de paro
def boton_5():
    #bldcMotor1.setTargetVelocity(0)
    return True

def enviar():
    global ns1
    conver = True
    recibir1 = num.get()
    recibir2 = num1.get()
    if conver:
        pasos_1 = recibir1*7.11
        ns1.setTargetPosition(pasos_1)
        ns1.setEngaged(True)
    else:
        pasos_2 = recibir1*8.88
        ns1.setTargetPosition(pasos_2)
        ns1.setEngaged(True)

    #ns2.setTargetPosition(recibir2)
    #ns2.setEngaged(True)
    #bldcMotor1.setTargetVelocity(recibir2)
    if Hori:
        #Giro a la derecha
        #bldcMotor0.setTargetVelocity(1)
        print("Derecha")
    else:
        #Giro a la derecha
        #bldcMotor0.setTargetVelocity(-1)
        print("Izquierda")

    if Vert:
        #Sube
        #bldcMotor1.setTargetVelocity(1)
        print("Arriba")
    else:
        #Baja
        #bldcMotor1.setTargetVelocity(-1)
        print("Abajo")


    """if int(recibir1) > 90:
        MessageBox.showerror(title="Valor incorrento", message="Solo acepta valores entre 0 y 90")
    elif int(recibir1) < 0:
        MessageBox.showerror(title="Valor incorrento", message="Solo acepta valores entre 0 y 90")

    elif int(recibir2) > 90:
        MessageBox.showerror(title="Valor incorrento", message="Solo acepta valores entre 0 y 90")
    elif int(recibir2) < 0:
        MessageBox.showerror(title="Valor incorrento", message="Solo acepta valores entre 0 y 90")
    """
    """datos1 = recibir1.encode()
    datos2 = recibir2.encode()
    #ser.write(datos1)
    #ser.write(datos2)
"""


def ventana_about():
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("About")
    aframe_1 = LabelFrame(ventana_secundaria, text="Nombre de la matería")
    aframe_1.grid(column=0, row=0)
    etq1 = Label(aframe_1, text="Diseño, Construcción y puesta en marcha de sistemas energéticos",
                 font=('bold')).pack(anchor=CENTER)

    aframe_2 = LabelFrame(ventana_secundaria, text="Profesor")
    aframe_2.grid(column=0, row=1)
    etq2 = Label(aframe_2, text="Dr. José Alejandro Aguirre Anaya").pack(padx=205)

    aframe_3 = LabelFrame(ventana_secundaria, text="Equipo 1")
    aframe_3.grid(column=0, row=2)
    etq3 = Label(aframe_3, text="INTEGRANTES:", font=('verdana', 10))
    etq3.grid(column=0, row=0)
    etq5 = Label(aframe_3, text="Aguirre Castillo Nils Francisco \n"
                                "Arroyo Barrios María Fernanda \n"
                                "Castillo Luna Armando \n "
                                "González García Juan \n"
                                "González Maldonado Ramiro Alejandro \n"
                                "Guerrero VIlleda Selene Minerva \n"
                                "Nolasco Ibarra Octavio\n"
                                "Pérez Martínez Zahra Amy \n"
                                "Santiago Rosales Andrey Sarahy")
    etq5.grid(column=0, row=1, padx=185)


window = Tk()
window.attributes('-fullscreen', False)
window.title("ventana")
window.config(bg="white")

num = IntVar()
num1 = IntVar()

"""/--------------------------------Imagenes--------------------------------/"""
foto1 = Image.open('../horario.png')
foto1 = foto1.resize((50, 50))
photo1 = ImageTk.PhotoImage(foto1)

foto2 = Image.open('../antihorario.png')
foto2 = foto2.resize((50, 50))
photo2 = ImageTk.PhotoImage(foto2)

foto3 = Image.open('../arriba.png')
foto3 = foto3.resize((50, 50))
photo3 = ImageTk.PhotoImage(foto3)

foto4 = Image.open('../abajo.png')
foto4 = foto4.resize((50, 50))
photo4 = ImageTk.PhotoImage(foto4)

foto5 = Image.open('../posicion_sol.jpg')
foto5 = foto5.resize((240, 220))
photo5 = ImageTk.PhotoImage(foto5)

foto6 = Image.open('../Logo_IPN.png')
foto6 = foto6.resize((120, 120))
photo6 = ImageTk.PhotoImage(foto6)

foto7 = Image.open('../upiem.png')
foto7 = foto7.resize((150, 120))
photo7 = ImageTk.PhotoImage(foto7)

foto8 = Image.open('../ON_2.png')
foto8 = foto8.resize((35, 35))
on = ImageTk.PhotoImage(foto8)

foto9 = Image.open('../off.png')
foto9 = foto9.resize((35, 35))
off = ImageTk.PhotoImage(foto9)

"""/--------------------------------Frame 1--------------------------------/"""
"""/--------------------------Control de motores---------------------------/"""
frame1 = LabelFrame(window, text="", bg="white")
frame1.grid(column=1, row=1, padx=5, pady=5, rowspan=2)

label1 = Label(frame1, text="Derecha", bg="white")
label1.grid(row=0, column=0, padx=(110,20), pady=1)
boton1 = Button(frame1, image=photo1, command=boton_1)
boton1.grid(row=0, column=1, padx=(20,110), pady=2)

label2 = Label(frame1, text="Izquierda", bg="white")
label2.grid(row=1, column=0, padx=(110,20), pady=1)
boton2 = Button(frame1, image=photo2, command=boton_2)
boton2.grid(row=1, column=1, padx=(20,110), pady=2)

label3 = Label(frame1, text="Arriba", bg="white")
label3.grid(row=2, column=0, padx=(110,20), pady=1)
boton3 = Button(frame1, image=photo3, command=boton_3)
boton3.grid(row=2, column=1, padx=(20,110), pady=2)

label4 = Label(frame1, text="Abajo", bg="white")
label4.grid(row=3, column=0, padx=(110,20), pady=1)
boton4 = Button(frame1, image=photo4, command=boton_4)
boton4.grid(row=3, column=1, padx=(20,110), pady=2)

"""/--------------------------------Frame 2--------------------------------/"""
"""/--------------------------------Entrys---------------------------------/"""
frame2 = LabelFrame(window, text="", bg="white")
frame2.grid(column=2, row=1, padx=5, pady=5, rowspan=2)

label5 = Label(frame2, text="Ingrese los grados de giro \n (0° a 360°)", bg="white")
label5.grid(row=0, column=0, padx=10, pady=(11,8))
entry1 = Entry(frame2, textvariable=num)
entry1.grid(row=1, column=0, padx=10, pady=1)
label6 = Label(frame2, text="Ingrese los grados de elevación \n (0° a 90°)", bg="white")
label6.grid(row=2, column=0, padx=10, pady=1)

entry2 = Entry(frame2, textvariable=num1)
entry2.grid(row=3, column=0, padx=10, pady=1)

boton5 = Button(frame2, text="Enviar", command=enviar, borderwidth=5, cursor="hand1")
boton5.grid(row=6, column=0, padx=10, pady=35)

"""/--------------------------------Frame 4--------------------------------/"""
"""/-------------------------Botón de emergencia---------------------------/"""
frame4 = LabelFrame(window, text="", bg="white")
frame4.grid(column=0, row=1, padx=5, pady=5)

label11 = Label(frame4, text="Comunicaciones", bg="white")
label11.grid(column=0, row=0, padx=10, pady=(10,5))
boton7 = Button(frame4, image=off, relief="flat", bg="white", activebackground='#A3FF1F', cursor="hand1", command=switch)
boton7.grid(column=0, row=1)
label10 = Label(frame4, text="Paro de emergencia", bg="white",fg="#303030")
label10.grid(column=0, row=2, padx=10,pady=5)
boton6 = Button(frame4, text="Detener", command=boton_5, borderwidth=5, cursor="hand1",fg="#303030")
boton6.grid(column=0, row=3, padx=45, pady=10)


"""/--------------------------------Frame 3-------------------------------/"""
"""/----------------------------Botón de About----------------------------/"""
frame3 = LabelFrame(window, text="", bg="white")
frame3.grid(column=0, row=2, padx=5, pady=5)
boton5 = Button(frame3, text="About", command=ventana_about, borderwidth=5, padx=6, cursor="hand1")
boton5.pack(padx=45, pady=15)

"""/--------------------------------Frame 5-------------------------------/"""
"""/---------------------------Frames de IMAGENES-------------------------/"""
frame5 = LabelFrame(window, text="", bg="white")
frame5.grid(column=1, row=0, padx=5, pady=5)
label7 = Label(frame5, image=photo5)
label7.grid(column=0, row=0, padx=62, pady=5)

"""Imagen IPN"""
frame6 = LabelFrame(window, text="", bg="white")
frame6.grid(column=0, row=0)
label8 = Label(frame6, image=photo6, bg="white")
label8.grid(column=0, row=0, padx=12, pady=55)

"""Imagen UPIEM"""
frame7 = LabelFrame(window, text="", bg="white")
frame7.grid(column=2, row=0)
label9 = Label(frame7, image=photo7, bg="white")
label9.grid(column=0, row=0, padx=19, pady=55)
"""
def ubdate_label():
    if ser.in_waiting >-1:
        line = ser.readline().decode('utf-8').rstrip()
        values = line.split(',')
        if values[0] == 'x':
            esp32_1_label.config(text="la corriente es: " + "\n" + values[1])
        if values[0] == 'y':
            esp32_2_label.config(text="La temperatura es : " + "\n" + values[1])

        window.after(40, ubdate_label)"""
#ubdate_label()
window.mainloop()
