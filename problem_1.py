numbers = range(1,1000)
s = []
for number in numbers:
    if number %3 == 0 or number %5 == 0:
        s.append(number)
print(sum(s))
