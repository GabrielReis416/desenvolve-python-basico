import random
import math


n = int(input("Digite o número de valores aleatórios a serem gerados: "))


v = [random.randint(0, 100) for _ in range(n)]


soma = sum(v)


raiz_quadrada = math.sqrt(soma)


print(f"Valores gerados: {v}")
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")