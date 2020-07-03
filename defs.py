class Task:
	"""Make a task object"""

	def __init__(self, name="", dur="", desc=""):
		if len(name)==0:self.name = "No Name given"		
		else:self.name = name

		if len(dur)==0:self.dur = "No Duration given"
		else:self.dur = dur 
		
		if len(desc)==0:self.desc = "No Description given"
		else:self.desc = desc
#used len(x)==0 because it felt correct				

	def set_name(self,name):
		self.name = name

	def set_dur(self,dur):
		self.dur = dur

	def set_desc(self,desc):
		self.desc = desc
#these will be used when changing any value