productos=[]
while True:
    print("-----Menu----")
    print(f" 1. Gestionar productos\n 2. Registrar una venta\n 3. Consultar stock\n 4. Gestionar caja\n 5. Salir")
    opcion=input("Elija una opcion: ")
    if opcion=="1":
        print("Gestionar productos")
        for i in range(len(productos)):

            print(f"Producto:{productos[i][0]}|Categoria:{productos[i][1]}|Precio:${productos[i][2]}|Cantidad disponible:{productos[i][3]}")
        while True:
            print("Menu")
            print(f"1.Agregar producto\n2.Borrar producto\n3.Editar producto\n4.Volver al menu")
            opcion_productos=input("Elija una opcion: ")

            if opcion_productos=="1":
                print("Agregar producto")
                while True:
                    nombre=input("Ingrese nombre del producto: ").capitalize()
                    categoria=input("Ingrese categoria del producto: ").capitalize()
                    while True:
                        try:
                            precio=float(input("Ingrese el precio del producto:$ "))
                        except ValueError:
                            print("Debe ingresar numero.")
                            continue
                        if precio >0:
                            break
                        else:
                            print("El precio debe ser mayor a 0.")
                            continue
                    while True:
                        try:
                            cantidad=int(input("Ingrese la cantidad del producto: "))
                        except ValueError:
                            print("Debe ingresar un numeros entero.")
                            continue
                        if cantidad >0:
                            break
                        else:
                            print("La cantidad debe ser mayor a 0.")
                            continue
                    productos.append([nombre, categoria, precio, cantidad])
                    print("Producto añadido correctamente.")
                    while True:
                        volver_agregar=input("Desea agregar otro producto?(s/n)").lower()
                        if volver_agregar=="s":
                            break
                        elif volver_agregar=="n":
                            break
                        else:
                            print("Caracter incorrecto.")
                    if volver_agregar=="n":
                        break

            elif opcion_productos=="2":
                print("Borrar producto")
                if len (productos) == 0:
                    print("No hay productos en la lista.")
                else:
                    for i in range(len(productos)):
                        print( f"{i + 1}Producto:{productos[i][0]}|Categoria:{productos[i][1]}|Precio:${productos[i][2]}|Cantidad disponible:{productos[i][3]}")
                    try:
                        producto_a_borrar=int(input("Que producto quiere eliminar: "))
                        if producto_a_borrar >=1 and producto_a_borrar <= len(productos):
                            productos.pop(producto_a_borrar - 1)
                            print("Producto eliminado")
                        else:
                            print("Numero de producto incorrecto.")
                    except ValueError:
                        print("Numero incorrecto")

            elif opcion_productos=="3":
                print("Editar producto")
                if len(productos) == 0:
                    print("No hay productos en la lista.")
                else:
                    for i in range(len(productos)):
                        print(f"{i +1}Producto:{productos[i][0]}|Categoria:{productos[i][1]}|Precio:${productos[i][2]}|Cantidad disponible:{productos[i][3]}")
                    try:
                        producto_a_editar=int(input("Que producto quiere editar: "))
                        if producto_a_editar >= 1 and producto_a_editar <= len(productos):
                            nuevo_nombre=input("Ingrese nuevo nombre: ")
                            nueva_categoria=input("Ingrese nueva categoria: ")
                            while True:
                                try:
                                    nuevo_precio=float(input("Ingrese nuevo precio: "))
                                    if nuevo_precio >0:
                                        print("Precio modificado.")
                                        break
                                    else:
                                        print("El precio debe ser mayor a 0.")
                                        continue
                                except ValueError:
                                    print("Debe ingresar un numero")
                            while True:
                                try:
                                    nueva_cantidad_disponible=int(input("Ingrese nueva cantidad disponible: "))
                                    if nueva_cantidad_disponible >0:
                                        print("Nueva cantidad modificada.")
                                        break
                                    else:
                                        print("La cantidad debe ser mayor a 0")
                                        continue
                                except ValueError:
                                    print("Debe ingresar un numero entero.")
                            productos[producto_a_editar - 1][0]=nuevo_nombre
                            productos[producto_a_editar - 1][1]=nueva_categoria 
                            productos[producto_a_editar - 1][2]=nuevo_precio 
                            productos[producto_a_editar - 1][3]=nueva_cantidad_disponible
                            print("Producto modificado correctamente.")
                        else:
                            print("Numero de producto incorrecto.")
                    except ValueError:
                       print("Debe ingresar un numero del indice.")
            elif opcion_productos=="4":
                break
            else:
                print("Caracter incorrecto.")
    elif opcion=="2":
        print("Registrar una venta")
    elif opcion=="3":
        print("Consultar stock")
    elif opcion=="4":
        print("Gestionar caja")
    elif opcion == "5":
        print("Saliendo del sistema")
        break
    else:
        print("Caracter incorrecto.")