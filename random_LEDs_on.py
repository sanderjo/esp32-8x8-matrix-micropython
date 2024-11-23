import machine, neopixel, random, time

np = neopixel.NeoPixel(machine.Pin(14), 64) # Pin 14 is the 8x8 matrix, and 8x8=64 pixels in total

for times in range(30):
   
    # turn all LEDs off
    for pixel in range(64):
        np[pixel]=(0,0,0)
    np.write()

    # prepare the LEDs
    for i in range(random.randint(4,40)):
        pixel = random.randint(0,63)
        randomcolor = (random.randint(0,2), random.randint(0,2), random.randint(0,2))
        np[pixel] = randomcolor

    np.write() # turn the LEDs on

    time.sleep(2)
