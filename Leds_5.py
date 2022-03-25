#Se Importa la libreria de Firmata para la cominicación genérica con arduino
#si no se tiene se instala ejecutando el comando pip install Firmata
#
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
print("")
print("Conectado con la Tarjeta Arduino")
print("")

button = board.digital[2]
Led1 = board.digital[11]
Led2 = board.digital[10]

Led_Encendido = 0
Boton_encendido = 0

it = pyfirmata.util.Iterator(board)
it.start()
button.mode = pyfirmata.INPUT

while True:
    Boton_estado = button.read()
    if Boton_estado != Boton_encendido:
        if Boton_estado is True:
            Led1.write(0)
            Led2.write(0)
            Led_Encendido +=1
            time.sleep(.05)
            if Led_Encendido == 2:
                Led1.write(1)
                print("Presionado")
                time.sleep(5)
                Led1.write(0)
            elif Led_Encendido == 4:
                Led2.write(1)
                print("Presionado")
                time.sleep(5)
                Led2.write(0)
                Led_Encendido = 0
    Boton_encendido = Boton_estado

