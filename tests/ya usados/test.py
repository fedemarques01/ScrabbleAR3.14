from pattern.text.es import lexicon, spelling, tag, suggest


def clasificar(palabra):
    print(tag(palabra, tokenize=True, encoding='utf-8'))


palabra = 'eme'
print(suggest(palabra))

if (not palabra in spelling) and( not palabra in lexicon):
    print('nono')
    clasificar(palabra)
else:
    print('La encontró')
    clasificar(palabra)
