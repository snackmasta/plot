import serial
import matplotlib.pyplot as plt

# Serial port configuration
ser = serial.Serial('COM11', 9600)  # Replace 'COM3' with your serial port

# Initialize lists to store data
angles = []
distances = []

# Read data from serial
while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        angle, distance = map(int, line.split(','))
        angles.append(angle)
        distances.append(distance)
        print(f"Angle: {angle}, Distance: {distance}")
        
        # Break the loop after reading all angles from Arduino
        if angle == 179:
            break

# Close serial port
ser.close()

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(angles, distances, marker='o', linestyle='-', color='b', label='Distance')
plt.title('Distance vs Angle')
plt.xlabel('Angle')
plt.ylabel('Distance (cm)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
