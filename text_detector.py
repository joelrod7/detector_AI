import easyocr
import cv2
import matplotlib.pyplot as plt
import warnings # ignorar advertencia sin GPU
warnings.filterwarnings("ignore")


def detect_text(image_path, lang='en'):
    reader = easyocr.Reader([lang])
    results = reader.readtext(image_path)

    image = cv2.imread(image_path)
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    detect_text("assets/7.jpg")
