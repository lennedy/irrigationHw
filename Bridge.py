import logging
import signal

from Valve import Valve
from MyButton import MyButton
from MyLed import MyLed

from pyhap.accessory import Accessory, Bridge
from pyhap.accessory_driver import AccessoryDriver
import pyhap.loader as loader

from gpiozero import LED
from Pins import Pins

def get_bridge(driver):
    """Call this method to get a Bridge instead of a standalone accessory."""
    pins = Pins("Enable")
    bridge = Bridge(driver, 'Bridge')
    button1    = MyButton(pins.buttonValve1())
    button2    = MyButton(pins.buttonValve2())
    buttonTemp = MyButton(pins.buttonValve3())
    buttonOff  = MyButton(pins.buttonAllOff()) #This is not configured yet

    led1  = MyLed(pins.ledValve1())
    led2  = MyLed(pins.ledValve2())

    valv1 = Valve("Valve1", pins.releValve1(), driver, 'MyValve1')
    valv2 = Valve("Valve2", pins.releValve2(), driver, 'MyValve2')
    valv1.appendButtonOnOff(button1)
    valv1.appendLed(led1)
    valv2.appendButtonOnOff(button2)
    valv2.appendLed(led2)
    

    valv1.appendButtonOff(buttonOff)
    valv2.appendButtonOff(buttonOff)

    led = MyLed(pins.ledSystem())
    led.blink()

    bridge.add_accessory(valv1)
    bridge.add_accessory(valv2)

    return bridge


#def get_accessory(driver):
#    """Call this method to get a standalone Accessory."""
#    return Valve("Valve", -1, driver, 'MyValve')


# Start the accessory on port 51826
driver = AccessoryDriver(port=51831)

# Change `get_accessory` to `get_bridge` if you want to run a Bridge.
driver.add_accessory(accessory=get_bridge(driver))

# We want SIGTERM (terminate) to be handled by the driver itself,
# so that it can gracefully stop the accessory, server and advertising.
signal.signal(signal.SIGTERM, driver.signal_handler)

# Start it!
driver.start()
