#Programa para hacer un recorrido de servomotor por posiciones en la velocidad elegida. Ejemplo: python3 servo.py lento 30 60 90 120
#https://github.com/Dtcsrni
import subprocess
import sys
from time import sleep

# Función para mapear un valor de entrada a un rango de salida
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Función para mover el servomotor a una posición angular
def irAngulo(valor, valorPrevio, velocidad):
    print(f"Moviendo a posición {valor} grados")
    if valor > valorPrevio:
        # Mover gradualmente a la posición deseada con la velocidad especificada
        for i in range(valorPrevio, valor):
            valorPWM = map_value(i, 0, 180, 70, 525)
            subprocess.run(['gpio', 'pwm', '2', str(valorPWM)])
            sleep(velocidad)
    else:
        # Mover gradualmente a la posición deseada con la velocidad especificada
        for i in range(valorPrevio, valor, -1):
            valorPWM = map_value(i, 0, 180, 70, 525)
            subprocess.run(['gpio', 'pwm', '2', str(valorPWM)])
            sleep(velocidad)
    return valor  # Devuelve el nuevo valorPrevio

# Comprobar que se proporcionen al menos 2 argumentos (1 de velocidad y 1 de posición)
if len(sys.argv) < 3:
    print("Usage: python3 servo.py <velocidad> <posicion1> [posicion2] ...")
    sys.exit(1)

# Obtener la velocidad desde el primer argumento
velocidad = sys.argv[1]

# Validar el valor de velocidad y ajustar el tiempo de espera
if velocidad == "muy lento":
    tiempo_espera = 0.1
elif velocidad == "lento":
    tiempo_espera = 0.05
elif velocidad == "normal":
    tiempo_espera = 0.02
elif velocidad == "rapido":
    tiempo_espera = 0.001
elif velocidad == "muy rapido":
    tiempo_espera = 0.005
elif velocidad == "instantaneo":
    tiempo_espera = 0  # Movimiento instantáneo
else:
    print("La velocidad debe ser 'muy lento', 'lento', 'normal', 'rapido', 'extremo rapido' o 'instantaneo'")
    sys.exit(1)

# Obtener las posiciones desde los argumentos restantes
posiciones = [int(arg) for arg in sys.argv[2:]]

# Añadir el tiempo de espera entre estados al tiempo de espera total
tiempo_espera_total = tiempo_espera + 0.1  # 0.1 segundos de margen entre estados

# Inicializar el valorPrevio en 0 (posición inicial)
valorPrevio = 0

# Imprimir mensaje de inicio
print("Moviendo el servo a la posición inicial")

# Iterar a través de las posiciones y mover el servo
for valor in posiciones:
    valorPrevio = irAngulo(valor, valorPrevio, tiempo_espera)
    sleep(tiempo_espera_total)

# Mensaje de regreso a la posición inicial
print("Regresando a origen")
