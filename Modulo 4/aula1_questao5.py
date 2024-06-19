#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.

n = int(input())
soma = 0
conta = 0
while conta < n :
 idade= int(input())
 conta += 1
 soma += idade

 print(f"A média das idades e {soma/n :.0f} anos")