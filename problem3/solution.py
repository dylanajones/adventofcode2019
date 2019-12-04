import numpy as np

def betweenPoints(p, p1, p2):

	return ((p1[0] <= p[0] <= p2[0]) or (p2[0] <= p[0] <= p1[0])) and ((p1[1] <= p[1] <= p2[1]) or (p2[1] <= p[1] <= p1[1]))

def stepDist(coords):

	d = 0

	for i, c in enumerate(coords[:-1]):

		d += abs(c[0] - coords[i+1][0]) + abs(c[1] - coords[i+1][1])

	return d

if __name__ == '__main__':

	f = open('input.txt', 'r')

	wires_cord = []

	# Takes the input file and coverts to a set of cornor coordinates
	print "Reading file"
	for line in f:

		directions = line.split(',')

		# Using homogenous coordinate to make intersection calculations easy
		wire = [[0,0,1]]

		for instruction in directions:

			d = instruction[0]
			l = int(instruction[1:])
			if d == 'R':
				wire.append([wire[-1][0]+l,wire[-1][1],1])

			elif d == 'L':
				wire.append([wire[-1][0]-l,wire[-1][1],1])

			elif d == 'U':
				wire.append([wire[-1][0],wire[-1][1]+l,1])

			elif d == 'D':
				wire.append([wire[-1][0],wire[-1][1]-l,1])

		wires_cord.append(wire)

	# Now need to go through and convert into lines so we can compute intersections

	int_dist = float('inf')
	step_dist = float('inf')

	wires_lines = []

	print "Converting to lines"
	for wire in wires_cord:

		lines = []

		for i in range(0, len(wire)-1):

			lines.append(np.cross(wire[i], wire[i+1]))

		wires_lines.append(lines)

	# Now have the lines, need to compute the intersections and check that they are actually between the points
	print "Computing intersections and distance"
	for i, lines in enumerate(wires_lines):

		for j, comp_lines in enumerate(wires_lines):

			if i != j:

				for n, line in enumerate(lines):
					
					intsecs = np.cross(line, comp_lines)

					for k, intsec in enumerate(intsecs):

						if intsec[2] != 0:

							p = [float(intsec[0]) / intsec[2], float(intsec[1]) / intsec[2]]

							p1_a = wires_cord[j][k]
							p1_b = wires_cord[j][k+1]

							p2_a = wires_cord[i][n]
							p2_b = wires_cord[i][n+1]
							
							if betweenPoints(p, p1_a, p1_b) and betweenPoints(p, p2_a, p2_b) and p != [0,0]:

								# Update distance if less than known minimum distance
								if abs(p[0]) + abs(p[1]) < int_dist:
									int_dist = abs(p[0]) + abs(p[1])

								w1 = [x for x in wires_cord[j][:k+1]]
								w1.append(p)
								w2 = [x for x in wires_cord[i][:n+1]]
								w2.append(p)

								step_w1 = stepDist(w1)
								step_w2 = stepDist(w2)

								if step_w1 + step_w2 < step_dist:
									step_dist = step_w1 + step_w2


	print int_dist
	print step_dist



