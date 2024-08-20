def conversor(tipo, temperatura):
    if tipo == 'F' or tipo == 'f':
        resultado = (1.8 * temperatura) + 32
        return print(f"Sua temperatura {temperatura} para Fahrenheit é: {resultado:.1f}ºF")
    elif tipo == 'C' or tipo == 'c':
        resultado = (temperatura - 32) / 1.8
        return print(f"Sua temperatura {temperatura} para Celsius é: {resultado:.1f}ºC")
    
tipo = input("Digite 'C' se quiser calcular fahrenheit para celsius \nOu 'F' para Celsius para fahrenheit: ")
temperatura = float(input("Agora informe a temperatura: "))
conversor(tipo, temperatura)
