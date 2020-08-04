from pattern.text.es import lexicon, spelling, tag, suggest,verbs


def clasificar(palabra):
    print(tag(palabra, tokenize=True, encoding='utf-8'))


palabra = 'zvpnllfa'
print(suggest(palabra))

if ((not palabra in spelling) and( not palabra in lexicon))or(not palabra in verbs):
    print('nono')
    clasificar(palabra)
else:
    print('La encontró')
    clasificar(palabra)
