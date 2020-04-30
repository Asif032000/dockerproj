
import sys 
import os 

cont = sys.argv[1]
print("Output from Python") 
print("\ncontainer name: " + cont)  

print("\ndeleting container...........",sys.argv[1])
os.system('systemctl start docker')

os.system('docker rm -f {}'.format(sys.argv[1]))
os.system('docker ps')

os.system('node app.js')
