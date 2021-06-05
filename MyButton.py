from gpiozero import Button
from MyDevice import MyDevice
from MyLed import MyLed

##########################################################
class SimulatedButton:
  def __init__(self, pin):
    self.pin = pin
##########################################################
class MyButton(MyDevice):

  def __init__(self, pin=-1):
    super().__init__(pin)
    self.__buttonPressed = False

    if self.isEnable():
      self.button = Button(pin)
      self.button.when_pressed  = self.setPressed
    else:
      self.button = SimulatedButton(pin)

    self.led = MyLed()

#********************************************************#
  def setPressed(self):
    self.__buttonPressed = True
    if self.led.isEnable():
      self.led.blink()
    print("The button was pressed!")

#********************************************************#
  def wasPressed(self):
    if (not self.isEnable() ):
      return False

    buttonPressed        = self.__buttonPressed
    self.__buttonPressed = False

    return buttonPressed

#********************************************************#
  def appendLed(self, led):
    self.led = led
#********************************************************#
#button = MyButton(5)
#while True:
#  a=0
