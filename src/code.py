import board
import displayio
import terminalio

from adafruit_display_text import label
import adafruit_displayio_ssd1305

# Props
WIDTH = 128
HEIGHT = 32
FONTSCALE = 1


# Detaches from display if something goes wrong
displayio.release_displays()

# Create the I2C interface.
i2c = board.I2C()

# Create the display bus
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Create the display
display = adafruit_displayio_ssd1305.SSD1305(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE, x=display.width // 2 - text_width // 2, y=display.height // 2
)
text_group.append(text_area)
splash.append(text_group)

while True:
    pass
