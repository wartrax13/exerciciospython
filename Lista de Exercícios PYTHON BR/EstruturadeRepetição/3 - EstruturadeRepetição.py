'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

name = str(input('Your name is: '))

while len(name) <= 3:
    print('Your name must have more than three characters. Try again.')
    name = str(input('Your name is: '))

print(f'Your name is {name}')
x = range(0,150)
age = int(input('Your age: '))
while age not in x:
    print('Your age is not valid. Try again.')
    age = int(input('Your age: '))
print(f'Your age is: {age}')

wage = float(input('Enter you wage: '))
while wage <= 0:
    print('Your wage is not valid. Try again.')
    wage = int(input('Your wage: '))
print(f'Your age is: {wage}')

sex = str(input(' [f] for female\n'
                ' [m] for male.\n'
                'Enter your sex: '))
valor = ('m', 'f')
while sex not in valor:
    print('Your sex is not valid. Try again.')
    wage = int(input('Your sex: '))
print(f'Your sex is valid.')

mar = ('s','c','v','d')
marital = str(input('[s] solteiro\n'
                    '[c] casado\n'
                    '[v] viuvo\n'
                    '[d] divorciado\n'
                    'Enter your Marital status:'))
while marital not in mar:
    print('Your marital is not valid. Try again.')
    marital = int(input('Your marital: '))
print(f'Your marital is valid.')
