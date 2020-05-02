import Dockernew
import os

while True:
	os.system('clear')
	print('===========================Welcome to Docker===================================')

	print('''

	 1. Install Docker.
	 2. Pull an Image.
	 3. Create a container
	 4. Enter a container
	 5. Start a container
	 6. Stop a container
	 7. Delete a container
	 8. Available Containers
	 9. Available Images
	10. Configure webserver in a container
	11. Commit an image
	12. Remove all the containers
	13. Remove a container
	14. Exit from the menu


	''')

	ch = input('What do you want to do?\n')

	if int(ch) == 1:
		Dockernew.install()
	elif int(ch) == 2:
		Dockernew.pull()
	elif int(ch) == 3:
		Dockernew.new_cont()
	elif int(ch) == 4:
		Dockernew.enter()
	elif int(ch) == 5:
		Dockernew.start()
	elif int(ch)== 6:
		Dockernew.stop()
	elif int(ch) == 7:
		Dockernew.delete()
	
	elif int(ch) == 8:
		Dockernew.show()
	elif int(ch) == 9:
		os.system('docker images')
	elif int(ch) == 10:
		Dockernew.web()
	elif int(ch) == 11:
		Dockernew.commit()
	
	elif int(ch) == 12:
		Dockernew.removeAll()
	
	elif int(ch) == 13:
		Dockernew.remove()
	elif int(ch) == 14:
		break
		os.system('exit')
	else:
		print('Invalid option')
	input('\n\n\nenter to continue')
		
