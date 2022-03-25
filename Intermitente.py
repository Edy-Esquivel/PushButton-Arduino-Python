
#Se Importa la libreria de Firmata para la cominicación genérica con arduino
#si no se tiene se instala ejecutando el comando pip install Firmata
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
print("Conectado con la Tarjeta Arduino")

button = board.digital[2]
Led1 = board.digital[11]
Led2 = board.digital[10]

Led_Encendido = 0
button_enc = 0

it = pyfirmata.util.Iterator(board)
it.start()


def Intermitente():
    encender = input("Ingrese las teclas AY para encender intermitentemente: ").upper()
    if encender == 'AY':
        while True:
            Led1.write(1)
            print("Presionado")
            Led2.write(1)  
            print("Presionado")  
            time.sleep(.5)
            Led1.write(0)
            print("Presionado")
            Led2.write(0)
            print("Presionado")
            time.sleep(.5)  
                
    else: 
        print("No son las Teclas correspondientes\n")

while True:
    Intermitente()
