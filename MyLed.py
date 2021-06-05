from gpiozero import LED
from MyDevice import MyDevice
##########################################################
class SimulatedLed:
  def __init__(self,pin):
    self.__pin = pin
    self.__ledState = False

  def on(self):
    self.__ledState = True
  def off(self):
    self.__ledState = False
  def blink(self,a1,a2):
    a=0
##########################################################
class MyLed(MyDevice):
  def __init__(self, pin=-1):
    super().__init__(pin)
    self.__periodo = 0.25

    if self.isEnable():
      self.__led = LED(pin)
    else:
      self.__led = SimulatedLed(pin)

  def blink(self):
    self.__led.blink(self.__periodo,self.__periodo)

  def on(self):
    self.__led.on()

  def off(self):
    self.__led.off()



