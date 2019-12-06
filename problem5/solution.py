def intInstruct(instruct):

	instruction = str(instruct)

	if len(instruction) > 1:

		return_val = [int(instruction[-2:])]

		inter_list = instruction[:-2]
		for item in inter_list[::-1]:
			return_val.append(int(item))


	else:
		return_val = [instruct]

	return return_val

def opt1(i_list, instruction, index):

	if len(instruction) > 1:
		if instruction[1] == 0:
			num1 = i_list[i_list[index+1]]
		else:
			num1 = i_list[index+1]

		if instruction[2] == 0:
			num2 = i_list[i_list[index+2]]
		else:
			num2 = i_list[index+2]
	else:
		print "Something went wrong"
		num1 = i_list[i_list[index+1]]
		num2 = i_list[i_list[index+2]]

	i_list[i_list[index+3]] = num1 + num2

def opt2(i_list, instruction, index):

	if len(instruction) > 1:
		if instruction[1] == 0:
			num1 = i_list[i_list[index+1]]
		else:
			num1 = i_list[index+1]

		if instruction[2] == 0:
			num2 = i_list[i_list[index+2]]
		else:
			num2 = i_list[index+2]
	else:
		print "Something went wrong"
		num1 = i_list[i_list[index+1]]
		num2 = i_list[i_list[index+2]]

	i_list[i_list[index+3]] = num1 * num2

def opt5(i_list, instruction, index):

	if instruction[1] == 0:
		if i_list[i_list[index+1]] != 0:
			if instruction[2] == 0:
				index = i_list[i_list[index+2]]
			else:
				index = i_list[index+2]
		else:
			index += 3
	else:
		if i_list[index+1] != 0:
			if instruction[2] == 0:
				index = i_list[i_list[index+2]]
			else:
				index = i_list[index+2]
		else:
			index += 3

	return index

def opt6(i_list, instruction, index):

	if instruction[1] == 0:
		if i_list[i_list[index+1]] == 0:
			if instruction[2] == 0:
				index = i_list[i_list[index+2]]
			else:
				index = i_list[index+2]
		else:
			index += 3
	else:
		if i_list[index+1] == 0:
			if instruction[2] == 0:
				index = i_list[i_list[index+2]]
			else:
				index = i_list[index+2]
		else:

			index += 3

	return index

def opt7(i_list, instruction, index):

	if instruction[1] == 0:
		val1 = i_list[i_list[index+1]]
	else:
		val1 = i_list[index+1]

	if instruction[2] == 0:
		val2 = i_list[i_list[index+2]]
	else:
		val2 = i_list[index+2]

	if val1 < val2:
		i_list[i_list[index+3]] = 1
	else:
		i_list[i_list[index+3]] = 0

def opt8(i_list, instruction, index):

	if instruction[1] == 0:
		val1 = i_list[i_list[index+1]]
	else:
		val1 = i_list[index+1]

	if instruction[2] == 0:
		val2 = i_list[i_list[index+2]]
	else:
		val2 = i_list[index+2]

	if val1 == val2:
		i_list[i_list[index+3]] = 1
	else:
		i_list[i_list[index+3]] = 0

def opcode(input_p, input_val):

	output = -99

	index = 0

	prev_instruct = []

	while input_p[index] != 99:

		#print input_p[index], intInstruct(input_p[index])
		instruction = intInstruct(input_p[index])
		if len(instruction) < 3:
				while (len(instruction)) != 3:
					instruction.append(0)
		if instruction[0] == 1:
			#input_p[input_p[index+3]] = input_p[input_p[index+1]] + input_p[input_p[index+2]]

			opt1(input_p, instruction, index)

			index += 4

		elif instruction[0] == 2:
			#input_p[input_p[index+3]] = input_p[input_p[index+1]] * input_p[input_p[index+2]]
			
			opt2(input_p, instruction, index)
			
			index += 4

		elif instruction[0] == 3:
			input_p[input_p[index+1]] = input_val
			index += 2

		elif instruction[0] == 4:
			
			if instruction[1] == 0:
				output_val = input_p[input_p[index+1]]
				print "output: ",output_val
			else:
				output_val = input_p[index+1]
				print "output: ",output_val
			# print prev_instruct
			index += 2

		elif instruction[0] == 5:

			index = opt5(input_p, instruction, index)

		elif instruction[0] == 6:

			index = opt6(input_p, instruction, index)

		elif instruction[0] == 7:

			opt7(input_p, instruction, index)

			index += 4

		elif instruction[0] == 8:

			opt8(input_p, instruction, index)

			index += 4

		else:
			"Something is very wrong"
			return output

		prev_instruct = instruction

	output = input_p[0]
	return output

def main():

	file_name = 'input.txt'

	f = open(file_name, 'r')

	program = f.read()

	program = program.split(',')

	int_pro = [int(x) for x in program]

	input_val = 5
	output = int(opcode(int_pro, input_val))

if __name__ == '__main__':

	main()

	# for noun in range(0,100):

	# 	for verb in range(0,100):

	# 		temp_pro = [x for x in int_pro]

	# 		temp_pro[1] = noun
	# 		temp_pro[2] = verb

	# 		output = int(opcode(temp_pro))

	# 		if output == 19690720:
	# 			print 100 * noun + verb
	# 			break
