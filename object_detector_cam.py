from ultralytics import YOLO
import cv2

def detect_objects_from_camera(model_path="yolov8n.pt", source=0):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(source)  # 0 = cámara web, o reemplaza con ruta a un archivo .mp4

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 - Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Ejemplo de uso
if __name__ == "__main__":
    # Cámara en vivo
    # detect_objects_from_camera()

    # O video local
    detect_objects_from_camera(source="assets/video.mp4")
