
# csv.reader(), csv.writer()
# delimiter=',', lineterminator='\n'

# json.dumps() converter para json
# json.loads() trazer para python

import csv

with open("alunos.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=",", lineterminator="\n")
    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Lucas", 8.5])
    escritor.writerow(["Ana", 9.0])
import json

dados = {"nome": "Joao", "idade": 16}
texto_json = json.dumps(dados)
print(texto_json)
