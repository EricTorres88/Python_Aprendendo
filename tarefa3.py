print("Insira o nome de um aluno e a nota, caso deseje sair insira 'sair'")
dicioaluno = {}

while True:
    chave = input("Digite um nome: ")
    if chave.lower() == "sair":
        break

    try:
        valor = float(input("Insira uma nota: "))

        dicioaluno[chave] = valor

    except ValueError:
        print("Por favor, certifique-se de inserir uma nota válida")

nome_arquivo = 'alunos.txt'
with open(nome_arquivo, 'w') as arquivo:
    for aluno, nota in dicioaluno.items():
        arquivo.write(f"{aluno} : {nota}\n")

print(f"Sua lista de notas foi salva em {nome_arquivo}")