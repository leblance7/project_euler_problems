#Generate a Fibonacci sequence starting with 1 and 2 going to 10
#Fibonacci sequence is the sum of the last two postions in the sequence
a = 1
b = 2
s = 0
d = [2]
print(a)
print(b) 

for _ in range(40):
    c = a + b
    if c >= 4_000_000:
        break
    a = b
    b = c
    s += c
    if c %2 == 0:
        d.append(c)
        print(sum(d))
        


    
