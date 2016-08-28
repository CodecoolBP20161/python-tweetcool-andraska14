import argparse
import ipaddress
import requests
import time
from userinterface import *

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host",
                    help="IP address of the Tweetcool server",
                    default='127.0.0.1')  # Equals 'localhost'
parser.add_argument("-P", "--port",
                    help="Post used by the Tweetcool server",
                    type=int,
                    default=9876)
args = parser.parse_args()

try:
    server = {
        'host': ipaddress.ip_address(args.host),
        'port': args.port
    }
except ValueError as e:
    print('The given host is not a valid IP address')
    exit(0)

if not(1024 < server["port"] < 65535):
    print('The given port number is not in the range between 1024 and 65535!')
    exit(0)

server["address"] = 'http://' + server["host"].compressed + ':' + str(server["port"])

#print(server['address'])# Logic starts here... somewhere..
#on= True

while Userinterface.on:
    Userinterface.login()
    if Userinterface.logged_in_user != None:
        ui = Userinterface(Userinterface.logged_in_user, server['address'])
        ui.run_app()
