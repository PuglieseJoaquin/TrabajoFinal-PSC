# Trabajo Final - Juego "Minas Explosivas"

# ---------------- IMPORTACIONES / DECLARACION DE FUNCIONES ----------------
import random 
import os 

def crear_tablero(fil, col):
    tablero = []
    flechas = [" ← ", " ↑ ", " → ", " ↓ "]
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            valor = random.choice(flechas)
            tablero[i].append(valor)
    return tablero

def mostrar_tablero(tablero): 
    for fil in tablero: 
        for elem in fil: 
            print(elem, end=" ") 
        print() 

def actualizar_flechas(tablero):
    flechas = [" ← ", " ↑ ", " → ", " ↓ "]
    # Reacorremos cada fila del tablero
    for i in range(len(tablero)): 
        # Recorre cada columna del tablero
        for j in range(len(tablero[0])): 
            if tablero[i][j] != "🦸" and tablero[i][j] != "💎": 
                tablero[i][j] = random.choice(flechas)

def colocar_minas(tablero, cantidad, fil, col):
    minas_ocultas = []
    while len(minas_ocultas) < cantidad:
        # Generamos coordenadas aleatorias dentro del tablero
        y = random.randint(0, fil - 1) 
        x = random.randint(0, col - 1)
        # No colocar más de una mina en la misma celda
        if tablero[y][x] != "M":  
            tablero[y][x] = "M"
            minas_ocultas.append((y, x))
    return tablero, minas_ocultas

def verificar_victoria(x, y, dx, dy, visible):
    # Coordenadas del jugador y diamante
    if x == dx and y == dy:
        os.system("cls" if os.name == "nt" else "clear")
        visible[y][x] = "🦸" # Coloca el heroe encima del diamante
        mostrar_tablero(visible)
        print("\n🎉 ¡Ganaste! Encontraste el diamante 💎 🎉") # \n = "newline" 
        return True
    return False

def presentacion():
    os.system("cls" if os.name == "nt" else "clear")
    print("**********************************************")
    print("*                                            *")
    print("*              MINAS EXPLOSIVAS              *")
    print("*                                            *")
    print("*                                            *")
    print("*                                            *")
    print("*              w/a/s/d - Moverse             *")
    print("*          'enter' para saltar turno         *")
    print("*                                            *")
    print("**********************************************")
    print("* Debe llegar 🦸 a 💎, podras?*")
    input(" 'Enter' para empezar.... ")

def menu():
    print()
    return input("TECLAS: w/s/a/d - q (salir) - Enter para saltar turno").lower() # Convertimos el texto a minusculas 


# ---------------- FLUJO DEL PROGRAMA ----------------

# Declaracion de variables globales y llamadas a funciones
columnas = 6
filas = 6

visible = crear_tablero(filas, columnas) # Lo que le mostramos al jugador 
oculto = crear_tablero(filas, columnas) # Tabla oculta para las minas 

oculto, minas_ocultas = colocar_minas(oculto, 4, filas, columnas) # Colocar 4 minas en oculto

# Inicia la presentacion 
presentacion()

# Colocar X (Donde empieza el jugador)
y = int(input("En que fila quieres empezar? De la 1 a la 6: "))-1
x = 0 # Primera columna 

real = visible[y][x]
visible[y][x] = "🦸"

# Colocar Diamante (Destino)
dy = int(input("Elija fila de destino, entre 1 y 6: "))-1
dx = 5  # Última columna
real_diamante = visible[dy][dx]
visible[dy][dx] = "💎"

# ======================= BUCLE DEL JUEGO =======================

jugador = True
while jugador:
    os.system("cls" if os.name == "nt" else "clear")
    mostrar_tablero(visible)
    mov = menu()
    # Tecla W - Subir 
    if mov == "w":
        if y > 0 and visible[y-1][x] in [" ↑ ", "💎"]: 
            visible[y][x] = real 
            y -= 1
            real = visible[y][x]
            visible[y][x] = "🦸"
            # Pierde o gana?
            if oculto[y][x] == "M":
                os.system("cls" if os.name == "nt" else "clear")
                mostrar_tablero(visible)
                print("\n💥 ¡Pisaste una mina! GAME OVER 💥")
                jugador = False
            elif verificar_victoria(x, y, dx, dy, visible):
                jugador = False
        else:
            print("❌ Movimiento no permitido: la celda de arriba no tiene flecha ↑ ni es el diamante.")
            input("Presiona Enter para continuar...")
    # Tecla S - Bajar
    elif mov == "s":
        if y < filas - 1 and visible[y+1][x] in [" ↓ ", "💎"]:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "🦸"
            if oculto[y][x] == "M":
                os.system("cls" if os.name == "nt" else "clear")
                mostrar_tablero(visible)
                print("\n💥 ¡Pisaste una mina! GAME OVER 💥")
                jugador = False
            elif verificar_victoria(x, y, dx, dy, visible):
                jugador = False
        else:
            print("❌ Movimiento no permitido: la celda de abajo no tiene flecha ↓ ni es el diamante.")
            input("Presiona Enter para continuar...")
    # Tecla A - Izquierda
    elif mov == "a":
        if x > 0 and visible[y][x-1] in [" ← ", "💎"]:
            visible[y][x] = real
            x -= 1
            real = visible[y][x]
            visible[y][x] = "🦸"
            if oculto[y][x] == "M":
                os.system("cls" if os.name == "nt" else "clear")
                mostrar_tablero(visible)
                print("\n💥 ¡Pisaste una mina! GAME OVER 💥")
                jugador = False
            elif verificar_victoria(x, y, dx, dy, visible):
                jugador = False
        else:
            print("❌ Movimiento no permitido: la celda a la izquierda no tiene flecha ← ni es el diamante.")
            input("Presiona Enter para continuar...")
    # Tecla D - Derecha
    elif mov == "d":
        if x < columnas - 1 and visible[y][x+1] in [" → ", "💎"]:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "🦸"
            if oculto[y][x] == "M":
                os.system("cls" if os.name == "nt" else "clear")
                mostrar_tablero(visible)
                print("\n💥 ¡Pisaste una mina! GAME OVER 💥")
                jugador = False
            elif verificar_victoria(x, y, dx, dy, visible):
                jugador = False
        else:
            print("❌ Movimiento no permitido: la celda a la derecha no tiene flecha → ni es el diamante.")
            input("Presiona Enter para continuar...")
    # Tecla Q
    elif mov == "q":
        print("👋 Saliendo del juego...")
        jugador = False
    # Tecla enter / otras
    else:
        print("Salteo de turno...")
        input("Presiona Enter para continuar...")
    if jugador:
        actualizar_flechas(visible)
