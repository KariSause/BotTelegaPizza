import json

ar = []

with open('cenz.txt') as r:
	for i in r:
		n = i.lower().split('\n')[0]
		if n != '':
			ar.append(n)

with open('cenz.json', 'w', encoding='utf-8') as e:
	json.dump(ar,e)