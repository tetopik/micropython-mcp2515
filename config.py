from micropython import const
from mcp2515 import MCP2515 as CAN
from umachine import freq, Pin


_USE_HW_SPI = False

if not _USE_HW_SPI:
    from umachine import SoftSPI as SPI
    
    _sck_pin  = const(35)
    _mosi_pin = const(33)
    _miso_pin = const(18)
    _cs_pin   = 16
    
    _max_cpu_freq = const(24*(10**7))
    if freq() is not _max_cpu_freq:
        freq(_max_cpu_freq)

    _spi = SPI(
        sck=Pin(_sck_pin),
        mosi=Pin(_mosi_pin),
        miso=Pin(_miso_pin),
        baudrate=1_200_000,
        firstbit=SPI.MSB,
        polarity=0,
        phase=0)

else:
    from umachine import SPI
    
    _cs_pin = 16
    
    _spi = SPI(
        1,
        baudrate=10_000_000,
        firstbit=SPI.MSB,
        polarity=0,
        phase=0)

print('FREQ\t: ', freq(), '\nSPI\t: ', _spi, '\nCS\t: ', _cs_pin)
can_bus = CAN(_spi, _cs_pin)
