genero = (input("digite sua genero: "))
idade = int(input("digite sua idade: "))
tempo = int(input("tempo de serviço: "))

a = ( genero == 'f' and idade >=60) or ( genero == 'm' and idade >=65) 
b = tempo > 30
c= idade >= 60 and tempo >=25

pode_aposentar =  a or b or c
print(pode_aposentar)
