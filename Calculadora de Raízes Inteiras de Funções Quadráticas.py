import math

print("f(x) = ax^2 + bx + c")
A = float(input("Para descobrir a(s) raíz(es) de qualquer função quadrática, insira o valor de 'a' diferente de 0:"))
B = float(input("Agora, o valor de 'b':"))
C = float(input("Por fim, o valor de 'c':"))

DELTA = (B**2) - (4*A*C)

if DELTA < 0:
    print("esta equação não possui raízes reais")
else:
    XIS1 = (-B - math.sqrt(DELTA))//(2*A)
    XIS2 = (-B + math.sqrt(DELTA))//(2*A)
    if(XIS1 == XIS2):
        print("a raiz dupla desta equação é",XIS1)
    else:
        if(XIS1 < XIS2):
            print("as raízes da equação são",XIS1,"e",XIS2)
        else:
            print("as raízes da equação são",XIS2,"e",XIS1)

