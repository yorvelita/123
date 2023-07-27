print("bienvenido,espero tengas una experiencia agradable en mi red")
print ('''
### ###  ####              #### ##    ####    ## ##   ### ##   ### ###
 ##  ##   ##               # ## ##     ##    ##   ##   ##  ##   ##  ##
 ##       ##                 ##        ##    ##        ##  ##   ##
 ## ##    ##                 ##        ##    ##  ###   ## ##    ## ##
 ##       ##                 ##        ##    ##   ##   ## ##    ##
 ##  ##   ##  ##             ##        ##    ##   ##   ##  ##   ##  ##
### ###  ### ###            ####      ####    ## ##   #### ##  ### ###
''')


nombre = input("como es tu nombre ")
print()
print("Hola ", nombre, ", bienvenido a EL TIGRE")
print()


agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2023-agno-1
print()



num_amigos = int(input("cuantos amigos tienes "))


print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con EL TIGRE")
print()

opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    
    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "años")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    
    elif opcion == 4:
        
        nombre = input("Para empezar, dime como te llamas. ")
        print()
        print("Hola ", nombre, ", bienvenido a Mi Red")
        print()

        
        agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
        edad = 2023-agno-1
        print()


        
        num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
       
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "años")
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()

    
    elif opcion == 0:
        print("Has decidido salir.")

    
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red (EL TIGRE). ¡Hasta pronto!")
print()

