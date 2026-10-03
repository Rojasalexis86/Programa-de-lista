while True:
     
 print(".....Mi programa.....")  
 print("1. Saludar") 
 print("2. Hacer una cuenta")
 print("3. Decir tu edad")
 print("4. Salir")

 opcion = input("Elegi una opcion:")

 if opcion =="1":
    print("Que onda papa, todo bien?")

 elif opcion =="2":
    numero1 = float(input("Ingresa el  primer numero:"))
    numero2 = float(input("Igresa el segundo numero:"))

    operacion = input("¿Que operacion queres hacer? (+,-,*,/): ")

    if operacion == "+":
        resultado = numero1 + numero2
        print("El resultado es:", resultado)
    elif operacion == "*":
            resultado = numero1 * numero2
            print("El resultado es:", resultado)   
    elif operacion == "/":
            if numero2 == 0:
                 print("No se puede dividir por 0.")
            else:
                 resultado = numero1 / numero2
                 print("El resultado es:", resultado)
                 
    elif operacion == "-":
            resultado = numero1 - numero2
            print("El resultado es:", resultado)
    else:
        print("operacion no valida")    

 elif opcion =="3":
    nombre = input("¿Como te llamas?")
    edad = int(input("¿Cuantos años tenes?"))

    anio_actual = 2026
    anio_nacimiento = anio_actual - edad

    print("Hola", nombre, "tenes", edad, "años. Full violado")
    print ("Aproximadamente naciste en", anio_nacimiento)

 elif opcion =="4":
    print("Chau chamigo")
    break

 else:
    print("Opcion no valida man.")

