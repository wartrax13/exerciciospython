from conta import Conta, Cliente

conta = Conta('123-4', 'João', 120.0, 1000.0)
conta2 = Conta('123-5', 'Pedro', 100.0, 1000.0)

cliente = Cliente('João', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', cliente, 120.0, 1000.0)
#conta.deposita(20.0)
#conta.extrato()
#conta.saca(500)
#conta.extrato()

#print(minha_conta.titular.nome)
print(type(conta.titular))