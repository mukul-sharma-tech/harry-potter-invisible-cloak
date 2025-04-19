# harry-potter-invisible-cloak
🧙‍♂️ Harry Potter Invisible Cloak Project
This project allows you to experience your very own Harry Potter Invisible Cloak! Using your webcam and OpenCV, the cloak effect will make you invisible by removing the color of your red cloak from the video feed in real-time, just like the magical cloak from the Harry Potter series.

📽️ Demo

A real-time webcam feed is used to detect a red cloak, removing it from the frame and creating an "invisible" effect.

Wear a red cloak or any red garment to trigger the effect.

🧠 Features
Invisible Cloak Effect: The red cloak is removed, creating an invisibility illusion.

Real-Time Video Feed: The webcam tracks the cloak's color in real-time.

Background Capture: The environment is captured as the background and remains visible when the cloak is detected.

Simple and Fun: Just wear a red cloak or garment, and the magic happens!

💻 Tech Stack
Python

OpenCV (cv2) for real-time video processing

NumPy for numerical operations

Time for background capturing delays

🖥️ Installation
Clone the repository:

git clone https://github.com/mukul-sharma-tech/harry-potter-invisible-cloak.git
cd harry-potter-invisible-cloak
Install dependencies:

pip install opencv-python numpy
Run the script:

python invisible_cloak.py
📌 Usage Instructions
Prepare Your Cloak:

Wear a red cloak or garment. The system detects the red color to simulate the invisibility effect.

Start the Program:

Run the Python script to start the webcam and cloak detection.

Enjoy the Effect:

Watch as the red area is removed, and your cloak disappears.

Press 'q' to quit and close the window.

🧠 How It Works
Background Capture:

The system first captures the background of the environment without the person wearing the cloak. This gives the illusion of invisibility.

Color Detection:

The red color range is detected in the webcam feed using OpenCV's HSV color space.

Two ranges for red are used to account for various shades of red.

Masking:

A mask is created to identify the red areas (the cloak).

The cloak area is replaced with the captured background, creating the invisibility effect.

🧑‍🔬 Gesture Logic Summary
Red Cloak Detection:

The red color range is tracked and removed from the video frame.

Background Replacement:

The area where the cloak is detected is replaced by the previously captured background.

🎨 Customization
You can adjust:

Cloak color detection range to match different shades of red.

Background capture time for better stability.

Feel free to tweak and experiment with different colors or effects for more magical features!

🤝 Contributing
Pull requests are welcome! If you have improvements, suggestions, or bug fixes, feel free to contribute. Ideas for expanding the magic, such as adding sound effects, additional color customization, or multi-colored cloaks, are welcome!

Enjoy the magic of the Harry Potter Invisible Cloak and immerse yourself in a little bit of wizardry today! ✨🧙‍♂️

