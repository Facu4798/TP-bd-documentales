# Propuestas de Dominio — TP Integrador

Cada propuesta justifica el uso de **MongoDB** (persistencia estructural) y **Redis** (capa de velocidad), y cubre las cuatro fases del trabajo.

---

## 1. Plataforma de Subastas en Tiempo Real

**Descripción del negocio:** Sitio donde usuarios publican ítems para subastar. Otros usuarios pujan durante un tiempo limitado; al vencer el tiempo, el mayor postor gana y se registra la venta.

**MongoDB**
- Colecciones: `items` (con historial de pujas embebido hasta cierto límite), `usuarios`, `ventas`, `categorias`
- Embedding vs Referencing: últimas 10 pujas embebidas en el ítem (lectura rápida del estado actual), historial completo referenciado en colección separada, datos del vendedor referenciados
- Transacción ACID: cerrar subasta + registrar venta + desactivar ítem + actualizar balance del vendedor (no puede haber dos ganadores)

**Redis**
- `Sorted Set` para el ranking de pujas activas de una subasta (score = monto, O(log n) para insertar y leer el máximo)
- `Hash` por sesión de usuario autenticado
- `String` con TTL como temporizador de la subasta (expiración dispara invalidación de caché)
- TTL en caché del estado actual del ítem para reducir lecturas a MongoDB durante picos de actividad

**Aggregation pipelines**
1. Ítems con mayor cantidad de pujas por categoría en los últimos 30 días
2. Usuarios con mayor volumen vendido (monto total de ventas cerradas)
3. Distribución de precios finales vs precio base (ratio de revalorización por categoría)

**Sharding natural:** `item_id` como shard key en la colección de pujas — distribuye carga por ítem activo

---

## 2. Sistema de Gestión de Flota de Monopatines Compartidos

**Descripción del negocio:** Servicio urbano de monopatines eléctricos. Usuarios desbloquean un monopatín, lo usan y lo devuelven en cualquier estación. El sistema registra viajes, cobra por minuto y gestiona la disponibilidad de la flota.

**MongoDB**
- Colecciones: `monopatines` (estado, batería, estación actual), `estaciones`, `usuarios`, `viajes`
- Embedding vs Referencing: coordenadas GPS y estado embebidos en `monopatines` (se actualizan frecuentemente y se leen juntos), historial de viajes referenciado (crece sin límite), métodos de pago referenciados en usuario
- Transacción ACID: iniciar viaje + marcar monopatín como "en uso" + reservar fondos del usuario (evita que dos usuarios desbloqueen el mismo vehículo)

**Redis**
- `Hash` por monopatín activo en viaje (usuario, timestamp de inicio, última coordenada)
- `Sorted Set` de monopatines disponibles por estación (score = nivel de batería, para recomendar el más cargado)
- `String` con TTL para bloqueo de desbloqueo (ventana de 30 s para confirmar el scan del QR)
- TTL en caché de disponibilidad por zona (se invalida cuando un monopatín se mueve de estación)

**Aggregation pipelines**
1. Duración y distancia promedio de viaje por franja horaria y día de semana
2. Estaciones con mayor rotación (monopatines que entran y salen por hora)
3. Usuarios con viajes interrumpidos o monopatines no devueltos (detección de incidencias)

**Sharding natural:** `estacion_id` como shard key — agrupa consultas de disponibilidad por zona geográfica

---

## 3. Red de Intercambio de Habilidades (Skill Swap)

**Descripción del negocio:** Plataforma donde usuarios ofrecen enseñar algo que saben (idiomas, programación, música, cocina) a cambio de aprender algo que otro ofrece. El sistema matchea solicitudes y gestiona sesiones de intercambio.

**MongoDB**
- Colecciones: `usuarios` (con arrays de habilidades que ofrecen y buscan), `intercambios`, `sesiones`, `valoraciones`
- Embedding vs Referencing: habilidades embebidas en usuario (pocas, se leen siempre juntas con el perfil), sesiones referenciadas en intercambio (pueden crecer), valoraciones referenciadas
- Transacción ACID: confirmar match + crear intercambio + remover ambas solicitudes del pool de búsqueda (evita que un usuario sea matcheado dos veces simultáneamente)

**Redis**
- `Sorted Set` de solicitudes activas por habilidad buscada (score = timestamp, para matchear por antigüedad)
- `Hash` por sesión de usuario (token, habilidades cargadas en caché)
- `List` de notificaciones pendientes por usuario (nuevo match, sesión próxima)
- TTL en caché del perfil público de usuario (se invalida si actualiza sus habilidades)

**Aggregation pipelines**
1. Habilidades más ofrecidas vs más buscadas (análisis de oferta/demanda)
2. Tasa de conversión de solicitud a intercambio completado por categoría de habilidad
3. Usuarios más activos rankeados por sesiones completadas y puntuación promedio recibida

**Sharding natural:** hash de `usuario_id` — distribuye uniformemente sin hotspots por habilidad popular

---

## 4. Gestor de Torneos de Videojuegos (Esports Amateur)

**Descripción del negocio:** Plataforma para organizar torneos de videojuegos en formato eliminatorio o de grupos. Equipos se inscriben, se generan brackets automáticamente, se reportan resultados y se lleva un ranking histórico.

**MongoDB**
- Colecciones: `torneos` (con fases y bracket embebidos), `equipos`, `jugadores`, `resultados`
- Embedding vs Referencing: fases y partidos del bracket embebidos en el torneo (se consultan juntos siempre), jugadores referenciados desde equipo (existen independientemente), historial de resultados referenciado
- Transacción ACID: reportar resultado de partido + avanzar al ganador en el bracket + eliminar al perdedor (el bracket no puede quedar en estado inconsistente)

**Redis**
- `Sorted Set` para el ranking global de equipos por puntos ELO (actualización en tiempo real tras cada resultado)
- `Hash` por torneo activo (estado actual, partidos pendientes de la ronda, conteo de reportes)
- `List` como cola de resultados pendientes de validación por el organizador
- TTL en caché del bracket completo del torneo (se invalida al avanzar una ronda)

**Aggregation pipelines**
1. Win rate por equipo desglosado por videojuego y modalidad
2. Torneos con mayor participación y tasa de abandono (equipos que no se presentaron)
3. Jugadores con mejor rendimiento individual dentro de equipos que fueron eliminados en primera ronda

**Sharding natural:** `torneo_id` como shard key en resultados — cada torneo es independiente y concentra sus propias lecturas

---

## Comparativa

| Criterio | Subastas | Monopatines | Skill Swap | Torneos |
|---|---|---|---|---|
| Complejidad de esquema | Media | Media | Media | Media |
| Transacción ACID obvia | **Muy clara** | **Muy clara** | Clara | **Muy clara** |
| Uso de Redis natural | **Muy alto** | **Muy alto** | Alto | Alto |
| Originalidad | Alta | Alta | **Muy alta** | Alta |
| Dificultad de seed data | Fácil | Fácil | Fácil | Media |

**Recomendación:** **Subastas** es el más completo técnicamente (TTL como lógica de negocio, Sorted Set como estructura central, transacción crítica). **Monopatines** tiene el modelo de datos más interesante para justificar sharding geográfico. **Torneos** es el más divertido de implementar y defender.
