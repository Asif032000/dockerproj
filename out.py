
import sys 
import os 

cont = sys.argv[1]
image = sys.argv[2]
print("Output from Python") 
print("\ncontainer name: " + cont) 
print("\nimage name: " + image) 

print("\ncreating container...........")
os.system('systemctl start docker')

os.system('docker run -dit --name {} {}'.format(cont,image))

os.system('docker ps')

os.system('node app.js')
