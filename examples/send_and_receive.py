from mcp2515.canio import Timer, Message, RemoteTransmissionRequest
from mcp2515.config import can_bus
from mcp2515 import MCP2515 as CAN
from urandom import randint
from ustruct import pack


sender = Timer(2)

while True:
    if sender.expired:
        sender.rewind_to(1.0)
        message = Message(id=0x557, data=pack('>BB', randint(122, 144), 337), extended=randint(0, 2))
        send_success = can_bus.send(message)
        print("Send success:", send_success)
        
    with can_bus.listen(timeout=1.0) as listener:       
        message_count = listener.in_waiting()
        if message_count == 0:
            continue
        print(message_count, "messages available")
        for _i in range(message_count):
            msg = listener.receive()
            print("Message from ", hex(msg.id), "extended:", msg.extended)
            if isinstance(msg, Message):
                print("message data:", msg.data)
            if isinstance(msg, RemoteTransmissionRequest):
                print("RTR length:", msg.length)
            print("")

