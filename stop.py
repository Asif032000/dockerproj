
import sys 
import os 

cont = sys.argv[1]

print("Output from Python") 
print("\ncontainer name: " + cont) 


print("\nstopping the container...........")
os.system('systemctl start docker')

os.system('docker stop {}'.format(cont))

os.system('docker ps')

os.system('node app.js')
