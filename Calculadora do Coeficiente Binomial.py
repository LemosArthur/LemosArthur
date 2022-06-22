def fatorial (A):
    fator = 1
    if A != 0:
        while A != 1:
            fator = fator * A
            A = A-1
    return fator

def cbinomial(x,y):
    return (fatorial(x)/(fatorial(y)* fatorial(x-y)))
    
