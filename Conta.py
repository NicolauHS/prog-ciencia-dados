from random import randint

class Conta:

    def __init__(self, agencia, nome, data_nascimento, valor):
        self.numero = "{:05}".format(randint(1, 99999))
        self.numero_validacao = "{:02}".format(randint(1, 99))
        self.agencia = agencia
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.valor = valor

        pass

    def deposito():
        pass

    def saque():
        pass

    def transferencia():
        pass

    def extrato():
        pass