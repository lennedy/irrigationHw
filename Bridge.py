from Valve import Valve

#def get_bridge(driver):
#    """Call this method to get a Bridge instead of a standalone accessory."""
#    bridge = Bridge(driver, 'Bridge')
#    temp_sensor = TemperatureSensor(driver, 'Sensor 2')
#    temp_sensor2 = TemperatureSensor(driver, 'Sensor 1')
#    bridge.add_accessory(temp_sensor)
#    bridge.add_accessory(temp_sensor2)

#    return bridge


def get_accessory(driver):
    """Call this method to get a standalone Accessory."""
    return Valve("Valve", -1, driver, 'MyValve')


# Start the accessory on port 51826
driver = AccessoryDriver(port=51831)

# Change `get_accessory` to `get_bridge` if you want to run a Bridge.
driver.add_accessory(accessory=get_accessory(driver))

# We want SIGTERM (terminate) to be handled by the driver itself,
# so that it can gracefully stop the accessory, server and advertising.
signal.signal(signal.SIGTERM, driver.signal_handler)

# Start it!
driver.start()
