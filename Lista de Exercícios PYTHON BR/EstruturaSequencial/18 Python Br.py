'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)'''
print('--'*20)
print('Bem vindo ao Bittorrent!')
print('--'*20)
tamanho = int(input('Qual é o tamanho do arquivo? '))
vel = int(input('Qual é a velocidade em Mbps? '))
velmin = vel * 60
time = tamanho / velmin
print(f'O tempo necessário para baixar {tamanho} megabites é de aproximadamente {time:.0f} minutos.')