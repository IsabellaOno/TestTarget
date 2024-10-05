print("Questão 01")
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print("Soma é igual a:", soma)

print()
print("Questão 02")
n = int(input("Digite o número:"))
contador = 1
fibonacci = [0, 1]

while contador < n + 2:
    numero = (fibonacci[-1]) + (fibonacci[-2])
    fibonacci.append(numero)
    contador += 1

if n in fibonacci:
    print(n,"pertence a sequência de Fibonnaci.")
else:
    print(n, "não pertence a sequência de Fibonacci")

print()
print("Questão 03")

import json

with open("Faturamentomensal.json", "r") as file:
    data = json.load(file)

valores = [dia["valor"] for dia in data["faturamento"] if dia["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)

media = sum(valores)/len(valores)

dias_acima = sum(1 for valor in valores if valor > media)

print("O menor valor de faturamento ocorrido no mês: R${:.2f}".format(menor_valor))
print("O maior valor de faturamento ocorrido no mês: R${:.2f}".format(maior_valor))
print("A média mensal foi de: R${:.2f}".format(media))
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", dias_acima)

print()
print("Questão 04")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

totalEstados = sp + rj + mg + es + outros
estados = [sp, rj, mg, es, outros]
nomes_estados = ["SP", "RJ", "MG", "ES", "Outros"]

for i in range(len(estados)):
    percentual = (estados[i]/totalEstados) * 100
    print("Percentual " + nomes_estados[i] + ": {:.2f}%".format(percentual))

print()
print("Questão 05")
print()

palavra = input("Digite a string:")
tamanhoPalavra = len(palavra)
invertido = ""

for i in range(tamanhoPalavra):
    invertido += palavra[tamanhoPalavra - i - 1]

print("String invertida:", invertido)