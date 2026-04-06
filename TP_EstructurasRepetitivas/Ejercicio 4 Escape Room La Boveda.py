# Ejercicio 4  — “Escape Room: La Bóveda” 

energia = 100
tiempo = 12
cerradurasAbiertas = 0
alarma = False
codigoParcial = ""
rachaForzar = 0

agente = input("Ingrese nombre del agente: ")
while not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ")

while energia > 0 and tiempo > 0 and cerradurasAbiertas < 3 and not alarma:
    print(f"\nAgente: {agente} | Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerradurasAbiertas} | Alarma: {alarma}")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía máx 100, -1 tiempo)")
    
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input("Error. Ingrese 1, 2 o 3: ")
    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        rachaForzar += 1

        if rachaForzar == 3:
            alarma = True
            print("La cerradura se trabó! Se activó la alarma.")
        else:
            if energia < 40:
                numero = input("Riesgo de alarma. Ingrese un número (1-3): ")
                while not numero.isdigit() or int(numero) not in [1, 2, 3]:
                    numero = input("Error. Ingrese un número válido (1-3): ")
                if int(numero) == 3:
                    alarma = True
                    print("Se activó la alarma!")
            if not alarma and rachaForzar < 3:
                cerradurasAbiertas += 1
                print("Cerradura forzada con éxito.")
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        rachaForzar = 0
        for i in range(4):
            codigoParcial += "A"
            print(f"Hackeando... paso {i+1}, código: {codigoParcial}")
        if len(codigoParcial) >= 8 and cerradurasAbiertas < 3:
            cerradurasAbiertas += 1
            print("Panel hackeado! Cerradura abierta.")
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        rachaForzar = 0
        if alarma:
            energia -= 10
            print("Descansar con alarma activa consume más energía.")

    if alarma and tiempo <= 3 and cerradurasAbiertas < 3:
        print("El sistema se bloqueó por alarma. DERROTA.")
        break

if cerradurasAbiertas == 3:
    print("VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")
elif alarma:
    print("DERROTA. El sistema se bloqueó por alarma.")