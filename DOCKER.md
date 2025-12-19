# 🐳 Docker Setup para Detector_AI

## 📋 Construcción y Ejecución con Docker

### Opción 1: Usando docker-compose (Recomendado)

```bash
# Construir la imagen
docker-compose build

# Ejecutar el contenedor
docker-compose up

# Ejecutar en modo detached
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

### Opción 2: Usando Docker directamente

```bash
# Construir la imagen
docker build -t detector_ai .

# Ejecutar el contenedor
docker run -it \
  -v $(pwd)/assets:/app/assets \
  -v $(pwd)/runs:/app/runs \
  --name detector_ai \
  detector_ai

# En Windows PowerShell:
docker run -it `
  -v ${PWD}/assets:/app/assets `
  -v ${PWD}/runs:/app/runs `
  --name detector_ai `
  detector_ai

# Ejecutar un comando específico
docker run -it \
  -v $(pwd)/assets:/app/assets \
  detector_ai \
  python object_detector.py
```

## 🎥 Uso con Cámara (Linux)

Para Linux, descomenta las líneas `devices` en `docker-compose.yml`:

```yaml
devices:
  - /dev/video0:/dev/video0
```

Luego ejecuta:
```bash
docker-compose up
```

## 💾 Volumes

- `./assets:/app/assets` - Acceso a las imágenes y recursos
- `./runs:/app/runs` - Salida de detecciones y resultados

## 🔧 Cambiar el Script Principal

Por defecto ejecuta `main.py`. Para cambiar, modifica en `Dockerfile`:

```dockerfile
# En lugar de:
CMD ["python", "main.py"]

# Usa:
CMD ["python", "object_detector.py"]
# o
CMD ["python", "text_detector.py"]
# o
CMD ["python", "image_matcher.py"]
```

## 📊 Ver contenedores

```bash
# Listar contenedores ejecutándose
docker ps

# Listar todas las imágenes
docker images

# Ver logs
docker logs detector_ai

# Acceder al contenedor
docker exec -it detector_ai /bin/bash
```

## 🧹 Limpiar

```bash
# Detener y eliminar contenedor
docker-compose down

# Eliminar imagen
docker rmi detector_ai

# Limpiar todo (contenedores, imágenes, volúmenes)
docker system prune -a
```

## ⚙️ Requisitos

- Docker >= 20.10
- Docker Compose >= 1.29
- RAM mínima: 4GB (recomendado 8GB+)
- GPU (opcional): NVIDIA GPU con nvidia-docker para aceleración

## 🚀 GPU Support (NVIDIA)

Si tienes GPU NVIDIA, instala `nvidia-docker` y modifica `docker-compose.yml`:

```yaml
services:
  detector_ai:
    build: .
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
```
