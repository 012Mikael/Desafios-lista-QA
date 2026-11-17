'''
Crie uma tupla com 5 dados

•
Altere a tupla para uma lista

•
Insira 2 dados extras a essa lista

•
Remova o primeiro dado da lista

•
Remova o último dado da lista

•
Faça um print com o primeiro dado da lista

•
Faça um print com a quantidade de dados da lista

•
Crie um dicionário com os seguintes dados:
Nome, Idade, Profissão

•
Imprima somente o valor contido na chave Nome do dicionário

'''

#Tupla com 5 dados
Eletronicos = ("Mouse", "Teclado", "Computador", "Cpu", "Processador")

print(Eletronicos)
print(50*"=")

#Lista com os dados da tupla
#adicionando mais 2 dados a lista
eletronicos_lista =  ["Mouse", "Teclado", "Computador", "Cpu", "Processador"]

eletronicos_lista.extend(["Impressora", "Scanner"])

#remover o primeiro dado
eletronicos_lista.pop(0)

#remover o último dado
eletronicos_lista.pop(5)

print(eletronicos_lista)

#primeiro dado da lista
print(f"Primeiro dado da lista: {eletronicos_lista[0]}")

#quantidade de dados da lista
print(f"Quantidade de dados da lista: {len(eletronicos_lista)}")

print(50*"=")

#criação do dicionário
dados_pessoais = { "Nome": input("Digite o nome: "), 
                  
                  "Idade": int(input("Digite a idade: ")), 

                  "Profissão": input("Digite a profissão: ")
                  }

print(f"nome contido na chave Nome do dicionário: {dados_pessoais['Nome']}")