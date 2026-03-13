from database_manager import init_db, agregar_producto, consultar_stock

def menu():
    init_db()
    while True:
        print("\n--- 📦 SISTEMA DE GESTIÓN DE INVENTARIOS ---")
        print("1. Agregar Producto")
        print("2. Ver Inventario Completo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nom = input("Nombre del producto: ")
            cat = input("Categoría: ")
            cant = int(input("Cantidad inicial: "))
            pre = float(input("Precio unitario: "))
            agregar_producto(nom, cat, cant, pre)
        elif opcion == '2':
            print("\nID | Nombre | Categoría | Stock | Precio")
            for p in consultar_stock():
                print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | ${p[4]}")
        elif opcion == '3':
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
