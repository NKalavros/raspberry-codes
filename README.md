#Connecting the Stepper Motor Driver:

[Specs for Wantai NEMA17 stepper motor:](https://grobotronics.com/stepper-motor-42byghw208-2.6kg.cm.html) Rate current is 0.4A

[Some notes on the A4988 stepper motor driver:](https://reprap.org/wiki/A4988_vs_DRV8825_Chinese_Stepper_Driver_Boards)
[And another link on the same subject:](https://www.allegromicro.com/en/Products/Motor-Drivers/Brush-DC-Motor-Drivers/A4988.aspx)
Our driver is equipped with two R100 resistors. We need to calculate the reference voltage for it, the formula being: I_TripMax= Vref/(8*Rs).
Therefore the current limit being 0.4A, our Vref is 0.4/0.8 = 0.5 V???

First, check the [image](https://raw.githubusercontent.com/NKalavros/raspberry-codes/master/IMG_20190929_232454.jpg) in the repository for the location of the pins. Next, begin making the connections, they are a little different than the actual schematic:
![Connection schematic](/schematic.png)

1. Connect Logic Ground to Ground rail
1. Connect Motor Ground to Ground rail
1. Connect power supply pos to VMOT
1. Connect power supply neg to Motor Ground
1. Connect 50 uF Capacitor to VMOT and Motor Ground (Gray stripe indicates the - end, connect that to the Motor Ground)
1. Connect Sleep to GPIO#16
1. Connect Reset to the Pi 3V3 pin
1. Connect Step  to GPIO#21
1. Connect Direction to GPIO#20
1. Connnect Pi GND (next to the 5V pins) to t Ground rail
1. Bootup Pi
1. Bootup Power supply at 12V
1. Connect power supply (measured using multimeter to 9.090V)
1. Bootup Polymeter
1. Use an alligator to connect a jumper to the negative pin
1. Use an alligator to connect a metal screwdriver to the positive pin
1. Screw clockwise to reduce Vref or counterclockwise to increase it (need 0.5V)
1. Disconnect the power supply and the Raspberry Pi
1. Connect the NEMA motor to 4 jumpers, after figuring out the coils (it has 2 coil groups - biphasic). You can try to light an LED or check for coil continuity with your multimeter.The coils are 12 and 34, as would be expected (checked with own multimeter).
1. Connect 1 coil pair to A1 and A2 and another to B1 and B2.
1. Connect MS1, MS2 and MS3 to GPIO #14, #15 and #18 (Make sure those connections are correct).
1. Bootup Pi and Power supply at 12V
1. Connect Raspberry Pi to screen or use VNC to access it (if on Wi-Fi)

Run the scripts that begin with test to make sure that the motor is working

[Some great resource](https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/)
