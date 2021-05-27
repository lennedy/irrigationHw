from gpiozero import Button

class MyDevice:
  def __init__(self, pin):
    self.__pin = pin
    if pin<0:
      self.__enable = False
    else:
      self.__enable = True

#********************************************************#
  def isEnable(self):
    return self.__enable
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

#********************************************************#
  def setPressed(self):
    self.__buttonPressed = True
    print("The button was pressed!")

#********************************************************#
  def wasPressed(self):
    if (not self.isEnable() ):
      return False

    buttonPressed        = self.__buttonPressed
    self.__buttonPressed = False

    return buttonPressed

#********************************************************#

#button = MyButton(5)
#while True:
#  a=0
