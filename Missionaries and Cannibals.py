def BFS():
	initial_state = CannibalsAndMissionaries(3,3,'left',0,0)
	if initial_state.check_if_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.check_if_goal():
			return state
		explored.add(state)
		decendant_nodes = successors(state)
		for i in decendant_nodes:
			if (i not in explored) or (i not in frontier):
				frontier.append(i)
	return None

def successors(current_state):
	decendant_nodes = [];
	if current_state.boat == 'left':
		successor_state = CannibalsAndMissionaries(current_state.left_cannibal, current_state.left_missionary - 2, 'right', current_state.right_cannibal, current_state.right_missionary + 2)
		if successor_state.check_restrictions():
			successor_state.parent = current_state
			decendant_nodes.append(successor_state)
		successor_state = CannibalsAndMissionaries(current_state.left_cannibal - 2, current_state.left_missionary, 'right', current_state.right_cannibal + 2, current_state.right_missionary)
		if successor_state.check_restrictions():
			successor_state.parent = current_state
			decendant_nodes.append(successor_state)
		successor_state = CannibalsAndMissionaries(current_state.left_cannibal - 1, current_state.left_missionary - 1, 'right', current_state.right_cannibal + 1, current_state.right_missionary + 1)
		if successor_state.check_restrictions():
			successor_state.parent = current_state
			decendant_nodes.append(successor_state)
		successor_state = CannibalsAndMissionaries(current_state.left_cannibal, current_state.left_missionary - 1, 'right', current_state.right_cannibal, current_state.right_missionary + 1)
		if successor_state.check_restrictions():
			successor_state.parent = current_state
			decendant_nodes.append(successor_state)
		successor_state = CannibalsAndMissionaries(current_state.left_cannibal - 1, current_state.left_missionary, 'right',
                                  current_state.right_cannibal + 1, current_state.right_missionary)
		if successor_state.check_restrictions():
			successor_state.parent = current_state
			decendant_nodes.append(successor_state)
	successor_state = CannibalsAndMissionaries(current_state.left_cannibal, current_state.left_missionary + 2, 'left', current_state.right_cannibal, current_state.right_missionary - 2)
	if successor_state.check_restrictions():
		successor_state.parent = current_state
		decendant_nodes.append(successor_state)
	successor_state = CannibalsAndMissionaries(current_state.left_cannibal + 2, current_state.left_missionary, 'left', current_state.right_cannibal - 2, current_state.right_missionary)
	if successor_state.check_restrictions():
		successor_state.parent = current_state
		decendant_nodes.append(successor_state)
	successor_state = CannibalsAndMissionaries(current_state.left_cannibal + 1, current_state.left_missionary + 1, 'left', current_state.right_cannibal - 1, current_state.right_missionary - 1)
	if successor_state.check_restrictions():
		successor_state.parent = current_state
		decendant_nodes.append(successor_state)
	successor_state = CannibalsAndMissionaries(current_state.left_cannibal, current_state.left_missionary + 1, 'left', current_state.right_cannibal, current_state.right_missionary - 1)
	if successor_state.check_restrictions():
		successor_state.parent = current_state
		decendant_nodes.append(successor_state)
	successor_state = CannibalsAndMissionaries(current_state.left_cannibal + 1, current_state.left_missionary, 'left', current_state.right_cannibal - 1, current_state.right_missionary)
	if successor_state.check_restrictions():
		successor_state.parent = current_state
		decendant_nodes.append(successor_state)
	return decendant_nodes

class CannibalsAndMissionaries():
	def __init__(self, left_cannibal, left_missionary, boat, right_cannibal, right_missionary):
		self.left_cannibal = left_cannibal
		self.left_missionary = left_missionary
		self.boat = boat
		self.right_cannibal = right_cannibal
		self.right_missionary = right_missionary
		self.parent = None
	def check_if_goal(self):
		if self.left_cannibal == 0 and self.left_missionary == 0:
			return True
		else:
			return False
	def check_restrictions(self):
		if self.left_missionary >= 0 and self.right_missionary >= 0 \
                   and self.left_cannibal >= 0 and self.right_cannibal >= 0 \
                   and (self.left_missionary == 0 or self.left_missionary >= self.left_cannibal) \
                   and (self.right_missionary == 0 or self.right_missionary >= self.right_cannibal):
			return True
		else:
			return False
	def __eq__(self, other):
		return self.left_cannibal == other.left_cannibal and self.left_missionary == other.left_missionary \
                   and self.boat == other.boat and self.right_cannibal == other.right_cannibal \
                   and self.right_missionary == other.right_missionary
	def __hash__(self):
		return hash((self.left_cannibal, self.left_missionary, self.boat, self.right_cannibal, self.right_missionary))

path = []
path.append(BFS())
parent = BFS().parent
while parent:
	path.append(parent)
	parent = parent.parent
for i in range(len(path)):
	state = path[len(path) - i - 1]
	print("C:", str(state.left_cannibal), "", "M:", str(state.left_missionary), end=' '),
	if state.boat == 'left':
		print ("|<==>--------|", end=''),
	else:
		print ("|''''''''<==>|", end=''),
	print(" C:", str(state.right_cannibal), "", "M:", str(state.right_missionary))
