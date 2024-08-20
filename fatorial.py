def fatorial(num):
    resultado = 1
    while num > 1:
        resultado *= num
        num -= 1
    return resultado
    
numero = int(input("Informe um número inteiro: "))
print(f"O fatorial de {numero} é: {fatorial(numero)}")