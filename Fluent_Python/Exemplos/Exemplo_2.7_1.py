# path, last_path
import os
_, filename = os.path.split('home/pedro/.ssh/idrsa.pub')
#print(filename)

#-----Usando * para capturar itens -------
#a, b, *rest = range(5)
#print(a, b, rest)

# No corpo
a, *body, c, d = range(5)
print(a, body, c, d)


