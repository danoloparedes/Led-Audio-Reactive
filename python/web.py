# import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import time
import subprocess
import sys

def ReadJson():
    with open("led_status.json","r") as openfile:
        estado = json.load(openfile)   
    return estado

# def visualization():
#     print("inicio vis")
#     while True:
#         print(ReadJson())
#         time.sleep(3)

def write_json(estado):
    json_update = {"estado":estado}
    with open("led_status.json","w") as file:
        json.dump(json_update,file)
def kill(self):
    print("kill")
    self.killed = True

# host_name = '192.168.1.158'
def control():
    global x
    x = 'Scroll'
    
    # # x = threading.Thread(target=visualization)
    # x.start()

    # host_name = '192.168.1.135'
    host_name = '192.168.0.107'
    # host_name = 'localhost'
    host_port = 8000
    with open('control.html','r') as f:
        html_string = f.read()

    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            global x

            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()

            self.wfile.write(bytes(html_string,"utf-8"))

            if self.path.find("Scroll=Scroll") != -1:
                write_json("Scroll")
            elif self.path.find("Energy=Energy") != -1:
                write_json("Energy")
            elif self.path.find("Spectrum=Spectrum") != -1:
                write_json("Spectrum")
            elif self.path.find("Fade=Fade") != -1:
                write_json("Fade")
            elif self.path.find("Rainbow=Rainbow") != -1:
                write_json("Rainbow")
            # fakefunc.visualization
            elif self.path.find("cancel") != -1:
                print('pog')


    server = HTTPServer((host_name, host_port), MyServer)
    print("Server now running...")

    server.serve_forever()
    server.server_close()
    print("Server Stopped!")
