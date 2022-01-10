english_to_spanish = { 'hello': 'hola', 'one': 'uno', 
                      'please': 'por favor', 'coffee': 'café' }

for word in "hello one coffee please".split():
    print(english_to_spanish[word], end=' ')
print()

english_to_spanish['corn'] = 'maize'
print(english_to_spanish)

english_to_spanish['table'] = 'mesa'
print(english_to_spanish)

english_to_spanish['flour'] = 'arina'
print(english_to_spanish)
