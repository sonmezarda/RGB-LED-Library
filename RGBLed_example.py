from RGBLed_lib import RGBLed

myRGB = RGBLed(15,14,13,RGBLed.Anode)

"""
myRGB = RGBLed(#Red pin,#Green pin, #Blue pin,#RGB Led type -Anode or Cathode)
myRGB.Off() -              Turn off all colors
myRGB.Set(120,50,75)       Set color Set(#Red Led,#Green Led,#Blue Led)  
myRGB.SlowSet(10,200,195)  Set color slowly SlowSet(#Red Led,#Green Led,#Blue Led,#delay - optional)
myRGB.Show()               Show last color values
myRGB.White()              Set RGB led to white (255,255,255)
myRGB.Yellow()             Set RGB led to yellow (255,255,0)
myRGB.Magenta()            Set RGB led to magenta (255,0,255)
myRGB.Cyan()               Set RGB led to cyan (0,255,255)  
"""
while True:
    myRGB.SlowSet(0,0,0)
    myRGB.SlowSet(255,255,255)
