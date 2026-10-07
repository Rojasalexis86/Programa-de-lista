contacos=[]
def agregar_contacto():
    while True:
            nombre=input("Ingrese el nombre del contacto: ").title()
            print("Nombre añadido correctamente.")
            numero=input("Ingrese nombre de telefono: ")
            print("Numero registrado.")
            while True:
                mail=input("Ingrese el mail: ")
                if "@" not in mail:
                        print("Mail incorrecto.")
                else:
                    print("Mail registrado.")
                    break
            contacto=[nombre, numero, mail]
            contacos.append(contacto)
            while True:
                agregar=input("Desea agregar otro contacto?(s/n): ").lower()
                if agregar == "s":
                    break
                elif agregar=="n":
                    break
                else:
                    print("Caracter incorrecto.")
                    continue
            if agregar=="n":
                break
def borrar_contacto():
    while True:
        print("*******************")
        print("  BORRAR CONTACTO")
        print("*******************")
        print("")
        encontrado=False
        contacto_a_borrar=input("Que contacto desea borrar: ").title()
        for contacto in contacos:
            if contacto_a_borrar==contacto[0]:
                contacos.remove(contacto)
                print("Contacto eliminado.")
                encontrado=True
                break
        if encontrado==False:
            print("Contacto inexitente.")
        while True:
            volver_a_borrar=input("Desea eliminar otro contacto?(s/n): ").lower()
            if volver_a_borrar=="s":
                break
            elif volver_a_borrar=="n":
                break
            else:
                print("Caracter incorrecto.")
        if volver_a_borrar=="n":
            break
def ver_contactos():
    print("**********************************************")
    print("             LISTA DE CONTACOS")
    print("**********************************************")
    for contacto in contacos:
        print(f"Nombre:{contacto[0]}|Numero:{contacto[1]}|Mail:{contacto[2]}")
    input("Presione enter para volver al menu...")
def editar_contacto():
    encontrado=False
    contaco_a_editar=input("Que contacto desea editar: ").title()
    for contacto in contacos:
        if contaco_a_editar==contacto[0]:
            nuevo_nombre=input("Ingrese nuevo nombre: ")
            nuevo_numero=input("Ingrese nuevo numero: ")
            nuevo_mail=input("Ingrese nuevo mail: ")
            contacto[0]=nuevo_nombre
            contacto[1]=nuevo_numero
            contacto[2]=nuevo_mail
            encontrado=True
            print("Contacto editado y guardado correctamente.")
    if encontrado==False:
                print("Contacto inexistente.")
#MENU PRINCIPAL
while True:
    print("******************")
    print("       MENU ")
    print("******************")
    print("")
    print("1.gregar contacto.\n2.Borrar contacto\n3.Ver contactos\n4.Editar contacto\n5.Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        agregar_contacto()
    elif opcion==2:
        borrar_contacto()
    elif opcion==3:
        ver_contactos()
    elif opcion==4:
        editar_contacto()
    elif opcion==5:
        break
    else:
        print("Debe ingresar un numero del 1-5")
        continue
    
