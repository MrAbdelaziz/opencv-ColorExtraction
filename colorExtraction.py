import cv2
import numpy as np

clicked_colors = []

drawing = False
start_x, start_y = -1, -1

def mouse_event(event, x, y, flags, param):
    global drawing, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image_copy = image.copy()
            cv2.rectangle(image_copy, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', image_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow('Image', image)

        selected_region = image[start_y:y, start_x:x]
        colors_in_region = np.unique(selected_region.reshape(-1, 3), axis=0)
        clicked_colors.extend(colors_in_region.tolist())

if __name__ == '__main__':
    image = cv2.imread('image.png')  # Replace with your image file path

    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', mouse_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Colors within the selected rectangle:")
    for color in clicked_colors:
        print(f"({color[0]}, {color[1]}, {color[2]})")
