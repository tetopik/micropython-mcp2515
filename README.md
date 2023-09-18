# Micropython_MCP2515
Micropython driver to communicate to CAN buses using MPC2515 via SPI port.


This driver is based on capella-ben' microPython_MCP2515 as well as Adafruit_CircuitPython_MCP2515 driver.

I modified here and there to:
  1. Add the capability to change the crystal baudrate (8MHz, 10MHz, 16MHz)
  2. Simplify the lib files
  3. Add config file for easy testing
  4. More examples


Go check Adafruit_CircuitPython_MCP2515 for further implementation.
