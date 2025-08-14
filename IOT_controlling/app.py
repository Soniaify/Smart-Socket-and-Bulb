from flask import Flask, request, render_template
import serial
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Open serial connection inside the request handler
            arduino = serial.Serial("COM3", 115200, timeout=2)
            time.sleep(2)  # wait for Arduino to reset
            
            if 'on_button' in request.form:
                arduino.write('on'.encode())
            elif 'off_button' in request.form:
                arduino.write('off'.encode())

            res = arduino.readline().decode('utf-8').strip()
            arduino.close()
            return res
        except Exception as e:
            return f"Error: {str(e)}"
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
