class SkipNode:  
	def __init__(self, height = 0, elem = None):
		self.val = elem
		self.next = [None]*height

	def __repr__(self) -> str:
		if self.val is None: return ""
		output = self.val
		if len(self.next)>0: output+=" -> "
		for v in self.next:
			if v:
				output += str(v) + ", "
		return output

	def __str__(self) -> str:
		if self.val is None: return ""
		output = self.val
		if len(self.next)>0: output+=" -> "
		for v in self.next:
			if v:
				output += str(v) + ", "
		return output