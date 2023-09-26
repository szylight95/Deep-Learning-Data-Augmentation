import cv2
import random

def cutout(img):
    h, w = img.shape[:2]
    scales = [0.5] * 1 + [0.25] * 2 + [0.125] * 4 + [0.0625] * 8 + [0.03125] * 16
    for s in scales:
        mask_h = random.randint(1, int(h * s))
        mask_w = random.randint(1, int(w * s))

        # box
        xmin = max(0, random.randint(0, w) - mask_w // 2)
        ymin = max(0, random.randint(0, h) - mask_h // 2)
        xmax = min(w, xmin + mask_w)
        ymax = min(h, ymin + mask_h)

        img[ymin:ymax, xmin:xmax] = [random.randint(0, 255) for _ in range(3)]

def main():
    # Load an example image (you should replace this with your own image)
    image_path = 'example.jpg'
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image from '{image_path}'")
        return

    # Apply the cutout function
    cutout(img)

    # Display the original and modified images
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Modified Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
