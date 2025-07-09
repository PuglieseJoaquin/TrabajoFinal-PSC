# TrabajoFinal-PSC

Profesor: Daniel J. Feijó

Fecha limite de entraga: 9 de Julio 23:59h 

Fecha de Defensa: 10 de Julio en clase

Alumnos: 
    - Joaquin Sebastian Pugliese
    
    - Mia Quadrelli
    
    - Abril Ortega
    
    - Ailen Mildemberger
    

-> Cumplimiento con el Enunciado 💥

1. Función que indique si un camino es válido
    ✔️ La función  (camino_valido(matriz, origen, destino)),  el juego implementa la verificación de movimientos válidos 
    (solo puedes moverte si hay una flecha en la dirección correcta o el diamante).

2. Generar matriz aleatoria con no más de 4 bombas
    ✔️ Tu función colocar_minas() hace exactamente eso.

3. Función que valide caminatas en presencia de bombas
    ✔️ Ya estás controlando si el jugador pisa una mina y terminas el juego. (dentro del while) 
    
4A. Flechas cambian aleatoriamente en cada paso
    ✔️ Lo haces con la función actualizar_flechas(visible) que se ejecuta al final de cada paso.

5. Indicar si el camino fue eficiente 
    ✔️ Consideramos con el equipo que era una funcion innecesaria ya que las flechas al moverse de manera aleatoria, nunca van a moverse de manera eficiente,
    se moveran los jugadores dependiendo lo que les permita el juego

6/7. Detección de loop 
    ✔️ Cuando el jugador se queda en un Loop le damos la opcion de apretar la tecla "enter" y saltear el turno, 
    haciendo que las flechas cambien de posicion de vuelta

8. Explicación con los 4 elementos del pensamiento computacional
        Descomposición: Separaste tareas en funciones (crear_tablero, mostrar_tablero, etc.)
        Reconocimiento de patrones: Identificaste el uso repetido de flechas y minas.
        Abstracción: Usás símbolos y lógica condicional para manejar bombas, flechas, jugador.
        Algoritmos: Definiste pasos secuenciales para moverse, verificar minas, y ganar o perder.

9. Buenas prácticas de programación 
    ✔️ Buenas prácticas que podrías destacar:
            Buena estructuracion 
            Uso de comentarios.
            Uso de funciones para tareas repetitivas.
            Variables con nombres entendibles.
