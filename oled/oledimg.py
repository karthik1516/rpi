from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

OLED_WIDTH=128
OLED_HEIGHT=64
ADDR=0x3c

def clear(display):
    display.fill(0)
    display.show()


i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=ADDR)


#image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
#draw = ImageDraw.Draw(image)
#font = ImageFont.load_default()

clear(display)
with Image.open("./ic.webp") as im:
    i3=im.resize((OLED_WIDTH, OLED_HEIGHT))
    i4=i3.convert('1')
    display.image(i4)
    display.show()





