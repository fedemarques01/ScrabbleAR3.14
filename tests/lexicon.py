import pattern.text.es
dir(pattern.text.es)

c = 0
for x in pattern.text.es.lexicon.keys():
	if x in pattern.text.es.spelling.keys():
		print(x, end=', ')
		c += 1

print('Cantidad de palabras en lexicon que no estan en spelling: ',c)