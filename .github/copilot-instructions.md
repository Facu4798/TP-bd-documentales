# Instrucciones para el trabajo práctico de bases de datos documentales

Toda la consigna se encuentra en el archivo `README.md`. El objetivo de este archivo es proporcionar contexto e instrucciones adicionales para el trabajo práctico


# Rol de github copilot
El rol de github copilot es asistir a los estudiantes en la implementación del trabajo práctico, proporcionando sugerencias de código, planeando arquitecturas, y ayudando a resolver problemas técnicos relacionados con MongoDB, Redis y la integración con Python. Copilot puede ser utilizado para generar fragmentos de código, explicar conceptos, y ofrecer recomendaciones sobre mejores prácticas en el diseño de sistemas NoSQL de alto rendimiento.

# ubicación de los archivos
- `README.md`: Contiene la consigna completa del trabajo práctico, incluyendo los requisitos y
- Todos los archivos relacionados con la implementación, como scripts de inicialización, código de aplicación, y documentación adicional, deben ser organizados en el repositorio siguiendo  esta estructura:
```
/src
  /python
    - main.py # orquestación de todos los procesos
    /functions
      - mongodb_operations.py # funciones relacionadas con MongoDB
      - redis_operations.py # funciones relacionadas con Redis
    /api
      - api.py # si llega a ser necesario implementar alguna api con flask
  /frontend # si llega a ser necesario implementar alguna interfaz de usuario
/data # cualquier dato que se necesite guardar
/docs # documentación adicional, diagramas, etc.
```

# Recursos tecnologicos disponibles
- Github codespaces
- Una instancia de databricks free edition