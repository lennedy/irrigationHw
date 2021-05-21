from gpiozero import Button

class MyDevice:
  def __init__(self, pin):
    self.pin = pin
    if pin<0:
      self.enable = False
    else:
      self.enable = True

  def isEnable(self):
    return self.enable

class SimulatedButton:
  def __init__(self, pin):
    self.pin = pin

class MyButton(MyDevice):

  def __init__(self, pin=-1):
    super().__init__(pin)
    self.buttonPressed = False

    if self.isEnable():
      self.button = Button(pin)
      self.button.when_pressed  = self.setPressed
    else:
      self.button = SimulatedButton(pin)

  def setPressed(self):
    self.buttonPressed =True
    print("The button was pressed!")

  def wasPressed(self):
    buttonPressed      = self.buttonPressed
    self.buttonPressed = False
    return buttonPressed


#button = MyButton(5)
#while True:
#  a=0
