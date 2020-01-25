file = open("fires_class.csv")
out = open("output.csv", 'w')
encoding = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
first = True
for line in file:
	if first:
		first = False
		continue
	items = line.split(',')
	items[5] = encoding[items[5][0]]
	for i, item in enumerate(items):
		out.write(str(item))
		if i < 5:
			out.write(',')
		else:
			out.write('\n')
out.close()
