import sqlite3

def init_db():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    # Creamos la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            cantidad INTEGER DEFAULT 0,
            precio REAL
        )
    ''')
    conn.commit()
    conn.close()

def agregar_producto(nombre, categoria, cantidad, precio):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)', 
                   (nombre, categoria, cantidad, precio))
    conn.commit()
    conn.close()
    print(f"✅ Producto '{nombre}' agregado con éxito.")

def consultar_stock():
    conn = sqlite3.connect('inventario.db')
    df_query = "SELECT * FROM productos"
    cursor = conn.cursor()
    cursor.execute(df_query)
    productos = cursor.fetchall()
    conn.close()
    return productos
