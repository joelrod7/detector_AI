
import gradio as gr
from ultralytics import YOLO
import cv2
import easyocr
import numpy as np

# Cargar modelos
yolo_model = YOLO("yolov8n.pt")
ocr_reader = easyocr.Reader(["en"], gpu=False)

# Función para detección de objetos
def detect_objects_from_image(image):
    results = yolo_model(image)
    return results[0].plot()

# Función para detección de texto
def detect_text_from_image(image):
    results = ocr_reader.readtext(image)
    for (bbox, text, prob) in results:
        (top_left, _, bottom_right, _) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    return image

# Función para coincidencia de imagen
def match_template(image, template):
    if template is None:
        return image
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)

    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(res)

    h, w = template_gray.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
    return image

# Crear interfaz
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Visión Demo en Python")
    with gr.Tab("Detección de Objetos (YOLOv8)"):
        img_input = gr.Image(label="Sube una imagen", type="numpy")
        obj_output = gr.Image(label="Resultado")
        btn1 = gr.Button("Detectar objetos")
        btn1.click(fn=detect_objects_from_image, inputs=img_input, outputs=obj_output)

    with gr.Tab("Detección de Texto (OCR)"):
        img_input_ocr = gr.Image(label="Sube una imagen", type="numpy")
        ocr_output = gr.Image(label="Resultado")
        btn2 = gr.Button("Detectar texto")
        btn2.click(fn=detect_text_from_image, inputs=img_input_ocr, outputs=ocr_output)

    with gr.Tab("Coincidencia de Imágenes"):
        img_main = gr.Image(label="Imagen principal", type="numpy")
        img_template = gr.Image(label="Plantilla a buscar", type="numpy")
        match_output = gr.Image(label="Resultado")
        btn3 = gr.Button("Buscar plantilla")
        btn3.click(fn=match_template, inputs=[img_main, img_template], outputs=match_output)

demo.launch()
