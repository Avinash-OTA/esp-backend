import serial

# Replace 'COMx' with your actual UART port, and adjust baudrate accordingly
ser = serial.Serial('COMx', baudrate=9600)

try:
    # Sending data
    ser.write(b'YourUARTCommandHere')

    # Reading data (optional)
    response = ser.readline()
    print(f'Response from UART: {response.decode()}')

finally:
    ser.close()