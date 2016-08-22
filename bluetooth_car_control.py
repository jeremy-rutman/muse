from bluetooth import *
#sudo apt-get install bluetooth libbluetooth-dev
#sudo pip install pybluez



from pprint import pprint

devices = discover_devices()
print devices
