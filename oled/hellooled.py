# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time




# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)

display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
disp=display

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:
    # Clear image buffer by drawing a black filled box to fill the whole display
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Draw a white filled box to clear the image.
    #draw.rectangle((0,0,width,height), outline=255, fill=255)

    # Write two lines of text.
    #draw.text((0, 0),  'Hello',  font=font, fill=255)
    #draw.text((0, 10), 'World!', font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
   # time.sleep(2)
    
    # Example: Drawing Shapes
    draw.rectangle((10, 20, 55, 45), outline=255, fill=0)
    # Write two lines of text.
    draw.text((13, 23),  'Hello',  font=font, fill=255)
    draw.text((13, 33), 'World!', font=font, fill=255)

    disp.image(image)
    disp.show()
    time.sleep(2)
    
    # Clear display.
    #disp.clear()
    disp.show()
    time.sleep(1)