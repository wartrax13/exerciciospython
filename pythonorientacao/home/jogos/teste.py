def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))



conta = cria_conta('123-4', 'João', 120.0, 1000.0)
deposita(conta, 15.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)