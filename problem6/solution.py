class Object():

	def __init__ (self, parent):
		self.orbits = parent
		self.orbitted = []
		self.num_orbits = 0

def readInList(f, p_dict):

	for line in f:

		d = line.split(')')
		d[1] = d[1].rstrip('\n')

		if d[0] not in p_dict.keys():
			p_dict[d[0]] = Object(None)
		
		p_dict[d[0]].orbitted.append(d[1])

		if d[1] not in p_dict.keys():
			p_dict[d[1]] = Object(d[0])
		else:
			p_dict[d[1]].orbits = d[0]

def findCOM(p_dict):

	for key in p_dict.keys():

		if p_dict[key].orbits == None:
			return key

	return None

def countOrbits(p_dict, COM):

	return recCountOrbits(0, COM, p_dict)

def recCountOrbits(d, key, p_dict):

	sum_below = 0

	for body in p_dict[key].orbitted:
		sum_below += recCountOrbits(d+1, body, p_dict)

	return d + sum_below

def BFS(p_dict):

	start_node = 'YOU'

	queue = [(start_node, 0)]

	visited = []

	while queue:

		n = queue.pop(0)
		visited.append(n[0])

		if n[0] == 'SAN':
			return n[1]
		else:
			neb = p_dict[n[0]].orbitted
			neb.append(p_dict[n[0]].orbits)
			for node in neb:
				if node not in visited and node is not None:
					queue.append((node, n[1]+1))




def main():

	f = open('input.txt', 'r')

	p_dict = {}

	readInList(f, p_dict)

	COM = findCOM(p_dict)

	print countOrbits(p_dict, COM)

	print BFS(p_dict) - 2

	return 0

if __name__ == '__main__':

	main()