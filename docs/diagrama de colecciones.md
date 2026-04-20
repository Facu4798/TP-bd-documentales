# Listado de colecciones

# Usuarios
Muestra los datos de los usuarios registrados en el sistema
```json
{
    "_objectId": "ObjectId('64a9c8e5f1d2c3b4a5e6f7g')",
    "nombre": "Juan Pérez",
    "email": "juanperez@gmail.com",
    "proyectos": [
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7h')",
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7i')" 
    ],
    "tareasAsignadas": [
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7j')",
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7k')" 
    ]
}
```

# Proyectos
Muestra los datos de los proyectos registrados en el sistema
```json
{
    "_objectId": "ObjectId('64a9c8e5f1d2c3b4a5e6f7h')",
    "nombre": "Proyecto Alpha",
    "descripcion": "Desarrollo de una aplicación web para gestión de tareas",
    "tareas": [
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7j')",
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7k')" 
    ]
}

# Tareas
Muestra los datos de las tareas registradas en el sistema
```json
{
    "_objectId": "ObjectId('64a9c8e5f1d2c3b4a5e6f7j')",
    "titulo": "Diseñar la interfaz de usuario",
    "descripcion": "Crear wireframes y prototipos para la aplicación web",
    "storyPoints": 5,
    "horas": 20,
    "estado": "En progreso",
    "asignadoA": "ObjectId('64a9c8e5f1d2c3b4a5e6f7g')",
    "objeto_padre": "ObjectId('64a9c8e5f1d2c3b4a5e6f7h')",
    "objeto_hijo": [
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7l')",
        "ObjectId('64a9c8e5f1d2c3b4a5e6f7m')" 
    ]
}
```
