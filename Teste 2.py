'''
Teste 2 - python

Curso: Matemática Aplicada

Disciplina: Topicos da Matemática Aplicada A

Nomes:
Felipe Rodrigues Ribeiro
Luiz Miguel Carmona Moura
Matheus Moreira do Nascimento
Vinícius Rabello Rodrigues

DRE(respectivamente):
119052031
119066153
119042060
119056899
'''


import csv

with open("perfil_eleitorado_ATUAL.txt") as arquivo:
    dados = csv.reader(arquivo, delimiter=';')
    
    idade = {}
   
    for lin in dados:
        if lin[6] not in idade:
            idade[lin[6]] = 0
        idade[lin[6]] += 1
    print("+","-"*58,"+")
    for i in idade:
        print("|Existem {0:^10} pessoas na categoria {1:20}|".format(idade[i],i))
    print("+","-"*58,"+")
