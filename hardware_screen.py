from rpi_backlight import Backlight

class HardwareScreen():

    def brightness (self):
        backlight = Backlight()
        backlight.brightness = 10
        return backlight



