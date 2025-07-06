import cv2
import matplotlib.pyplot as plt

def match_template(image_path, template_path):
    img = cv2.imread(image_path, 0)
    template = cv2.imread(template_path, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    h, w = template.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(img_color, top_left, bottom_right, (0, 0, 255), 2)

    plt.imshow(img_color)
    plt.title("Image Match")
    plt.axis("off")
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    match_template("assets/test_image.jpg", "assets/7.jpg")
