import csv

with open("dados.csv", "w", newline ='', encoding='utf8') as arquivo:
    arq = csv.writer(arquivo)
    arq.writerow(["Nome", "Idade", "Cidade"])
    arq.writerow(["Fátima", "20", "Recife"])