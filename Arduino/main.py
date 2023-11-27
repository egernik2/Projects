import serial

ser = serial.Serial('COM1', 9600)

ser.write(b'Hello, Arduino!')

data = ser.read(10)
print (data)