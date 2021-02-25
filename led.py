# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import COVID19Py
import random
import math
import statistics
import socket

# time.sleep(20)

# Get Covid information from API
covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()

cases = latest['confirmed']
print(cases)
infected = False

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 8

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# WIFI configurations
LOCAL_UDP_IP = "192.168.1.2"
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.bind((LOCAL_UDP_IP, SHARED_UDP_PORT))


def sigmoid(x):
  return 1 / (1 + math.exp(-x))


def natural_infection():
    new_input = random.randint(0, cases)
    rand_input.append(new_input)
    if len(rand_input) > 10 :
        rand_input.pop(0)
    map(sigmoid, rand_input)
    res = statistics.median(new_input)
    return res


# Scrodinger's parameters
rand_input = []

digits = []
cases_by_million = int(cases/1000000)
# print(cases_by_million)

while cases_by_million > 0:
    d = cases_by_million % 2
    digits.append(d)
    cases_by_million = cases_by_million//2
digits.reverse()
# print(digits)

# Update LED lights
while True:
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(1)
    for i in range(len(digits)):
        if digits[i] == 1:
            pixels[i] = (255, 0, 0)
    pixels.show()
    time.sleep(1)





