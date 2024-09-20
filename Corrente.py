from Conta import Conta


class Corrente(Conta):
    
    def __init__(self, agencia, nome, data_nascimento, valor):
        super().__init__(agencia, nome, data_nascimento, valor)
        self.limite = valor * .1
        pass