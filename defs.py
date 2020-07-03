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

	def set_name(self,name):
		self.name = name

	def set_dur(self,dur):
		self.dur = dur
		
	def set_desc(self,desc):
		self.desc = desc
		
	def set_ind(self,ind):
		self.ind = ind