#Encaminha o arquivo
nome_arquivo = "numeros.txt"

#abre comparação de arquivos
try:
    with open(nome_arquivo, 'r') as arquivo:
        soma = 0

        for linha in arquivo:
            #Soma os inteiros em cada linha
            soma += int(linha.strip())
    print(f"A soma dos números no arquivo {nome_arquivo} é: {soma}")

#Erro de arquivo não encontrado
except FileNotFoundError:
    print(f"O arquivo {nome_arquivo} não foi encontrado!")

#erro de valor diferente de inteiro
except ValueError:
    print(f"Certifique-se que o arquivo têm somente números inteiros!")
