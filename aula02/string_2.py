nome = "Nayara"
idade = 20
profissao = "Programadora"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Nayara", "idade": 20}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}" .format(nome, idade))

print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))

print("Nome: {nome} Idade: {idade}" .format(nome=nome , idade=idade))
print("Nome: {name} Idade: {age}" .format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome {nome} Idade: {idade}")
print(f"Nome {nome} Idade: {idade} Saldo: {saldo:.2f}")