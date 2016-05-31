def prob_3(b,p):
	b1 = b
	for i in range(1,p):
		b = b*b1
	return b