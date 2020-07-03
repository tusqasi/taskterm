from defs import Task

c = 0
tasks = []

while True:
	if c == 0:
		prmt = str(input("'a' for adding new task\n'l' for listing all tasks\n
			             'c' for changing a task")) 