from defs import Task

c = 0
tasks = []

while True:
	if c == 0:
		prmt = str(input("'a' for adding new task\n'l' for listing all tasks\n'c' for changing a task\n")) 
	
	else:
		prmt = str(input("'l' for listing all tasks\n'c' for changing a task\n'q' to exit\n"))	


	if prmt == 'a':
		c+=1
		usrn, usrdu ,usrds = str(input("name:duration:description (separated by colons)\n")).split(":" , 2)
		tasks.append(Task(name=usrn, dur=usrdu, desc=usrds))

	elif prmt == 'l':
		
		print("all tasks:\n")
		for task in tasks:
			print("No.{serial}\nName:{name}\nDuration:{duration}\nDescription{description}").format(serial=,  )
		elif prmt == 'q':
		break


		
