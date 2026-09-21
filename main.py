from servicios.restaurante import Restaurante

restaurante = Restaurante()

while True:

    print("\n===== RESTAURANTE =====")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Registrar venta")
    print("4. Listar productos")
    print("5. Listar usuarios")
    print("6. Ver ventas de un usuario")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        contrasena = input("Contraseña: ")

        try:

            restaurante.registrar_usuario(
                identificacion,
                nombre,
                contrasena
            )

            print("Usuario registrado correctamente")

        except Exception as e:

            print("Error:", e)

    elif opcion == "2":

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        try:

            restaurante.registrar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )

            print("Producto registrado correctamente")

        except Exception as e:

            print("Error:", e)

    elif opcion == "3":

        usuario_id = input("ID Usuario: ")
        producto_codigo = input("Código Producto: ")
        cantidad = int(input("Cantidad: "))

        try:

            restaurante.registrar_venta(
                usuario_id,
                producto_codigo,
                cantidad
            )

            print("Venta registrada correctamente")

        except Exception as e:

            print("Error:", e)

    elif opcion == "4":

        print("\n=== PRODUCTOS ===")

        for producto in restaurante.listar_productos():

            print(producto)

    elif opcion == "5":

        print("\n=== USUARIOS ===")

        for usuario in restaurante.listar_usuarios():

            print(usuario)

    elif opcion == "6":

        usuario_id = input(
            "Ingrese ID del usuario: "
        )

        ventas = restaurante.obtener_ventas_usuario(
            usuario_id
        )

        print("\n=== VENTAS ===")

        if not ventas:

            print("No existen ventas")

        else:

            for venta in ventas:

                print(venta)

    elif opcion == "7":

        print("Programa finalizado")
        break

    else:

        print("Opción inválida")