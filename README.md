# 📦 Inventory Management System (SQL + Python)

Sistema de gestión de inventarios profesional desarrollado en Python utilizando **SQLite** como motor de base de datos relacional. 

## 🎯 Objetivo
Demostrar el manejo de operaciones **CRUD** (Create, Read, Update, Delete) y la persistencia de datos local, fundamental para aplicaciones de gestión empresarial.

## 🛠️ Características Técnicas
* **Motor de DB:** SQLite3 (Sin dependencias externas para facilitar la portabilidad).
* **Arquitectura:** Separación de lógica de datos (`database_manager.py`) y lógica de negocio (`main.py`).
* **Integridad de Datos:** Uso de tipos de datos estrictos y Primary Keys autoincrementales.

## 🚀 Cómo probarlo
1. Ejecuta el archivo principal: `python main.py`.
2. El sistema creará automáticamente el archivo `inventario.db` si no existe.
3. Interactúa con el menú para gestionar tus productos.
