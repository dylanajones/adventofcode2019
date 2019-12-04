
def testSame(str_num):

	for i, digit in enumerate(str_num[:-1]):

		if digit == str_num[i+1]:

			if i != 0:
				if i+2 == len(str_num):
					if digit != str_num[i-1]:
						# print '1 ', i
						return True
				else:
					if digit != str_num[i+2] and digit != str_num[i-1]:
						# print '2 ', i
						return True
			else:
				if i+2 == len(str_num):
					# print '3 ', i
					return True
				elif digit != str_num[i+2]:
					# print '4 ', i
					return True

	return False

def testIncrease(str_num):

	for i, digit in enumerate(str_num[:-1]):

		if int(digit) > int(str_num[i+1]):

			return False

	return True

if __name__ == '__main__':

	# test_num = '111122'

	# print testSame(test_num)
	# print testIncrease(test_num)

	input_range = ['231832', '767346']

	num_meet = 0
	cur_num = input_range[0]

	while int(cur_num) <= int(input_range[1]):

		print cur_num

		if testSame(cur_num) and testIncrease(cur_num):
			num_meet += 1

		cur_num = str(int(cur_num)+1)

	print num_meet