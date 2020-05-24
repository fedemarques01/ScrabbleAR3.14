from pattern.text.es import lexicon, spelling, tag, suggest

def clasificar(palabra):
	print(tag(palabra, tokenize=True, encoding='utf-8'))


palabra = 'casa'
print(suggest(palabra))

if not palabra in spelling:
	if not palabra in lexicon:
		print('No se encuentra en pattern.es')
	else:
		print('La encontró en lexicon')
		clasificar(palabra)
else:
	print('La encontró en spelling')
	clasificar(palabra)