# Hand Gesture Controlled LEDs

This project uses computer vision and Arduino to control the brightness of LEDs based on hand gestures detected through a webcam. By utilizing the MediaPipe library for hand tracking and the PyFirmata library for Arduino communication, the system maps the distance of hand landmarks to the intensity of LEDs connected to an Arduino board.

---

## Features
- Real-time hand detection using MediaPipe's hand-tracking module.
- Calculation of distances between hand landmarks.
- Control of 5 LEDs on an Arduino board based on the distances.
- LEDs are dimmed or brightened dynamically based on finger movements.
- Automatic LED reset when no hand is detected for a specified duration.

---

## Technologies Used

### Python Libraries
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For real-time hand landmark detection.
- **PyFirmata2**: For communication with the Arduino board.
- **Math**: For distance calculations.
- **Time**: For timing logic and timeouts.

### Hardware
- **Arduino Board**: Used to control the LEDs.
- **5 LEDs**: Connected to the Arduino on PWM pins.
- **Webcam**: For capturing live video.

---

## Setup and Installation

### Requirements
1. **Python 3.x**
2. **Arduino Board** with appropriate drivers installed.
3. **Webcam** for video input.

### Install Python Dependencies
Run the following command to install the required Python libraries:

```bash
pip install opencv-python mediapipe pyfirmata2
```

### Arduino Setup
1. Connect 5 LEDs to the Arduino board's PWM pins: `3`, `5`, `6`, `9`, `10`.
2. Ensure the Arduino board is connected to your computer.
3. Update the COM port in the code (`COM9`) to match your Arduino's port.

---

## How It Works

1. **Hand Detection**: The program uses MediaPipe to detect hand landmarks in real-time from the webcam feed.
2. **Distance Calculation**: The Euclidean distance between each finger landmark and the palm's center is calculated.
3. **LED Control**:
   - If the calculated distance exceeds a threshold, the corresponding LED is turned on with brightness proportional to the distance.
   - If no hand is detected for more than 1 second, all LEDs are turned off.
4. **Real-time Feedback**: The processed video is displayed, showing the detected hand landmarks.

---

## Usage

1. Run the Python script:

   ```bash
   python script_name.py
   ```

2. Place your hand in front of the webcam. Adjust the distances of your fingers to control the LEDs' brightness.
3. To exit the program, press the `q` key.

---

## Code Explanation

### Arduino Initialization
```python
board = pyfirmata2.Arduino('COM9')
led1 = board.get_pin("d:3:p")
led2 = board.get_pin("d:5:p")
led3 = board.get_pin("d:6:p")
led4 = board.get_pin("d:9:p")
led5 = board.get_pin("d:10:p")
```
Sets up communication with the Arduino board and initializes the LEDs on specified pins.

### Hand Landmark Detection
```python
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils
```
Initializes MediaPipe's hand detection model.

### LED Brightness Control
```python
if distanse1 > 0.13375745176688528:
    led1.write(distanse1*2)
else:
    led1.write(0)
```
Calculates the distance and adjusts the brightness of LEDs accordingly.

### Timeout Mechanism
```python
if hand_detected and time.time() - start_time > timeout_duration:
    led1.write(0)
    led2.write(0)
    led3.write(0)
    led4.write(0)
    led5.write(0)
    hand_detected = False
```
Resets all LEDs if no hand is detected for the specified duration.

---

## Customization
- **COM Port**: Update `COM9` to match your Arduino's port.
- **LED Pins**: Modify the pin assignments if needed.
- **Threshold Values**: Adjust the distance thresholds to match your hand size and desired sensitivity.
- **Timeout Duration**: Change the `timeout_duration` value for different reset timings.

---

## License
This project is licensed under the MIT License.

---

## Contributing
Feel free to submit issues or pull requests to improve this project. Suggestions and feedback are welcome!

---

## Acknowledgments
- MediaPipe for the excellent hand-tracking library.
- PyFirmata for simplifying Arduino communication.

