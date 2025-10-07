import time
import board
import pwmio

# Configuramos el pin de salida LED en modo PWM, con una
# frecuencia de 5MHz y porcentaje de duty cycle activo de 0,
# es decir apagado todo el tiempo:
led = pwmio.PWMOut(board.GP1, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        if i < 50:
            # En la primer mitad del ciclo de 100 pasos vamos aumentando
            # el duty cycle paulatinamente hasta llegar al máximo de 65535
            led.duty_cycle = int(i * 2 * 65535 / 100)
        else:
            # En la segunda mitad del ciclo hacemos el proceso inverso,
            # disminuyendo hasta llegar a 0
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
        time.sleep(0.01)
