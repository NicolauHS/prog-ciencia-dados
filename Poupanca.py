from Conta import Conta

class Poupanca(Conta):
    
    def __init__(self, rendimento, agencia, nome, data_nascimento, valor):
        super().__init__(agencia, nome, data_nascimento, valor)
        self.rendimento = rendimento
        self.valor_projetado = 0;
        self.taxa = 0;
        
    def calcular_saldo_prox():
        return float
    
    def resgatar():
        return float