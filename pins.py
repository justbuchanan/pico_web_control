# this module contains details on each pin on the pico w. It is used by both the
# real server and the demo server, so it's important that it not depend on
# anything specific to CircuitPython.

PinInfo = [
    # left side of board in top-down order
    {"id": "GP0", "is_gpio": True},
    {"id": "GP1", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP2", "is_gpio": True},
    {"id": "GP3", "is_gpio": True},
    {"id": "GP4", "is_gpio": True},
    {"id": "GP5", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP6", "is_gpio": True},
    {"id": "GP7", "is_gpio": True},
    {"id": "GP8", "is_gpio": True},
    {"id": "GP9", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP10", "is_gpio": True},
    {"id": "GP11", "is_gpio": True},
    {"id": "GP12", "is_gpio": True},
    {"id": "GP13", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP14", "is_gpio": True},
    {"id": "GP15", "is_gpio": True},

    # right side of board in bottom-up order
    {"id": "GP16", "is_gpio": True},
    {"id": "GP17", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP18", "is_gpio": True},
    {"id": "GP19", "is_gpio": True},
    {"id": "GP20", "is_gpio": True},
    {"id": "GP21", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP22", "is_gpio": True},
    {"id": "RUN", "is_gpio": False},
    {"id": "GP26", "is_gpio": True},
    {"id": "GP27", "is_gpio": True},
    {"id": "GND", "is_gpio": False},
    {"id": "GP28", "is_gpio": True},
    {"id": "ADC_VREF", "is_gpio": False},
    {"id": "3V3_OUT", "is_gpio": False},
    {"id": "3V3_EN", "is_gpio": False},
    {"id": "GND", "is_gpio": False},
    {"id": "VSYS", "is_gpio": False},
    {"id": "VBUS", "is_gpio": False},
]
