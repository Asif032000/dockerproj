
import sys 
import os 

cont = sys.argv[1]

print("Output from Python") 
print("\ncontainer name: " + cont) 


print("\nremovinga all containers.....")
os.system('systemctl start docker')

os.system('docker rm -f $(docker ps -aq)')

os.system('docker ps')

os.system('node app.js')


