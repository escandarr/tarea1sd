
# Tarea 1 - Sistemas Distribuidos

### Benjamin Escandar

Este proyecto tiene como objetivo implementar un sistema distribuido utilizando **Redis** como sistema de cache distribuido, **Docker** para la contenedorización y despliegue, y **Python** para la implementación de los servicios.

## Tecnologías Utilizadas

[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=flat)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white&style=flat)](https://redis.io/)

## Instrucciones de Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/escandarr/tarea1sd.git
cd tarea1sd
```

### 2. Construcción de los contenedores
Asegúrate de tener Docker instalado. Para construir y ejecutar los contenedores, utiliza:

```bash
docker-compose up --build
```

Esto levantará los siguientes servicios:
- **Redis Cluster**: Un cluster de Redis con 3 nodos.
- **API**: Servicio que interactúa con el cluster de Redis.
- **gRPC Service**: Servicio para la comunicación gRPC (por implementar).

### 3. Uso de la API
Una vez que el contenedor de la API esté corriendo, puedes interactuar con él utilizando `curl` o cualquier cliente HTTP.

Ejemplo para agregar un valor en Redis:
```bash
curl -X POST http://localhost:5000/set -H 'Content-Type: application/json' -d '{"key": "test", "value": "123"}'
```

Ejemplo para obtener un valor:
```bash
curl "http://localhost:5000/get?key=test"
```

### 4. Servicios gRPC
El servicio gRPC aún está en desarrollo. Una vez implementado, se podrá utilizar para hacer llamadas remotas al sistema de cache distribuido.
```

esta muy incompleto lo se, lo hice tarde y mi compañero que nisiquiera se como se llama no aporto mucho
