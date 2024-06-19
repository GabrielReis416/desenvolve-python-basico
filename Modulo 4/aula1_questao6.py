#Exercício de maratona: https://www.beecrowd.com.br/judge/pt/problems/view/1094
#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas

n = int(input()) 
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

while cont < n :
 quantia = int(input())
tipo=input()

if tipo=='s':
 soma_sapo += quantia
elif tipo =='r':
 soma_rato += quantia
elif tipo =='c':
 soma_coelho += quantia

cont+= 1

print("Total de cobaias :", soma_sapo+soma_rato+soma_coelho)
print("Total de sapos", soma_sapo)
print("Total de ratos", soma_rato)
print("Total de coelhos", soma_coelho)