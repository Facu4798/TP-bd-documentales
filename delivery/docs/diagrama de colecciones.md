<p style="text-align:center;font-size:48px">Diagrama de Colecciones</p>

# Usuarios

```js
{
    "_id": ObjectId,
    "nombre": String,
    "email": String,
    "direccion": String,
    "telefono": String,
    "pedidos": [ObjectId] // Referencia a pedidos
}
```

# Restaurantes

```js
{
    "_id": ObjectId,
    "nombre": String,
    "direccion": String,
    "telefono": String,
    "menu": [ // Embedding del menú
        {
            "nombre_plato": String,
            "descripcion": String,
            "precio": Number
        }
    ],
    "promedio_valoracion": Number // Campo para almacenar el promedio de valoraciones
}
```

# Conductores

```js
{
    "_id": ObjectId,
    "nombre": String,
    "telefono": String,
    "vehiculo": String,
    "pedidos_asignados": [ObjectId] // Referencia a pedidos asignados
}
```

# Pedidos

```js
{
    "_id": ObjectId,
    "usuario_id": ObjectId, // Referencia al usuario
    "restaurante_id": ObjectId, // Referencia al restaurante
    "conductor_id": ObjectId, // Referencia al conductor (puede ser null hasta que se asigne)
    "platos": [ // Detalles de los platos pedidos
        {
            "nombre_plato": String,
            "cantidad": Number,
            "precio_unitario": Number
        }
    ],
    "total": Number,
    "estado": String, // Ej: "pendiente", "en preparación", "en camino", "entregado"
    "valoracion_restaurante": Number, // Valoración del restaurante por parte del usuario
    "valoracion_conductor": Number // Valoración del conductor por parte del usuario
}
```

# Valoraciones

```js
{
    "_id": ObjectId,
    "pedido_id": ObjectId, // Referencia al pedido
    "restaurante_id": ObjectId, // Referencia al restaurante
    "conductor_id": ObjectId, // Referencia al conductor
    "usuario_id": ObjectId, // Referencia al usuario
    "valoracion_restaurante": Number,
    "valoracion_conductor": Number,
}
```

