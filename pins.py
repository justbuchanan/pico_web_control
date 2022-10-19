# this module contains details on each pin on the pico w. It is used by both the
# real server and the demo server, so it's important that it not depend on
# anything specific to CircuitPython.

# pin information.
# TODO: consider dropping name field.
# TODO: consider changing 'type' to a bool is_gpio?
PinInfo = [
    # left side of board in top-down order
    {"id": "GP0", "name": "GP0", "type": "digitalio"},
    {"id": "GP1", "name": "GP1", "type": "digitalio"},
    {"id": "GND0", "name": "GND", "type": "gnd"},
    {"id": "GP2", "name": "GP2", "type": "digitalio"},
    {"id": "GP3", "name": "GP3", "type": "digitalio"},
    {"id": "GP4", "name": "GP4", "type": "digitalio"},
    {"id": "GP5", "name": "GP5", "type": "digitalio"},
    {"id": "GND1", "name": "GND", "type": "gnd"},
    {"id": "GP6", "name": "GP6", "type": "digitalio"},
    {"id": "GP7", "name": "GP7", "type": "digitalio"},
    {"id": "GP8", "name": "GP8", "type": "digitalio"},
    {"id": "GP9", "name": "GP9", "type": "digitalio"},
    {"id": "GND2", "name": "GND", "type": "gnd"},
    {"id": "GP10", "name": "GP10", "type": "digitalio"},
    {"id": "GP11", "name": "GP11", "type": "digitalio"},
    {"id": "GP12", "name": "GP12", "type": "digitalio"},
    {"id": "GP13", "name": "GP13", "type": "digitalio"},
    {"id": "GND3", "name": "GND", "type": "gnd"},
    {"id": "GP14", "name": "GP14", "type": "digitalio"},
    {"id": "GP15", "name": "GP15", "type": "digitalio"},

    # right side of board in bottom-up order
    {"id": "GP16", "name": "GP16", "type": "digitalio"},
    {"id": "GP17", "name": "GP17", "type": "digitalio"},
    {"id": "GND3", "name": "GND", "type": "gnd"},
    {"id": "GP18", "name": "GP18", "type": "digitalio"},
    {"id": "GP19", "name": "GP19", "type": "digitalio"},
    {"id": "GP20", "name": "GP20", "type": "digitalio"},
    {"id": "GP21", "name": "GP21", "type": "digitalio"},
    {"id": "GND2", "name": "GND", "type": "gnd"},
    {"id": "GP22", "name": "GP22", "type": "digitalio"},
    {"id": "RUN0", "name": "RUN", "type": "run"},
    {"id": "GP26", "name": "GP26", "type": "digitalio"},
    {"id": "GP27", "name": "GP27", "type": "digitalio"},
    {"id": "GND2", "name": "GND", "type": "gnd"},
    {"id": "GP28", "name": "GP28", "type": "digitalio"},
    {"id": "ADC", "name": "ADC_VREF", "type": "adc_vref"},
    {"id": "VOUT", "name": "3V3(OUT)", "type": "v"},
    {"id": "V", "name": "3V3_EN", "type": "v"},
    {"id": "GND3", "name": "GND", "type": "gnd"},
    {"id": "VSYS", "name": "VSYS", "type": "vsys"},
    {"id": "VBUS", "name": "VBUS", "type": "vbus"},
]
