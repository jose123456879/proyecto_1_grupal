def prob_9 (x,y,z):
	lista = [x, y, z]
	lista.sort()
	if (lista[0]**2)+(lista[1]**2)==(lista[2]**2):
		return ("representan los lados de un triangulo rectangulo, esto es Tripleta Pitagórica")
	else:
		return ("no representa un triangulo reactangulo, no es una tripleta pitagorica")