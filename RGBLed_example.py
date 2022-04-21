from RGBLed_lib import RGBLed

myRGB = RGBLed(15,14,13,RGBLed.anode)

"""
myRGB = RGBLed(#Red pin,#Green pin, #Blue pin,#RGB Led type -anode or cathode)
myRGB.off() -              Turn off all colors
myRGB.set(120,50,75)       Set color Set(#Red Led,#Green Led,#Blue Led)  
myRGB.slowSet(10,200,195)  Set color slowly SlowSet(#Red Led,#Green Led,#Blue Led,#delay - optional)
myRGB.show()               Show last color values
myRGB.white()              Set RGB led to white (255,255,255)
myRGB.yellow()             Set RGB led to yellow (255,255,0)
myRGB.magenta()            Set RGB led to magenta (255,0,255)
myRGB.cyan()               Set RGB led to cyan (0,255,255)  
"""
while True:
    myRGB.slowSet(0,0,0)
    myRGB.slowSet(255,255,255)
