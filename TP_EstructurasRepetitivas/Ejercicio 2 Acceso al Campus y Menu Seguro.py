#Ejercicio 2  — “Acceso al Campus y Menú Seguro” 

usuarioCorrecto = "alumno"
claveCorrecta = "python123"

intentos = 0
maxIntentos = 3
acceso = False

while intentos < maxIntentos and not acceso:
    print(f"Intento {intentos+1}/{maxIntentos}")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuarioCorrecto and clave == claveCorrecta:
        print("Acceso concedido.")
        acceso = True
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    opcion = ""
    while opcion != "4":
        print("\n1. Estado de inscripcion  \n2. Cambiar clave  \n3. Mensaje motivacional  \n4. Salir")
        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == "1":
            print("Inscripto")
        elif opcion == "2":
            nuevaClave = input("Ingrese nueva clave con minimo 6 caracteres: ")
            while len(nuevaClave) < 6:
                nuevaClave = input("Error. La clave debe tener al menos 6 caracteres: ")
            confirmacion = input("Confirme la nueva clave: ")
            if nuevaClave == confirmacion:
                claveCorrecta = nuevaClave
                print("Clave cambiada exitosamente.")
            else:
                print("Error: las claves no coinciden, por favor intente nuevamente.")
        elif opcion == "3":
            print("Vas muy bien, segui asi!")
        elif opcion == "4":
            print("Sesión finalizada.")