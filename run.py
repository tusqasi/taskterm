from defs import Task
from time import sleep, gmtime, strftime
 

c = 1      #initializing vars
tasks = [] #

while True: #main program loop
	ct = strftime("%H-%M-%S", gmtime())
	prmt = str(input("'a' for adding new task\
					\n'l' for listing all tasks\
					\n'c' for changing a task\
					\n'q' for exiting program\n")) 
	
	if prmt == 'a':
		#c+=1
		c = Task.add_task(tasks,c ,ct) 
		#appends a task to tasks
	elif prmt == 'l':
		if c == 0: print("No tasks")	# careful here
		#lists tasks	
		else:	
			for taskl in tasks:
				print(("No.{serial}\
					  \nName:{name}\
					  \nDuration:{duration}\
					  \nDescription:{description}\
					  \n").format(serial=taskl.ind,
					   			  name=taskl.name, 
					   			  duration=taskl.dur,
					   			  description=taskl.desc))
				sleep(0.5)
	elif prmt == 'q':
		print("Bye User")
		break
	elif prmt == 'c':
		#changes task
		s = str(input("Which task(No.) and \
					 \nwhat (name, dur(ation) or desc(ription))\
					 \n('|' separated)\n")).split('|', 1)
		if s[1] == 'name':
			tasks[s[0]].set_name(s[1])
		elif s[1] == 'dur':
			tasks[s[0]].set_dur(s[1])
		elif s[1] == 'desc':
			tasks[s[0]].set_desc(s[1])

	else:
		print("{} not defined".format(prmt))