def isPali(num):
    return str(num) == str(num)[::-1]
valMax = 0
for i in xrange(999,100,-1):
    for j in xrange(999,100,-1):
        if isPali(i*j):
            valMax = max(valMax, i*j)
            break
print(valMax)

