class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Pedro', '9409-9323')
conta = Conta(c1.get_nome(), 1222, 0)

conta.deposito(200)
conta.saque(60)
conta.extrato()