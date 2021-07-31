#TUPLAS NOMEADAS é uma fábrica que gera subclasses de tuple melhoradas com nomes de campos e um nome de classe.
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

print(tokyo.population)
print(tokyo[1])