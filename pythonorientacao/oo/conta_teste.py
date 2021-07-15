from conta import Conta

conta = Conta('123-4', 'João', 120.0, 1000.0)
conta2 = Conta('123=5', 'Pedro', 50, 1000.0)
print(conta.numero)
conta.deposita(80.0)
conta.saca(10.0)
conta.extrato()
'''
def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

conta = criar_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)
'''