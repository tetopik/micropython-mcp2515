from mcp2515.canio import Message, RemoteTransmissionRequest
from mcp2515.config import _spi, _cs_pin
from mcp2515 import MCP2515 as CAN
from utime import sleep


can_bus = CAN(
    _spi, _cs_pin, loopback=True, silent=True
)  # use loopback to test without another device

while True:
    with can_bus.listen(timeout=1.0) as listener:

        message = Message(id=0x1234ABCD, data=b"adafruit", extended=True)
        send_success = can_bus.send(message)
        print("Send success:", send_success)
        message_count = listener.in_waiting()
        print(message_count, "messages available")
        for _i in range(message_count):
            msg = listener.receive()
            print("Message from ", hex(msg.id))
            if isinstance(msg, Message):
                print("message data:", msg.data)
            if isinstance(msg, RemoteTransmissionRequest):
                print("RTR length:", msg.length)
    sleep(1)
