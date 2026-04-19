<p style="text-align:center;font-size:48px">Trabajo Práctico Integrador</p>

<p style="text-align:center;font-size:30px"> Diseño de 
Sistemas NoSQL de Alto Rendimiento</p>

# 1. El Desafío
Su grupo deberá diseñar, prototipar y defender la persistencia y el caching de una plataforma moderna. El objetivo es construir un sistema que no solo sea funcional, sino también escalable y técnicamente 
robusto, justificando cada decisión arquitectónica.

## Requisitos del Dominio
El escenario elegido por el grupo debe ser lo suficientemente complejo para justificar el uso de ambas 
tecnologías:
- **MongoDB**: Para el almacenamiento estructural, jerarquías de documentos y persistencia de 
larga duración.
- **Redis**: Como capa de velocidad para datos efímeros, gestión de estados o caché de alta 
frecuencia.

# 2. Estructura y Requisitos Técnicos

## Fase 1: Modelado y Fundamentos
- **Definición de Dominio**: Un breve documento que describa el caso de negocio.
- **Diseño de Esquema**: Presentar el diagrama de colecciones.
- **Decisiones de Modelado**: Documentar explícitamente al menos tres casos de Embedding vs. 
Referencing, justificando la elección en base a patrones de lectura/escritura y límites de tamaño 
de documentos.
- **Carga de Datos**: Script de inicialización (Seed) para poblar el sistema.

## Fase 2: Integración y Procesamiento Avanzado
- **Capa de Aplicación**: Conexión obligatoria mediante el driver oficial de Python (PyMongo).
- **Aggregation Framework**: Implementar al menos 3 pipelines complejos (ej: reportes, métricas 
en tiempo real o transformaciones de datos anidados).
- **Optimización**: Aplicar estrategias de indexación compuestas siguiendo la regla ESR (Equality, 
Sort, Range) para las consultas críticas.

## Fase 3: Integridad y Escalabilidad (Nuevo Requisito)
- **Transacciones Multi-documento**: Identificar un proceso de negocio que requiera atomicidad 
(ej: una transferencia, un pedido con actualización de stock, un sistema de reservas). 
Implementar este flujo utilizando sesiones y transacciones ACID en MongoDB para garantizar 
la consistencia.
- **Análisis CAP**: Justificar el comportamiento del sistema ante una partición de red (Prioridad CP 
o AP).
- **Estrategia de Sharding**: Proponer una Shard Key lógica que evite "hotspots" y permita el 
escalamiento horizontal.
## Fase 4: Aceleración con Redis
- **Estructuras de Datos**: Uso obligatorio de al menos dos estructuras distintas a Strings (ej: 
    Hashes para sesiones, Sorted Sets para rankings, o Lists para colas de mensajes).
- **Gestión de Caché**: Implementar políticas de expiración (TTL) y una estrategia de invalidación 
coherente con el negocio.
