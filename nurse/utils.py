import serial

def send_serial_data(data, port='COM1', baudrate=9600):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Opened serial port: {ser.name}")

        # Send the data
        ser.write(data.encode())
        print(f"Sent data: {data}")

        # Close the serial port
        ser.close()
        print("Closed serial port")

    except serial.SerialException as e:
        print(f"Error: {e}")

