1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar migraciones y crear superusuario:

```bash
python manage.py migrate
python manage.py createsuperuser
```
5. Iniciar servidor de desarrollo:

```bash
python manage.py runserver

Abrir `http://127.0.0.1:8000/` para el sitio público y `http://127.0.0.1:8000/admin/` para el panel de administración.

Archivos importantes:
- `cafeteria/models.py`: modelos usados (Product, Car, Event, Branch, Comment).
- `cafeteria/admin.py`: registro de modelos en el administrador.
- `templates/cafeteria/`: plantillas HTML públicas.
- `static/`: CSS e imágenes.
