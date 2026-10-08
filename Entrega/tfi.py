#Pre-entrega

productos = []

while True:

    print("*"*40)
    print(f"Sistema de gestion básica de productos \n\n 1. Agregar producto \n 2. Mostrar productos \n 3. Buscar producto \n 4. Eliminar producto \n 5. Salir")
    print("*"*40)


    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# 1. Agregar producto
    if opcion == "1":

        while True:
            
            nombre = input("Nombre del producto: ").strip().title()

            tiene_numero = False
            for letra in nombre:
                if letra.isdigit():
                    tiene_numero = True
            
            if nombre == "":
                print("Error: el nombre no puede estar vacío.")
            elif tiene_numero:
                print("Error: el nombre no puede contener números.")
            else:
                break

        while True:
            categoria = input("Categoría: ").strip().title()

            tiene_numero = False
            for letra in categoria:
                if letra.isdigit():
                    tiene_numero = True
            
            if categoria == "":
                print("Error: la categoría no puede estar vacía.")
            elif tiene_numero:
                print("Error: la categoría no puede contener números.")
            else:
                break

        while True:
            precio = input("Precio (sin centavos): ").strip()
            if precio.isdigit():
                if int(precio) <= 0:    
                    print("Error: el precio debe ser mayor que 0.")
                else:
                    precio = int(precio)
                    break
            else:
                print("Error: el precio debe ser un número válido.")


        productos.append([nombre,categoria,precio])

        print("*"*40)
        print(f"Producto agregado correctamente: {nombre} | {categoria} | ${precio}")
        print("*\n\n"*40)        

# 2. Mostrar productos
    elif opcion == "2":
        print("*"*40)
        print("Productos registrados:")
        print("*"*40)

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for indice in range(len(productos)):
                print(f"{indice + 1}: nombre: {productos[indice][0]} | categoría: {productos[indice][1]} | precio: ${productos[indice][2]}")
            print("*" * 40, "\n\n")


# 3. Buscar productos
    elif opcion == "3":
        nombreBuscado = input("Ingrese el nombre del producto a buscar: ").strip().title()
        productoEncontrado = []
        cont = 0

        for indice in range(len(productos)):
            if productos[indice][0] == nombreBuscado:
                cont += 1
                productoEncontrado.append(productos[indice])

        if productoEncontrado == []:
            print("*" * 40)
            print("Producto no encontrado.")
            print("*" * 40, end="\n\n")
        else:
            print("*" * 40)
            print(f"Coincidencias encontradas: {cont}")
            print("*" * 40)
            for indice in range(len(productoEncontrado)):
                producto = productoEncontrado[indice]
                print(f"{indice + 1}. {producto[0]} | {producto[1]} | ${producto[2]}")
            print("*" * 40, end="\n\n")

# 4. Eliminar productos
    elif opcion == "4":
        
        while True:

            productoEliminar = input("Ingrese el numero en la lista para eliminar el producto: ").strip()
        
            if productoEliminar.isdigit() and 1 <= int(productoEliminar) <= len(productos):
                
                productoEliminar = int(productoEliminar)-1
                
                print(f"Producto eliminado: {productos[productoEliminar][0]} | {productos[productoEliminar][1]} | ${productos[productoEliminar][2]}")
                productos.pop(productoEliminar)
                break
                                                   
            else:
                print("Error: debe ingresar un número válido.")    

# 5. Salir
    elif opcion == "5":
        print("Saliendo del sistema de gestión de productos...")
        break
        

