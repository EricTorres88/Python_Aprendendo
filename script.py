def saudacao(nome):
    return print(f'Olá, {nome}!')

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
saudacao(nome)
print(f"{nome} tem {idade} anos.")