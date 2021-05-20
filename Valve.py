import time

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SPRINKLER

class Relay:
  def __init__(self):
    self.value = False
    
class Timer:
  def __init__(self):
    self.value=0
  def init(self, duration):
    self.value=time.time()+duration;
    
  def timeToFinish(self):
    if ( self.value > time.time() ):
      return self.value - time.time()
    else:
      return 0
    
  def isFinished(self):
  	return ( self.value < time.time() )

class Valve(Accessory):
    """Implementation of a mock light accessory."""

    category = CATEGORY_SPRINKLER  # This is for the icon in the iOS Home app.

    def __init__(self, name, pin, *args, **kwargs):
        """Here, we just store a reference to the on and brightness characteristics and
        add a method that will be executed every time their value changes.
        """
        # If overriding this method, be sure to call the super's implementation first.
        super().__init__(*args, **kwargs)

        # variable to server
        self._state        = False
        self._valveType    = 1
        self._inUse        = 1
        self._duration     = 60
        self.timer = Timer()
        self._active = False
        
        # Add the services that this Accessory will support with add_preload_service here        
        serv_valve             = self.add_preload_service('Valve', chars=['Active', 'InUse', 'ValveType', 'SetDuration', 'RemainingDuration', "Name"])
        self.char_type         = serv_valve.configure_char('ValveType', value=self._valveType)
        self.char_active       = serv_valve.configure_char('Active', value=self._state)
        self.char_inUse        = serv_valve.configure_char('InUse', value=self._inUse)
        self.char_duration     = serv_valve.configure_char('SetDuration', value=self._duration)
        self.char_remainingDur = serv_valve.configure_char('RemainingDuration', value=0)
        self.char_name = serv_valve.configure_char('Name', value=name)        

        serv_valve.setter_callback = self._set_chars

        # variable to Hardware   
        if(pin<0):
            self._relay = Relay()
        else:
            self._relay = DigitalOutputDevice(pin=pin, active_high=active_high, initial_value=initial_value)

    def openHw(self):
        self._relay.value = 1
        self._active = True
        
    def closeHw(self):
        self._relay.value = 0      
        self._active = False
        
    def openGUI(self):
        self.char_active.set_value(1)
        self.char_inUse.set_value(1)
        self.char_remainingDur.set_value(round(self.timer.timeToFinish()))
        
    def closeGUI(self):
        self.char_active.set_value(0)
        self.char_inUse.set_value(0) 
        self.char_remainingDur.set_value(0)
        

    def print(self):
#        print ("Nome: "+self.name)
        print ("************************")
        print ("Name: ",self.char_name.get_value())
        print ("State: ",self._state)
        print ("Active: ",self._active)
        print ("Timer: ", self.timer.timeToFinish())
        print ("Remaining Duration: ",self.char_remainingDur.get_value())
        print ("########################")        

    def _set_chars(self, char_values):
        """This will be called every time the value of the on of the
        characteristics on the service changes.
        """
        if "Active" in char_values:
            print('On changed to: ', char_values["Active"])
            self._state = char_values["Active"]
            
        if "SetDuration" in char_values:
            self._duration = char_values["SetDuration"]
            
    @Accessory.run_at_interval(3)  # Run this method every 3 seconds
    # The `run` method can be `async` as well
    def run(self):
        """This method runs every 3 seconds.
        """        
      
        
        if self._state:
            if (self._active==False):
                self.timer.init(self._duration)
            self.openHw()
            self.openGUI()

        else:
            self.closeHw()
            self.closeGUI()

        if self.timer.isFinished() & self._active:
            self._state = 0       
            self.closeHw()
            self.closeGUI()        
           
        self.print()


    # The `stop` method can be `async` as well
    def stop(self):
        """We override this method to clean up any resources or perform final actions, as
        this is called by the AccessoryDriver when the Accessory is being stopped.
        """
        print('Stopping accessory.')

