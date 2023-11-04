# OrangePi5Plus_Proyectos
-Programa para controlar la rotación de un servomotor utilizando PWM en los GPIO de la Orange Pi 5 Plus. El programa coloca el servo en la posición inicial y luego sigue la ruta especificada en los comandos a la velocidad indicada.
Uso:

<velocidad> <ángulo ><ángulo><ángulo>......<ángulo>

La velocidad puede ser 'muy lento', 'lento', 'normal', 'rapido', 'muy rapido' o 'instantaneo'". Ejemplo:

instantaneo 80 90 50 0 180 140 

En este caso, el servo irá a la posición 80 grados, 90 grados, 50 grados, 0 grados, 180 grados y 140 grados, luego regresará a la posición inicial.
