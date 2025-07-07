# 🧠 Visión por Computadora con Python

Proyecto de ejemplo para detección de **objetos**, **texto (OCR)** y **coincidencia de imágenes** utilizando Python y librerías como `YOLOv8`, `EasyOCR` y `OpenCV`.

---

## 📦 Requisitos

- Python 3.8 o superior
- pip
- Recomendado: entorno virtual (venv)

### 🛠️ Instalación

```bash
git clone 
python -m venv objenv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📁 Estructura del Proyecto

```
name_project/
│
├── main.py                 # Script principal de prueba
├── object_detector.py      # Detección de objetos con YOLOv8
├── text_detector.py        # Detección de texto con EasyOCR
├── image_matcher.py        # Coincidencia de imágenes con OpenCV
├── requirements.txt
└── assets/
    ├── test_image.jpg      # Imagen de prueba
    ├── template.jpg        # Plantilla para coincidencia
    └── video.mp4           # Video opcional
```

---

## 🧪 Cómo ejecutar

### 🔍 Detección de Objetos (imagen, cámara o video)

```bash
python object_detector.py
```

Por defecto usa una imagen (`assets/test_image.jpg`), pero puedes activar el uso de cámara o video editando:

```python
# object_detector_cam.py
detect_objects_from_camera()                # Usa cámara
# detect_objects_from_camera("assets/video.mp4")  # Usa video
```

---

### 🧾 Detección de Texto OCR (imagen, cámara o video)

```bash
python text_detector.py
```

Opciones similares para trabajar con imágenes o videos.

---

### 🧩 Coincidencia de Imágenes (template matching)

```bash
python image_matcher.py
```

Busca una plantilla (`assets/template.jpg`) dentro de una imagen más grande (`assets/test_image.jpg`).

---

## 📌 Notas

- El modelo YOLOv8 se descarga automáticamente en la primera ejecución (`yolov8n.pt`).
- Para OCR en otro idioma, cambia el parámetro `lang='es'` o `lang='en'`.

---

## 🔓 Licencia

Este proyecto es de código abierto bajo la licencia MIT.
