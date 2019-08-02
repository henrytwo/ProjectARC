# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import pickle 
import math

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 20
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)

# Period of rotation in seconds
per = 0.545

# Load pattern
with open('pattern.pkl', 'rb') as file:
    pattern = pickle.load(file)

start = time.time()

while True:

    angle = ((time.time() - start) % per) / per

    pixels.fill((0, 0, 0))

    for i in range(num_pixels):
        # Start at the center of the jagged array and sweep out
        pixels[i] = pattern[num_pixels - 1 + int(i * math.cos(angle * 2 * 3.1415))][num_pixels - 1 + int(i  * math.sin(angle * 2 * 3.1415))]

    pixels.show()

    time.sleep(per / 100)
