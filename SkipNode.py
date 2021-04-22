class SkipNode:
    """A node from a skip list"""    
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        self.next = [None]*height
