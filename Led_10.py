
#uso de la libreria tkinter para menú boton
from tkinter import *
root = Tk()
#Se Importa la libreria de Firmata para la cominicación genérica con arduino
#si no se tiene se instala ejecutando el comando pip install Firmata
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
print("Conectado")

button = board.digital[2]
Led1 = board.digital[11]
Led2 = board.digital[10]

Led_Encendido = 0
button_enc = 0


it = pyfirmata.util.Iterator(board)
it.start()

root.title("PushBottons Python y Arduino")
root.geometry('300x400')

def botton():
    boton1 = True
    button_state = boton1
    texto =Button(root,text="Apagado", bg="red",padx=30, pady=30,command=botton, width=5, height=2).grid()
    if button_state != button_enc:
        
        if  button_state is True:
            
            Led1.write(1)
            print("Presionado")
            time.sleep(10)
            Led1.write(0)

Boton =Button(root,text="Encendido", bg="green",padx=30, pady=30,command=botton, width=10, height=5).grid(row=5,column=5)

root.mainloop()