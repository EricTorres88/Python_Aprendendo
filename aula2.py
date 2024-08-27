print("Digite uma lista de compras, digite 'sair' para sair. ")
listacompras = []

#função de atribuição de lista
while True:
    item = input("Digite um item: ")
    #verifica se o input é igual ou diferente de 'sair'
    if item.lower() == 'sair':
        break
    else:
        #adiciona os itens em pilha um após o outro
        listacompras.append(item)

#cria o nome do arquivo
nome_arquivo = "lista_de_compras.txt"

#abre o arquivo para escrita
with open(nome_arquivo, 'w', encoding="UTF-8") as arquivo:
    for item in listacompras:
        arquivo.write(item + '\n')

print(f"Sua lista de compras foi salva no arquivo '{nome_arquivo}'. ")