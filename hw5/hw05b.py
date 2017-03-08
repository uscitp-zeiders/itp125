a = 0
b = 1
val = 0
while b < 4000000:
    temp = b
    b = b + a
    a = temp
    if b%2 == 0:
        val = val + b
print val
    
