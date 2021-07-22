nf = int(input("Quantos numeros da sequencia de fibonati voce quer ?"))
t,tt,ttt = (0,1,1)
print("{} - ".format(t),end="")
for i in range(nf - 2):
    ttt = tt + t
    print("{} - ".format(tt),end='')
    t = tt
    tt = ttt
print(ttt,".",'numero de fi:',tt / t)
