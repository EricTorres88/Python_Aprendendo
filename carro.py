class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        print("O veículo está se movendo.")
class Carro(Veiculo):

    rodas = 4

    @classmethod
    def exibir_rodas(cls):
        print(f"Todos os carros têm {cls.rodas} rodas.")

    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_info()

Carro.exibir_rodas()