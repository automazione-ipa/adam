"""
Creare un programma che stampa i primi 10 numeri della sequenza di fibonacci"
"""
n = 10
i = 0
n1 = 0 
n2 = 1

while i<n:
    somma = n1 + n2 
    n1 = n2  
    n2 = somma  
    i += 1  
    print(n1)