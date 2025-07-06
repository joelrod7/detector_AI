from ultralytics import YOLO
import cv2

def detect_objects(image_path, model_path="yolov8n.pt"):
    model = YOLO(model_path)
    results = model(image_path)

    for r in results:
        r.plot(show=True)

# Ejemplo de uso
if __name__ == "__main__":
    detect_objects("assets/test_image.jpg")
