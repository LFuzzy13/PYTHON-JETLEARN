import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

bg = cv2.imread("brightness.png")

if bg is None:
    print("Error: background.jpg could not be found.")
    cap.release()
    exit()

bg = cv2.resize(bg, (160, 120))

mp_selfie = mp.solutions.selfie_segmentation

segment = mp_selfie.SelfieSegmentation(model_selection=1)

previous_mask = None

while True:

    ret, frame = cap.read()

    if not ret:
        print("Could not read webcam.")
        break

    frame = cv2.resize(frame, (160, 120))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = segment.process(rgb)

    mask = result.segmentation_mask

    mask = mask.astype(np.float32)

    if previous_mask is None:
        previous_mask = mask
    else:
        previous_mask = 0.80 * previous_mask + 0.20 * mask

    mask = previous_mask

    binary_mask = (mask > 0.5).astype(np.uint8) * 255

    kernel = np.ones((5, 5), np.uint8)

    binary_mask = cv2.morphologyEx(
        binary_mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    binary_mask = cv2.morphologyEx(
        binary_mask,
        cv2.MORPH_OPEN,
        kernel
    )

    smooth_mask = cv2.GaussianBlur(
        binary_mask,
        (15, 15),
        0
    )

    alpha = smooth_mask.astype(np.float32) / 255.0

    alpha = alpha[:, :, None]

    frame_float = frame.astype(np.float32)
    bg_float = bg.astype(np.float32)

    output = alpha * frame_float + (1 - alpha) * bg_float

    output = np.clip(output, 0, 255).astype(np.uint8)

    cv2.imshow("Webcam Background Test", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


