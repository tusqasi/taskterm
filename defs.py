class Task:
	"""Make a task object"""

	def __init__(self, name="", dur="", desc="",ind=0, ct=""):
		if len(name)==0:self.name = "No Name given"		
		else:self.name = name

		if len(dur)==0:self.dur = "No Duration given"
		else:self.dur = dur 
		
		if len(desc)==0:self.desc = "No Description given"
		else:self.desc = desc

		self.ind= ind

		self.ct = ct
#used len(x)==0 because it felt correct				

	def set_name(self,name):
		self.name = name

	def set_dur(self,dur):
		self.dur = dur

	def set_desc(self,desc):
		self.desc = desc
	def set_ct(self, ct):
		self.ct = ct
#these will be used when changing any value
	def add_task(ltask,co):
		"""to add a task to tasks list"""
		usrn, usrdu ,usrds = str(input("name:duration:description\
								 	   \n(separated by '|')\
								 	   \n")).split("|" , 2)
		ltask.append(Task(name=usrn, dur=usrdu, desc=usrds, ind=co))
	 	
			
