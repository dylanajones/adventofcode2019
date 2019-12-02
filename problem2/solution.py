

def opcode(input_p):

	output = -99

	index = 0

	while input_p[index] != 99:

		if input_p[index] == 1:
			input_p[input_p[index+3]] = input_p[input_p[index+1]] + input_p[input_p[index+2]]

		elif input_p[index] == 2:
			input_p[input_p[index+3]] = input_p[input_p[index+1]] * input_p[input_p[index+2]]

		else:
			"Something is very wrong"
			return output

		index += 4

	output = input_p[0]
	return output

if __name__ == '__main__':

	file_name = 'input.txt'

	f = open(file_name, 'r')

	program = f.read()

	program = program.split(',')

	int_pro = [int(x) for x in program]

	for noun in range(0,100):

		for verb in range(0,100):

			temp_pro = [x for x in int_pro]

			temp_pro[1] = noun
			temp_pro[2] = verb

			output = int(opcode(temp_pro))

			if output == 19690720:
				print 100 * noun + verb
				break

	