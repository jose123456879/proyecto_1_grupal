def prob_7 ():
	lista = []
	for i in range(0,250):
		cu = 4*i
		if cu < 1000:
			lista.append(cu)
		si = 7*i
		if si < 1000:
			lista.append(si)
	lista.sort()
	return lista
