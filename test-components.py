import pyupm_i2clcd as lcd
import pyupm_grove as temp
import time
import mraa
import math

ecran = lcd.Jhd1313m1(0)
color = 0
red = mraa.Aio(0)
color = red.read()/10
degree = temp.GroveTemp(1)
a = degree.value()
resistance= float((1023-a)*10000/a)
temperature=1/(math.log(resistance/10000)/3975+1/298.15)-273.15
print degree.name()
print temperature
while 1:
        color = red.read()/10
        if color > 255:
                color = 255
        elif color < 0:
                color = 0

        ecran.clear()
        ecran.write(str(color) + 'toto')
        ecran.setColor(color, 0, 0)
