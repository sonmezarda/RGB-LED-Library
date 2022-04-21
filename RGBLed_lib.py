#rgb led lib

from machine import PWM, Pin
import utime

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class RGBLed:
    anode = 'anode'
    cathode = 'cathode'
    
    def __init__(self, rPin, gPin, bPin, ledType, currentValueR = 0, currentValueG = 0, currentValueB=0):
        self.rPin = rPin
        self.gPin = gPin
        self.bPin = bPin
        self.ledType = ledType
        self.currentValueR = currentValueR
        self.currentValueG = currentValueG
        self.currentValueB = currentValueB
        self.Set(currentValueR,currentValueG,currentValueB)
     
    def show(self):
        print("Red Pin:", self.rPin)
        print("Green Pin:", self.gPin)
        print("Blue Pin:", self.bPin)
        print("Led Type:",self.ledType)
        print("Current Red Value:",self.currentValueR)
        print("Current Green Value:",self.currentValueG)
        print("Current Blue Value:",self.currentValueB)
        
    def set(self,r,g,b):
        if self.ledType == 'anode':
            self.currentValueR = r
            self.currentValueG = g
            self.currentValueB = b
            
            r = convert(r,0,255,65534,0)
            g = convert(g,0,255,65534,0)
            b = convert(b,0,255,65534,0)
            rPWM = PWM(Pin(self.rPin))
            gPWM = PWM(Pin(self.gPin))
            bPWM = PWM(Pin(self.bPin))
            rPWM.duty_u16(r)
            gPWM.duty_u16(g)
            bPWM.duty_u16(b)
        elif self.ledType == 'cathode':
            self.currentValueR = r
            self.currentValueG = g
            self.currentValueB = b
            
            r = convert(r,0,255,0,65534)
            g = convert(g,0,255,0,65534)
            b = convert(b,0,255,0,65534)
            rPWM = PWM(Pin(self.rPin))
            gPWM = PWM(Pin(self.gPin))
            bPWM = PWM(Pin(self.bPin))
            rPWM.duty_u16(r)
            gPWM.duty_u16(g)
            bPWM.duty_u16(b)
    
    def off(self):
        self.Set(0,0,0)
        
    def white(self):
        self.Set(255,255,255)
    
    def yellow(self):
        self.Set(255,255,0)
    
    def magenta(self):
        self.Set(255,0,255)
    
    def cyan(self):
        self.Set(0,255,255)
        
    def slowSet(self,r,g,b,delay = 0.01):
        if r>self.currentValueR:
            rStep = 1
        else:
            rStep -= 1
        
        if g>self.currentValueG:
            gStep = 1
        else:
            gStep = -1
            
        if b>self.currentValueB:
            bStep = 1
        else:
            bStep = -1
            
        if self.ledType == 'anode':
            for i in range(self.currentValueR,r,rStep):
                x = convert(i,0,255,65534,0)
                rPWM = PWM(Pin(self.rPin))
                rPWM.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueG,g,gStep):
                x = convert(i,0,255,65534,0)
                gPWM = PWM(Pin(self.gPin))
                gPWM.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueB,b,bStep):
                x = convert(i,0,255,65534,0)
                bPWM = PWM(Pin(self.bPin))
                bPWM.duty_u16(x)
                utime.sleep(delay)
                
        elif self.ledType == 'cathode':
            for i in range(self.currentValueR,r,rStep):
                x = convert(i,0,255,0,65534)
                rPWM = PWM(Pin(self.rPin))
                rPWM.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueG,g,gStep):
                x = convert(i,0,255,0,65534)
                gPWM = PWM(Pin(self.gPin))
                gPWM.duty_u16(x)
                utime.sleep(delay)
            for i in range(self.currentValueB,b,bStep):
                x = convert(i,0,255,0,65534)
                bPWM = PWM(Pin(self.bPin))
                bPWM.duty_u16(x)
                utime.sleep(delay)
                
        self.currentValueR = r
        self.currentValueG = g
        self.currentValueB = b
        self.Set(r,g,b)
