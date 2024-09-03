import json

dados = {"nome": "Roni", "Idade": 25, "Cidade": "Recife"}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)