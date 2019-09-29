[Specs for Wantai NEMA17 stepper motor:](https://www.cableworks.gr/ilektronika/arduino-and-microcontrollers/motors/stepper/nema-17-wantai-stepper-motor-42byghw609-4000g.cm-1.7a-3d-reprap-printer-ce-rosh-iso/)

[Some notes on the A4988 stepper motor driver:](https://reprap.org/wiki/A4988_vs_DRV8825_Chinese_Stepper_Driver_Boards)
[And another link on the same subject:](https://www.allegromicro.com/en/Products/Motor-Drivers/Brush-DC-Motor-Drivers/A4988.aspx)
Our driver is equipped with two R100 resistors. We need to calculate the reference voltage for it, the formula being: I_TripMax= Vref/(8*Rs).
Therefore the current limit being
