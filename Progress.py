def pr(q):
    k=0
    for i in range(2, q // 2 + 1):
        if (q % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False
def fact(n):
    s=""
    r=[]
    i=2
    m=n
    if pr(n):
        r.append(n)
    else:
        while n>1:
            while i<=n:
                if pr(i):
                    if n%i==0:
                        r.append(str(i))
                        n=n//i
                        break
                i=i+1
            i=2
    return "*".join(r)

print(fact(21))



