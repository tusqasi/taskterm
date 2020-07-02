class Task:
	"""Make a task object"""

	def __init__(self, name="", dur="", desc="" , ind=""):
		if len(name)==0:
			self.name = "No Name given"	
		else:
			self.name = name

		if len(dur)=0:
			self.dur = "No Duration given"
		else:
			self.dur = dur 
		
		if len(desc)=0:
			self.desc = "No Description given"
		else:
				self.desc = desc
				
		if len(ind)=0:
			self.ind = "No Index given"
		else:
				self.ind = ind