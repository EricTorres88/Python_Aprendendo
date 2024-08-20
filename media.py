def media_aritmetica(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(f"Sua média aritmética é: {media:.2f}")
    #A sintaxe :.2f dentro da média, retorna apenas duas casas decimais da média.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um segundo número: "))
n3 = float(input("Digite um terceiro número: "))
media_aritmetica(n1, n2, n3)
