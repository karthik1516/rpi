import time
import board
import adafruit_dht

from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

OLED_WIDTH=128
OLED_HEIGHT=64
ADDR=0x3c

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

def clear(display):
    display.fill(0)
    display.show()


i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=ADDR)


image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

def show_text(txt1, txt2, txt3):
    image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    clear(display)
    draw.text((5,5), txt1, fill=255, font=font)
    draw.text((5,20), txt2, fill=255, font=font)
    draw.text((5,35), txt3, fill=255, font=font)
    display.image(image)
    display.show()

show_text('Cool', 'Temperature', 'Sensor')
time.sleep(5)



# Initialize the DHT device, with data pin connected to:
# - GPIO 4 (as per [1] and [4])
# - GPIO 17 (as per [5], alternative)
dht_device = adafruit_dht.DHT11(board.D4)  # Use board.D17 for GPIO 17

while True:
    try:
        # Print the values to the serial port
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity
        s1=now()
        s2='Temperature: {:.2f}F'.format(temperature_f)
        s3='Humidity: {:.2f}%'.format(humidity)
        show_text(s1,s2,s3)

    except Exception as e:
        print("Error: {}".format(e))

    time.sleep(10)  # Wait 1 second before taking the next reading
