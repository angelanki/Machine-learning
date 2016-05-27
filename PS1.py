
class Node:

	def __init__(self):
		self.value = None
		self.children = None

	def get_value(self):
		
		'''
		given a node, will return the value at this node
		'''
		return self.value

	def get_children(self):
		
		'''
		given a node, will return the children of this node
		'''
		return self.children
			
		
def breadth_first_search(root):
	
	'''
	given the root node, will complete a breadth-first-search on the tree, returning the value of each node in the correct order
	'''
	queue = ""
	queue_ = []
	node = root
	queue = str(root.get_value())
	while node.children is not None:
		for i in node.get_children():
			queue += " " + str(node.children[i].get_value())
			queue_.append(node.children[i])
		node = queue_.pop(0)
	return queue


def tester():
	a = Node()
	a.value = 5
	b = Node()
	b.value = 7
	a.children = {1: b}
	
	'''
	c = Node()
	c.value = 9
	d = Node()
	d.value = 11
	a.children = {1: b, 2: c, 3:d}
	b.children = {1: a, 2: d}
	c.children = {1: d}
	'''
	print str(a.get_value()) + ' should be 5.'
	print str(a.get_children()) + ' should be {1: ' + str(b) + '}.'
	print str(breadth_first_search(a)) + ' should be 5 7.'

tester()