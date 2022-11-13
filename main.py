import cv2
import numpy as np
import math

if __name__ == "__main__":

    # =============== Loads a frame of the camera which captures the road ===============#
    image = cv2.imread("sample.png")
    # cv2.imshow("Basic Image", image)
    cv2.waitKey(0)

    # =============== Transforms the loaded frame to gray scale =========================#

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Grayscaled Image", gray)
    cv2.waitKey(0)

    # =============== Blurs the grayed out image =======================================#

    blur = cv2.blur(image, (9, 9))
    cv2.imshow("Blurred Image", blur)
    cv2.waitKey(0)

    # =============== Creating a mask to apply to our image ============================#

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (0, 170), (640, 480), 255, -1)
    cv2.imshow("Mask", mask)
    cv2.waitKey(0)

    # =============== Applying the mask to apply to our image ==========================#

    masked = cv2.bitwise_and(blur, blur, mask=mask)
    cv2.imshow("Mask applied to Image", masked)
    cv2.waitKey(0)

    # =============== Detecting the edges of our image =================================#

    edges = cv2.Canny(masked, 110, 220)
    cv2.imshow("Detected edges", edges)
    cv2.waitKey(0)

    # =============== Detecting the lines from the image ===============================#

    detected = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(detected, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Detected Lines", detected)
    cv2.waitKey(0)

    # ================ Creating and applying a mask to the detected lanes =============#

    mask2 = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask2, (0, 180), (640, 480), 255, -1)
    maskedDetected = cv2.bitwise_and(detected, detected, mask=mask2)
    cv2.imshow("Masked Detected Lines", maskedDetected)
    cv2.waitKey(0)

    # ====== Final image: the loaded frame with the detected lanes on top =============#

    final = cv2.addWeighted(image, 0.5, maskedDetected, 0.7, 0)
    cv2.imshow("Final image", final)
    cv2.waitKey(0)
