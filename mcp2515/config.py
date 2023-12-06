from micropython import const
from mcp2515 import MCP2515 as CAN
from machine import freq, Pin


_USE_HW_SPI = False

if not _USE_HW_SPI:
    from machine import SoftSPI
    
    CS_PIN = 16
    
    _SCK_PIN   = const(35)
    _MOSI_PIN  = const(33)
    _MISO_PIN  = const(18)
    _MAX_CPU_F = const(240_000_000)
   
    if freq() is not _MAX_CPU_F:
        freq(_MAX_CPU_F)
    
    spi = SoftSPI(
        sck=Pin(_SCK_PIN),
        mosi=Pin(_MOSI_PIN),
        miso=Pin(_MISO_PIN),
        baudrate=1_200_000,
        firstbit=SoftSPI.MSB,
        polarity=0,
        phase=0)

else:
    from machine import SPI

    CS_PIN = 10
    
    spi = SPI(
        1,
        baudrate=10_000_000,
        firstbit=SPI.MSB,
        polarity=0,
        phase=0)

print('FREQ\t: ', freq(), '\nSPI\t: ', spi, '\nCS\t: ', CS_PIN)

can_bus = CAN(spi, CS_PIN,
    baudrate     = 500_000,    # 125_000, 500_000, 1_000_000, etc  (bps)
    crystal_freq = 16_000_000,  # 8_000_000, 10_000_000, 16_000_000 (Hz)
    loopback     = False,
    silent       = False,
    auto_restart = False,
    debug        = False)
