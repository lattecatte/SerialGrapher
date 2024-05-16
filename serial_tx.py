import serial
import time

ser = serial.Serial('COM30', 9600) # change string 'COM30' to match transmitting port
sample = open('sample.txt')
sample_list = sample.readlines()
mag_counter = 0

for line in range(len(sample_list)):
    if sample_list[line].startswith('$MAG'):
        # time.sleep(1) # set 1 second delay between writing $MAG lines
        mag_counter += 1
        ser.write(sample_list[line].encode('Ascii'))
        print('MAG Line:', mag_counter, ',', 'Serial Line:', line, '(', sample_list[line], ')')