class Pins:

  def __init__(self, status):
    PIN_DESABILITADO = -1

    self.__PIN_RELE_VALVE1= PIN_DESABILITADO
    self.__PIN_RELE_VALVE2= PIN_DESABILITADO
    self.__PIN_RELE_VALVE3= PIN_DESABILITADO
    self.__PIN_RELE_MOTOR1= PIN_DESABILITADO
    
    self.__PIN_LED_VALVE1 = PIN_DESABILITADO
    self.__PIN_LED_VALVE2 = PIN_DESABILITADO
    self.__PIN_LED_VALVE3 = PIN_DESABILITADO
    self.__PIN_LED_MOTOR1 = PIN_DESABILITADO
    self.__PIN_LED_SYSTEM = PIN_DESABILITADO
  
    self.__PIN_BOTAO_VALVE1 = PIN_DESABILITADO
    self.__PIN_BOTAO_VALVE2 = PIN_DESABILITADO  
    self.__PIN_BOTAO_VALVE3 = PIN_DESABILITADO
    self.__PIN_BOTAO_ALL_OFF= PIN_DESABILITADO
    
    if(status == "Enable"):
      self.__PIN_RELE_VALVE1= 20
      self.__PIN_RELE_VALVE2= 21
      self.__PIN_RELE_VALVE3= 19
      self.__PIN_RELE_MOTOR1= 13
      
      self.__PIN_LED_VALVE1 = 23
      self.__PIN_LED_VALVE2 = 24
      self.__PIN_LED_VALVE3 = 25      
      self.__PIN_LED_MOTOR1 = 12
      self.__PIN_LED_SYSTEM = 16

      self.__PIN_BOTAO_VALVE1 = 17
      self.__PIN_BOTAO_VALVE2 = 22
      self.__PIN_BOTAO_VALVE3 = 5
      self.__PIN_BOTAO_ALL_OFF= 6
      
  #####################################    
  def releValve1(self):
    return self.__PIN_RELE_VALVE1

  def releValve2(self):
    return self.__PIN_RELE_VALVE2    

  def releValve3(self):
    return self.__PIN_RELE_VALVE3
    
  def releMotor1(self):
    return self.__PIN_RELE_MOTOR1    
  #####################################
  #####################################
  def ledValve1(self):
    return self.__PIN_LED_VALVE1
  
  def ledValve2(self):
    return self.__PIN_LED_VALVE2        

  def ledValve3(self):
    return self.__PIN_LED_VALVE3
            
  def ledMotor1(self):
    return self.__PIN_LED_MOTOR1
    
  def ledSystem(self):
    return self.__PIN_LED_SYSTEM
  #####################################  
  #####################################
  def buttonValve1(self):
    return self.__PIN_BOTAO_VALVE1
    
  def buttonValve2(self):
    return self.__PIN_BOTAO_VALVE2
    
  def buttonValve3(self):
    return self.__PIN_BOTAO_VALVE3
    
  def buttonAllOff(self):
    return self.__PIN_BOTAO_ALL_OFF
  #####################################
