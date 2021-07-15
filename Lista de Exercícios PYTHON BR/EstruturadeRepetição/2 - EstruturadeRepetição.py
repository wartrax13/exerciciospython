'''Faça um programa que leia um nome de usuário
e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.'''
user = ''
password = user
while password == user:
    user = input('Enter your user: ')
    password = input('Type your password: ')
    if password != user:
        break
    print('ERROR: User cannot equal password.')
    print('Try again.')
print('Acess validated.')