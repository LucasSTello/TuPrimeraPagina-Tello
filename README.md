# Yamaha Motocross Blog

Proyecto web desarrollado con **Django** cumpliendo con el patrón MVT (Model-View-Template).
Este proyecto es un blog temático sobre motos de motocross Yamaha, donde se pueden cargar modelos de motos, pilotos y eventos de carreras.

## Tecnologías usadas
- Python 3
- Django 5.x
- Bootstrap 5 (vía CDN para diseño responsivo)
- SQLite3 (Base de datos por defecto de Django)

## Requisitos Previos
Tener Python instalado en el sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Instrucciones de instalación paso a paso

1. **Abrir una terminal** en la carpeta principal del proyecto (donde se encuentra `manage.py`).

2. **Crear un entorno virtual (Recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar Django (o las dependencias):**
   ```bash
   pip install -r requirements.txt
   ```
   *(Si no funciona, simplemente usa: `pip install django`)*

5. **Aplicar las migraciones (Crear la base de datos):**
   ```bash
   python manage.py makemigrations motocross
   python manage.py migrate
   ```

6. **Crear un superusuario (Administrador):**
   ```bash
   python manage.py createsuperuser
   ```
   *(Sigue las instrucciones en la consola para elegir un usuario, email y contraseña).*

7. **Ejecutar el servidor local:**
   ```bash
   python manage.py runserver
   ```
   
8. **Abrir el navegador** y visitar `http://127.0.0.1:8000/`.

## Orden recomendado para probar

1. **Crear motos:** Ve a la sección "Motos" en el menú, haz clic en "Agregar Nueva Moto" y llena el formulario (ej: Yamaha YZ250F).
2. **Crear pilotos:** Ve a "Pilotos", haz clic en "Agregar Nuevo Piloto" y asócialo a la moto que creaste en el paso anterior.
3. **Crear carreras:** Ve a "Carreras", haz clic en "Agregar Nueva Carrera" y asigna un piloto ganador.
4. **Usar el buscador:** En la barra de navegación (arriba a la derecha), ingresa el nombre o modelo de una moto que hayas creado y presiona "Buscar".
5. **Panel de Admin:** Puedes visitar `http://127.0.0.1:8000/admin/` e iniciar sesión con el superusuario para gestionar todos los datos desde el panel de administración de Django.
