from conta import Conta, Cliente

cliente = Cliente('João', 'Oliveira', '11111111111-11')
#cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta = Conta('123-4', cliente, 1000.0)
#conta2 = Conta('123-5', cliente2, 1000.0)
#conta1.deposita(100.0)
#conta1.saca(50.0)
#conta1.transfere_para(conta2, 200.0)
#conta1.extrato()
#conta.historico.imprime()

#conta2.historico.imprime()

print(vars(conta))

