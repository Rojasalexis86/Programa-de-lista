productos = []
while True:
    print("**********************")
    print("        MENU")
    print("**********************")
    print(f" 1.Agregar producto\n 2.Borrar producto\n 3.Ver productos\n 4.Buscar producto\n 5.Salir")
    print("**********************")

#Elegir opcion

    while True:
        try:
            opcion = int(input("Ingrese una opcion del 1-5: "))
            break
        except ValueError:
            print("Ingrese un numero del 1-5")

#Agregar prodto

    if opcion == 1:
        while True:
            print("****************")
            print("Agregar producto")
            print("****************")
            while True:
                nombre = input("Nombre del producto: ").capitalize()
                if nombre == "":
                    print("Nombre no puede quedar vacio.")
                    continue
                else:
                    break
            while True:
                categoria = input("Categoria: ").capitalize()
                if categoria == "":
                    print("Categoria no puede quedar vacio.")
                    continue
                else:
                    break
            while True:
                try:
                    precio = int(input("Ingrese el precio del producto: "))
                    print("Precio añadido correctamente.")
                    break
                except ValueError:
                    print("Debe ingresar un numero.")
            producto = [nombre, categoria, precio]
            print("Producto añadido correctamente.")
            productos.append(producto)
            while True:
                agregar=input("Desea agregar otro producto?(s/n)")
                if agregar == "s":
                    break
                elif agregar == "n":
                    break
                else:
                    print("Caracter incorrecto.")
                    continue
            if agregar == "n":
                break

#Borrar producto

    elif opcion == 2:
        while True:
            print("***************")
            print("Borrar producto")
            print("***************")
            try:
                borrar = int(input("Que producto desea eliminar:"))
                if borrar >= 1 and borrar <= len(productos):
                    productos.pop(borrar - 1)
                    print("Producrto elimniado.")
                else:
                    print("Numero de producto incorrecto.")
            except ValueError:
                print("Numero incorrecto.")
            while True:
                borrar_otro=input("Desea borrar otro producto?(s/n)")
                if borrar_otro == "s":
                    break
                elif borrar_otro == "n":
                    break
                else:
                    print("Caracter incorrecto.")
                    continue
            if borrar_otro=="n":
                break

#Mostrar productos

    elif opcion == 3:
            print("******************")
            print("Lista de productos")
            print("******************")
            if len(productos) > 0:
                for i in range(len(productos)):
                    print(f"{i + 1}.Producto: {productos[i][0]} | Categoria: {productos[i][1]} | Precio: ${productos[i][2]}")
            else:
                print("No hay productos en la lista.")
            print("******************")

#BUSCAR PRODUCTO

    elif opcion == 4:
        while True:
            print("*********************")
            print("Buscador de productos")
            print("*********************")

            producto_a_buscar = input("Que producto esta buscandi?: ").capitalize()
            encontado = False
            for producto in productos:
                if producto_a_buscar == producto[0]:
                    print("Producto encontrado:")
                    print(f"producto: {producto[0]} | categoria: {producto[1]} | Precio: ${producto[2]}")
                    encontado = True
            if encontado == False:
                print("Producto inexistente.")
            while True:
                volver_a_buscar=input("Desea buscar otro producto?(s/n): ")
                if volver_a_buscar == "s":
                    break
                elif volver_a_buscar == "n":
                    break
                else:
                    print("Caracter incorrecto.")
            if volver_a_buscar == "n":
                break


#Salir del programa
    elif opcion == 5:
        break

    else:
        print("Caracter incorrecto, elija un numero del 1 al 5.")

            
