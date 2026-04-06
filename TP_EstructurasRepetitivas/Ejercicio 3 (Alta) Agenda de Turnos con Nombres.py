#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = 0

while opcion != 5:
    print("\n1. Reservar turno \n2. Cancelar turno (por nombre) \n3. Ver agenda del día \n4. Ver resumen general \n5. Cerrar sistema")
     
    opcion_str = input("Seleccione una opción: ")
     
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue
    opcion = int(opcion_str)

    if opcion < 1 or opcion > 5:
        print("Fuera de rango, elija una opción válida.")
        continue

    if opcion == 1:
        dia = input("Elegir día: 1 = Lunes, 2 = Martes: ")
        while dia not in ["1", "2"]:
            dia = input("Elegir día: 1 = Lunes, 2 = Martes: ")
        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Ingrese solo letras para el nombre del paciente: ")
     
        if dia == "1":
            if paciente in [lunes1, lunes2, lunes3, lunes4]:
                print(f"El paciente {paciente} ya tiene turno ese día.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno agendado.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno agendado.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno agendado.")
            elif lunes4 == "":
                lunes4 = paciente 
                print("Turno agendado.")
            else:
                print("No hay turnos disponibles en Lunes.")                   
        else:
            if paciente in [martes1, martes2, martes3]:
                print("Error: paciente ya tiene turno ese día.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno agendado.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno agendado.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno agendado.")
            else:
                print("No hay turnos disponibles en Martes.")                       

    elif opcion == 2:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while dia not in ["1", "2"]:
            dia = input("Error. Ingrese 1 para Lunes o 2 para Martes: ")
        paciente = input("Ingrese nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            paciente = input("Error. Ingrese solo letras: ")

        if dia == "1":
            if paciente == lunes1: lunes1 = ""
            elif paciente == lunes2: lunes2 = ""
            elif paciente == lunes3: lunes3 = ""
            elif paciente == lunes4: lunes4 = ""
            else: print("Paciente no encontrado en Lunes.")
        else:
            if paciente == martes1: martes1 = ""
            elif paciente == martes2: martes2 = ""
            elif paciente == martes3: martes3 = ""
            else: print("Paciente no encontrado en Martes.")

    elif opcion == 3:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while dia not in ["1", "2"]:
            dia = input("Error. Ingrese 1 para Lunes o 2 para Martes: ")

        if dia == "1":
            print(f"Lunes - Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Lunes - Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Lunes - Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Lunes - Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"Martes - Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Martes - Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Martes - Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == 4:
        ocupados_lunes = (1 if lunes1 != "" else 0) + (1 if lunes2 != "" else 0) + (1 if lunes3 != "" else 0) + (1 if lunes4 != "" else 0)
        ocupados_martes = (1 if martes1 != "" else 0) + (1 if martes2 != "" else 0) + (1 if martes3 != "" else 0)
        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print(f"Lunes: {ocupados_lunes} ocupados, {libres_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {libres_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Lunes tiene más turnos ocupados.")
        elif ocupados_martes > ocupados_lunes:
            print("Martes tiene más turnos ocupados.")
        else:
            print("Empate en cantidad de turnos ocupados.")

    elif opcion == 5:
        print("Sesión finalizada.")