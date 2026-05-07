# App de delivery

Esta app de delivery conecta restaurantes con clientes para pedidos de comida a domicilio. Los usuarios pueden buscar restaurantes, ver menús, realizar pedidos y seguir el estado de su entrega en tiempo real.

## MongoDB
- Colecciones: `usuarios`, `restaurantes`, `pedidos`, `repartidores`, `valoraciones`
- Embedding vs Referencing: 
    - Menús embebidos en restaurantes (se consultan siempre juntos)
    - Pedidos referenciados desde usuario y restaurante (pueden crecer con el tiempo)
    - Repartidores referenciados desde pedidos (pueden existir independientemente)
    - Valoración embedded en pedido (va a haber un pipeline de promedio para embeber el promedio al restaurante/repartidor)
- Transacción ACID: confirmar pedido + asignar repartidor + hacer el cobro (evita que un pedido quede sin repartidor o sin cobro)


## Pipelines complejos:
1. Reporte de ventas por restaurante: Agrupar pedidos por restaurante, sumar total de ventas y contar número de pedidos.
2. Métricas en tiempo real: Contar pedidos activos por restaurante y repartidor.
3. Transformación de datos anidados: Calcular el promedio de valoración por restaurante y actualizar el campo `promedio_valoracion` en la colección de restaurantes.

## Redis
- Estructuras de datos:
    - Hashes para sesiones de usuario (almacenar token, tiempo de expiración, etc.)
    - Sorted Sets para rankings de restaurantes (ordenados por promedio de valoración)
- Gestión de caché:
    - TTL de 10 minutos para sesiones de usuario
    - Invalida el ranking de restaurantes en Redis cada vez que se actualiza el promedio de valoración de un restaurante en MongoDB.