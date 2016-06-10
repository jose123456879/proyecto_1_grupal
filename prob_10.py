def prob_10(a,b,c):
	lista=[a, b, c]
	tupla=tuple(lista)
	if tupla[0]==tupla[1]==tupla[2]:
		return("Representa un tiangulo equilatero")
	if tupla[0]==tupla[1]>tupla[2]:
		return("represeta un triangulo isoseles")
	if tupla[0]!=tupla[1]!=tupla[2]:
		return("Representa un triangulo escaleno")
	if tupla[0]==0 or tupla[1]==0 or tupla[2]==0:
		return("no es un triangulo.")