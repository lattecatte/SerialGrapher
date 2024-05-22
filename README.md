# SerialGrapher
*[Used on Kyushu University's Phoenix LR unmanned aircraft for 2023 Aeromagnetic Survey in Afar, Ethiopia]*

Real-time graph plotter based on keyword data received from serial communication.


https://github.com/lattecatte/SerialGrapher/assets/154484150/ed7abfde-140b-40aa-817d-8f19eded9e3e


## Features
- Filters a keyword and plots the keyword data in real-time using matplotlib animation.
- Shows cumulative data and interval data plots.
- Shows maximum, minimum, average, and current values.

## Instructions
For real serial communication with a real modem:
1. Edit the first line in serial_rx.py to reflect the used COM port and the integer 9600 to match the baud rate of the corresponding modem.
2. Run serial_rx.py.
3. Start the modem and serial communication.

For virtual serial communication for testing and debugging purposes:
1. Open a pair of virtual ports on your PC.<br>
  This can be done via a third-party software such as VSPD.<br>
  In VSPD, open a pair of virtual serial ports.<br>
  Select the pair and click the "Edit" button.<br>
  Select the port names. In the code's sample case, "COM29" and "COM30" were used.<br>
  Check "Enable strict baudrate emulation".<br>
  Click "Save".
2. Rename the sample text file you want to test read to "sample.txt".
3. Place sample.txt into the same directory as serial_rx.py.
4. Edit the first line in serial_rx.py and serial_tx.py to reflect the COM port selected in VSPD.
5. Run serial_rx.py.
6. Run serial_tx.py.

### Optional Settings
In serial_tx.py:
- Edit the line "time.sleep(1)" to set the time delay (in seconds) for each virtual keyword appearance. 

In serial_rx.py:
- Edit the line "xs1 = xs1[-15:]" to set desired time interval (in seconds) for the graph on the right.
- Uncomment the line "ax.set_ylim" to make 0 always visible on the y-axis.
