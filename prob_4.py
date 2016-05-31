def prob_4(a,c):
	izq = (c-len(a))//2
	der = c - (izq+len(a))
	return (("*"*izq)+ a +("*"*der))