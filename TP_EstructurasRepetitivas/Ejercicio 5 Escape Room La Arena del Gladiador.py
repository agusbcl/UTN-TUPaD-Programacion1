#Ejercicio 5  — “Escape Room:"La Arena del Gladiador" 

print("--- BIENVENIDO A LA ARENA ---")

nombreGladiador = input("Nombre del Gladiador: ")
while not nombreGladiador.isalpha():
    nombreGladiador = input("Error: Solo se permiten letras. Nombre del Gladiador: ")

#Estadísticas
vidaGladiador = 100
vidaEnemigo = 100
pociones = 3
ataquePesado = 15
ataqueEnemigo = 12
turnoGladiador = True
juegoActivo = True

print("=== INICIO DEL COMBATE ===")

#Combate
while vidaGladiador > 0 and vidaEnemigo > 0 and juegoActivo:
    if turnoGladiador:
        print(f"\n{nombreGladiador} (HP: {vidaGladiador}) vs Enemigo (HP: {vidaEnemigo}) | Pociones: {pociones}")
        print("Elige accion:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")
        while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
            opcion = input("Error: Ingrese un numero valido (1-3): ")
        opcion = int(opcion)

        if opcion == 1:
            if vidaEnemigo < 20:
                daño = ataquePesado * 1.5
                print(f"Golpe Critico! Atacaste al enemigo por {daño:.1f} puntos de daño!")
            else:
                daño = ataquePesado
                print(f"Atacaste al enemigo por {daño} puntos de daño!")
            vidaEnemigo -= daño

        elif opcion == 2:
            print(">> Inicias una ráfaga de golpes!")
            for i in range(3):
                vidaEnemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vidaGladiador += 30
                pociones -= 1
                print(f"Has usado una poción! Vida actual: {vidaGladiador}")
            else:
                print("No quedan pociones!")

#Turno del enemigo
        vidaGladiador -= ataqueEnemigo
        print(f">> El enemigo contraataca por {ataqueEnemigo} puntos!")

        if vidaGladiador > 0 and vidaEnemigo > 0:
            print("=== NUEVO TURNO ===")

#Resultados
if vidaGladiador > 0 and vidaEnemigo <= 0:
    print(f"VICTORIA! {nombreGladiador} ha ganado la batalla.")
elif vidaGladiador <= 0:
    print("DERROTA. Has caído en combate.")