class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite = 1000.0):
        print('inicializando uma conta')
        self.numero = numero
        self.titular = Cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente. Tente de novo.')
            return False

        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
        return True
