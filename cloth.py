import cv2
import numpy as np
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)
time.sleep(3)  # Give the camera some time to adjust

# Capture the background (without the person)
print("Capturing background... Stay out of the frame.")
for i in range(50):  # Capture multiple frames to get a stable background
    ret, background = cap.read()

background = cv2.flip(background, 1)  # Flip to match the live video

print("Background captured. Now wear your cloak!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame to match the background
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV color space

    # Define color range for the cloak (red in this case)
    lower_red1 = np.array([0, 120, 70])  # Lower boundary for red
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])  # Upper boundary for red
    upper_red2 = np.array([180, 255, 255])

    # Create masks to detect red color
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2  # Combine both masks

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))  # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert the mask to get everything except the cloak
    mask_inv = cv2.bitwise_not(mask)

    # Extract the person (excluding the cloak)
    person = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Extract the background only where the cloak is present
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Combine both to create the invisible effect
    final_output = cv2.add(person, cloak_area)

    # Display the output
    cv2.imshow("Invisible Cloak", final_output)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()



