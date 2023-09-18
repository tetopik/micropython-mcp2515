# Micropython_MCP2515
Micropython driver to communicate to CAN buses using MPC2515 via SPI port

This driver is based on capella-ben' microPython_MCP2515 driver. I modified the original driver to:
1. Add the capability to change the crytal baudrate (8MHz, 10MHz, 16MHz)
2. Simplify the code
3. Add config file for easy implementing
4. More examples

Check adafruit_mcp2515 for documentation.
