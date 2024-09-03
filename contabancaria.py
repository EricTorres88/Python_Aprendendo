class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def exibir_saldo(self):
        print(f"Saldo: R$ {self.__saldo}")

conta = ContaBancaria(1000)
conta.exibir_saldo()