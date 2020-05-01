
import sys 
import os 

cont = sys.argv[1]

print("Output from Python") 
print("\ncontainer name: " + cont) 


print("\ncontainer is running...........")
os.system('systemctl start docker')

os.system('docker start {}'.format(cont))

os.system('docker ps')

os.system('node app.js')
