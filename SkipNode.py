class SkipNode:  
	def __init__(self, height = 0, elem = None):
		self.val = elem
		self.next = [None]*height

	def __repr__(self) -> str:
		return "SkipNode Class"

	def __str__(self) -> str:
		if self.val is None: return ""
		output = self.val
		if len(self.next)>0: output+=" -> "
		for v in self.next:
			if v:
				output += v + ", "
		return output