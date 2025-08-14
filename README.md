# IoT Smart Socket and Bulb Controller

This project demonstrates how to control a smart socket and a bulb through a web-based interface using **Flask** (Python) and **Arduino**. The system allows you to turn the devices ON or OFF from a webpage, with commands sent over serial communication to the Arduino.

---

## Features
- **Web-based Control**: Simple HTML interface to turn devices on/off.
- **IoT Integration**: Uses Flask to handle HTTP requests and Arduino for hardware control.
- **Serial Communication**: Python sends commands directly to Arduino over USB.
- **Cross-platform**: Works on any system that can run Flask and connect to Arduino.

---

## Project Structure
├── app.py # Flask backend server
├── index.html # Web interface
├── IOT.ino # Arduino code for controlling devices

---

## Requirements
### Hardware
- Arduino board (e.g., Uno, Nano)
- Smart socket or relay module
- Bulb or load device
- USB cable for Arduino
- Jumper wires

### Software
- Python 3.x
- Arduino IDE
- Flask (`pip install flask`)
- PySerial (`pip install pyserial`)

---

## Setup Instructions

1. **Arduino Setup**
   - Open `IOT.ino` in Arduino IDE.
   - Upload to your Arduino board.
   - Connect the smart socket/relay and bulb according to the wiring diagram in your Arduino code.

2. **Python & Flask Setup**
   ```bash
   pip install flask pyserial
Edit app.py and change "COM3" to your Arduino's port (e.g., "/dev/ttyUSB0" for Linux).

3. **Run the Flask App**
   - python app.py
   - Access the web interface at: http://127.0.0.1:5000

4. **Control Devices**
   - Click Turn on Socket and bulb to switch devices ON.
   - Click Turn off Socket and bulb to switch devices OFF.

## How It Works
   - User Action: Click a button on the webpage.
   - Flask Backend: Sends the corresponding command (on or off) over serial to Arduino.
   - Arduino: Reads the command and switches the socket/bulb via relay.

Arduino: Reads the command and switches the socket/bulb via relay.
