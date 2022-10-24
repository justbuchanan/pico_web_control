import socketpool
import wifi
import board
import digitalio
import json
import time

from adafruit_httpserver import HTTPServer, HTTPResponse

from secrets import secrets
from pins import PinInfo

# init all gpio pins to INPUT state and store in a dict mapped by id
pins = {}
for pininfo in PinInfo:
    if not pininfo["is_gpio"]:
        continue
    io = digitalio.DigitalInOut(getattr(board, pininfo["id"]))
    io.direction = digitalio.Direction.INPUT
    pins[pininfo["id"]] = io

# handle LED separately from the other pins - it's always an output and it's not
# really a pin (it's actually connected to the wifi module and not the main
# chip)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
pins["LED"] = led

# connect to wifi
ssid = secrets['WIFI_SSID']
print()
print("Connecting to", ssid)
wifi.radio.connect(ssid, secrets['WIFI_PASSWORD'])
print("Connected to", ssid)
print(f"Listening on http://{wifi.radio.ipv4_address}:80")

# http server
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)


@server.route("/")
def base(request):
    return HTTPResponse(filename="/index.html")


@server.route("/pico.svg")
def svg(request):
    # TODO: set headers so that this is cached by the browser. It's a large file
    # and takes a long time to load from the pi. Since it doesn't change much
    # (ever), don't re-transfer it on every page load.
    return HTTPResponse(filename="/pico.svg")


@server.route("/update", method="POST")
def update(request):
    ur = json.loads(request.request_data)
    print("got update request: %s" % str(request))
    pin = pins[ur['id']]
    pin.direction = digitalio.Direction.INPUT if ur[
        'inout'] == 'IN' else digitalio.Direction.OUTPUT
    if pin.direction == digitalio.Direction.OUTPUT:
        pin.value = ur['value']

    return HTTPResponse(body="done")


@server.route("/pinstates")
def pinstates(request):
    states = {}
    for pinID, pin in pins.items():
        states[pinID] = {
            "id": pinID,
            "inout":
            'In' if pin.direction == digitalio.Direction.INPUT else 'Out',
            "value": pin.value,
        }
    return HTTPResponse(content_type="application/json",
                        body=json.dumps(states))


@server.route("/pininfo")
def pininfo(request):
    return HTTPResponse(content_type="application/json",
                        body=json.dumps(PinInfo))


# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))
