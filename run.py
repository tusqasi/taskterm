from defs import Task

c = 0
tasks = []

while True:
	if c == 0:
		prmt = str(input("'a' for adding new task\
						\n'l' for listing all tasks\
						\n'c' for changing a task\n")) 
	
	else:
		prmt = str(input("'l' for listing all tasks\
						 \n'c' for changing a task\
						 \n'q' to exit\n"))	


	if prmt == 'a':
		c+=1
		usrn, usrdu ,usrds = str(input("name:duration:description\
								 	   \n(separated by colons)\
								 	   \n")).split(":" , 2)
		tasks.append(Task(name=usrn, dur=usrdu, desc=usrds))

	elif prmt == 'l':
		print("all tasks:\n")
		if c == 0: print("No tasks")	# careful here
		
		else:	
			for task in tasks:
				print("No.{serial}\n\
					  \nName:{name}\
					  \nDuration:{duration}\
					  \nDescription{description}\
					  \n").format(serial=c,
					   			  name=tasks[c].name, 
					   			  duration=tasks[c].dur,
					   			  description=tasks[c].desc)

	elif prmt == 'q':
		break


		
