A = int(input("Digite um valor para saber a soma de seus algarismos: "))

soma = 0
B = 1
while B != 0:
    B = A%10
    soma = soma + B
    A = A//10
print("A soma dos algarismos é",soma)


#1234
    
