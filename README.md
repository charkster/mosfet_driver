# mosfet_driver
MOSFET driver board which can connect to a Xiao MCU board. The outer left holes are to be shared with the right side of a Seeed Xiao board. I am expecting to use jumpers to connect the 5V, GND and GPIO signals.

A MCP1416R mosfet driver is connected to a TO-220-3 package mosfet. I plan to use the USB 5V to power the MCP1416R and four 22uF ceramic caps will provide the current needed to quickly turn on the mosfet (as ceramic caps have the lowest ESR). My mosfet of choice is a IRFB7430PBF (40V, 195A).

Oshpark charged me $5.20 for 3 boards with Super-Swift-Service and USPS shipping.

![picture](https://github.com/charkster/mosfet_driver/blob/main/mosfet_driver_top_layout.png)

![picture](https://github.com/charkster/mosfet_driver/blob/main/mosfet_driver_3d.png)
