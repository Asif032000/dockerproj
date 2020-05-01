
import sys 
import os 
import time

image = sys.argv[1]

print("\nPulling Image...........",sys.argv[1])
os.system('systemctl start docker')

os.system('docker pull {}'.format(image))



