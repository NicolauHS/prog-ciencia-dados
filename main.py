from Conta import Conta
from Corrente import Corrente
from Poupanca import Poupanca

if __name__ == '__main__':
    
    conta = Conta(1, "Nicolas", "01/01/2000", 1000)

    print(f"{conta.nome} tem R${conta.valor} na conta {conta.numero}-{conta.numero_validacao} da agencia {conta.agencia}")