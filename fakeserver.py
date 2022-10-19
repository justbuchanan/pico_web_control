from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import threading
import time

from pins import PinInfo

pinstates = {}
for p in PinInfo:
    pstate = {'value': False}
    if p['type'] == 'digitalio':
        pstate['inout'] = 'In'
    pinstates[p['id']] = pstate
pinstates['LED'] = {'value': False, 'inout': 'Out'}


class FakePicoWServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # logging.info("GET request,\nPath: %s", str(self.path))

        # serve index.html and "/"
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
            print('returned index')
            return

        # serve pico.svg
        if self.path == "/pico.svg":
            self.send_response(200)
            self.send_header('Content-type', 'image/svg+xml')
            self.end_headers()
            with open('pico.svg', 'rb') as file:
                self.wfile.write(file.read())
            return

        # serve pin states json
        if self.path == "/pinstates":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(pinstates).encode('utf-8'))
            return

        # serve pin spec json
        if self.path == "/pininfo":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(PinInfo).encode('utf-8'))
            return

        # not found
        logging.warning("GET request for invalid path: %s" % self.path)
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        updateInfo = json.loads(post_data.decode('utf-8'))
        logging.info("/update called with info: %s" % str(updateInfo))
        pinID = updateInfo['id']

        if pinID in pinstates:
            pinstates[pinID]['value'] = updateInfo['value']
            pinstates[pinID]['inout'] = updateInfo['inout']

            logging.info("set pinstates[%s] to %s" %
                         (updateInfo['id'], str(pinstates[pinID])))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        else:
            console.log("Attempt to update invalid pin: %s" % pinID)
            self.send_response(404)  # pin not found


def toggle_pin_forever(pinID):
    while True:
        time.sleep(3)
        pinstates[pinID]['value'] = not pinstates[pinID]['value']


def run(port=8080):
    httpd = HTTPServer(('', port), FakePicoWServer)
    logging.info('Starting httpd...\n')

    # periodically toggle a gpio pin on and off so we can test that the UI actually updates
    thread = threading.Thread(target=toggle_pin_forever, args=["GP5"])
    thread.daemon = True
    thread.start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
