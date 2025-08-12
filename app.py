n = int(input("Tabuada de: ")) #aqui você coloca o número que você deseja multiplicar
inicio = int(input("De: ")) #Aqui da onde ele começa
fim = int(input("Até: "))  #até onde termina obs: pode ser qualquer número
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
