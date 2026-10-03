clientes = []
while True:
    print("Menu")
    print("1.Agregar cliente")
    print("2.Mostrar clientes")
    print("3.Salir")
    opcion = input("Elija una opcion:")
    if opcion == "1":
        while True:
            cliente = input("Agregar cliente:").capitalize()
            clientes.append(cliente)
            while True:
                agregar = input("Desea agregar otro cliente?(s/n)")
                if agregar == "s":
                    break
                elif agregar == "n":
                    break
                else:
                    print("Caracter incorrecto.")
                    continue
            if agregar == "n":
                break
    elif opcion == "2":
        while True:
    #USamos lista for
            for i in range(len(clientes)):
                if clientes[i] == "":
                    print(f"Cliente {i + 1}: [ERROR] Nombre no valido")
                else:
                    print(f"Cliente {i + 1}: {clientes[i]}")
            input("Presione enter para volver al menu:")    
            break    

    elif opcion =="3":
        break
    else:
        print("Caracter incorrecto:")