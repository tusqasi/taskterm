from defs import Task

c = 0
tasks = []

while True:
	if c == 0:
		prmt = str(input("'a' for adding new task\n'l' for listing all tasks\n'c' for changing a task\n")) 
	
	else:
		prmt = str(input("'l' for listing all tasks\n'c' for changing a task"))	


	if prmt == 'a':
		c+=1
		usrn, usrdu ,usrds = str(input("name:duration:description (separated by colons)")) 
		tasks.append(Task(name=usrn, dur=usrdu, desc=usrds, ind=c))

	
