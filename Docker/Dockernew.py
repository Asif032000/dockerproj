import os


def install():

	print('\nPlease make sure you have yum configured')

	z=1



	while z==1:
		ch = input('\nDo you want to continue?(y/n)\n')

		if str(ch) == 'y':
			print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Installing Docker , Please have patience++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

			
			
			os.system('''

			curl  https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo


			yum install docker-ce --nobest -y

			
			''')
			z=0
		elif str(ch) == 'n':
			print('\nOK , configure yum first\n')
			z=0	

		else:
			print('\nPress y or n\n')
	
	
	pull()
	new_cont()
	start()
	enter()
	


#pulling an image 


def pull():

	ch = input('want to pull an image?(y/n)\n')

	if str(ch) == 'y':
		nameos = input('Which os image would you like to install?\n')
		versionch = input('Do you want a specific version?(y/n)\n')
		if str(versionch) == 'y':
			version = input('which version?\n')
		else:
			version = 'latest'
		os.system('docker pull {}:{}'.format(nameos,version))
		print('\nImage downloaded\n')
	else:
		print("It's your choice \n")
		


#creating a container

def new_cont():

	inkk = input('Want to create a container?(y/n)\n')
	if str(inkk)== 'y':
		name = input('What name would you like to give to your container?\n')
		image = input('Which image would you like to use?\n')
		version_ch = input('Would you like to choose a specific version?(y/n)\n')
		if str(version_ch) == 'y':
			version = input('Which version?\n')
		else:
			version = 'latest'
			
		print('\nCreating a new container:{}'.format(name))
		os.system('docker run -dit --name {} {}:{}'.format(name,image,version))
		
		return name

	else:
		print('\nOk , we will create container later\n')
	

#starting a container
def start():
	start_ch = input('\nWould you like to start a container?(y/n)\n')
	if str(start_ch) == 'y':
		print('/Available containers are:\n\n')
		os.system('docker ps -a')
		
		container_ch = input('\nWhich container would you like to enter in?\n')
		os.system('docker start {}'.format(container_ch))
		print('\n {} started'.format(container_ch))
		print('IP details of container are:')
		ret_value = os.system('docker exec {} ifconfig'.format(container_ch))
		if int(ret_value) == 0:
			os.system('docker exec {} ifconfig'.format(container_ch))
		else:
			return 0
	else:
		print('choose another option from menu')
	


#Entering a container
def enter():

	enter_ch  = input('\nWould you like to enter a container?(y/n)\n')
	if str(enter_ch) == 'y':
		print('\nAvailable containers are:\n\n')
		os.system('docker ps -a ')
		
		container_ch = input('\nWhich container would you like to enter in?\n')
		os.system('docker start {}'.format(container_ch))
		os.system('docker attach {}'.format(container_ch))
	else:
		print('\nSee ya next time...........')


#Deleting a container
def delete():
	print('Available Containers are:\n')
	os.system('docker ps -a')
	os_name = input('\nWhich container would you like to Delete?')
	os.system('docker rm {}'.format(os_name))


#Stopping a container
def stop():
	print('Available Containers are:\n')
	os.system('docker ps -a')
	os_name = input('\nWhich container would you like to stop?')
	os.system('docker stop {}'.format(os_name))
	print('\b stopped')


#Available Containers

def show():
	os.system('docker ps -a')


#Configuring web server in container


def web():
	print('Make sure SElinux and firewall are disabled in base OS. You can disable them after installation but make sure to restart container\n')
	print('\nAvailable containers are:')
	os.system('docker ps -a')
	os_ch = input('''
			Please make a choice:
			1. Create a new container.
			2. Use an existing container.
			3. Exit  \n''')
			
	if int(os_ch) == 1 :
		print('do something')
		os_name = new_cont()
		rem_part_config(os_name)
	elif int(os_ch) == 2:
	
		os_name = input('\nIn which container do you want to configure web server?\n')
		rem_part_config(os_name)
	elif int(os_ch) == 3:
		return 0
	else:
		print('That is invalid')



#Remove container
def remove():
	print('You have these containers:')
	os.system('docker ps -a')
	cont_name = input('\n Enter the name of the container to remove:\n')
	os.system('docker rm -f {}'.format(cont_name))


#Removing all containers

def removeAll():
	confirm = input('*******WARNING**********\n All the containers will be removed. Do you want to go ahead?(y/n)\n')
	if str(confirm) == 'y':
		os.system('docker rm -f $(docker container ls -a -q)')
	else:
		print('Always Be careful')	


#Committing an image from a container

def commit():
	print('\nThese are the containers you have:\n')
	os.system('docker ps -a')
	os_name = input('\nWhich container would you like to commit?\n')
	image_name = input('\nName of the image?')
	os.system('docker commit {} {}'.format(os_name,image_name))
		



#REmaining config

def rem_part_config(os_name):
	os.system("docker start {}".format(os_name))
	os.system("docker exec -it {} bash -c 'yum install httpd -y'".format(os_name))
	os.system("docker exec -it {} bash -c 'yum install net-tools -y'".format(os_name))
	os.system('''docker exec {} bash -c "echo 'rm -rf /var/run/httpd/*  \n /usr/sbin/httpd' >> /root/.bashrc"'''.format(os_name))
	os.system("docker restart {}".format(os_name))
	print('\nSuccessfully configured webserver in {}'.format(os_name))
	
	file_ch = input('Want to create an html file to check your server?(y/n)\n')
	if str(file_ch) == 'y':
		print('This file will be saved in /var/www/html  as index.html')
		os.system("docker exec -it {} bash -c 'vi /var/www/html/index.html'".format(os_name))
		print('You can check the web server using using following details of {}\n'.format(os_name))
		os.system('docker exec {} ifconfig'.format(os_name))
	else:
		print('You can create it later.........TATA')
		
	commit = input('Do you want to commit this webserver?')
	if str(commit) == 'y':
		image_name = input('What name would you like to give to this image?')
		os.system('docker commit {} {}'.format(os_name,image_name))




	

