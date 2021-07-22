print("-------------------------------------------------------------")
nf = int(input("Quantos numeros da sequencia de fibonati voce quer ?"))
print("-------------------------------------------------------------")

cont = 2

t1 = 0
t2 = 1
t3 = t2 + t1
x: int

print("{} - {}".format(t1, t2), end='')


def fibo(a, b, c):
    c = b + a
    print(" - {}".format(c), end='')
    a = b
    b = c
    return a, b, c


while cont < nf:

    '''fibo(t1 ,t2 ,t3)#'''
    (t1, t2, t3) = fibo(a=t1, b=t2, c=t3)

    cont = cont + 1


proporção_de_fibonati = t2 / t1

print("")
print("")
print("")
print("Com {} numeros ,o numero de fi é {}".format(nf, proporção_de_fibonati))
