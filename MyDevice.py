
class MyDevice:
  def __init__(self, pin):
    self.__pin = pin
    if pin<0:
      self.__enable = False
    else:
      self.__enable = True

  def isEnable(self):
    return self.__enable

