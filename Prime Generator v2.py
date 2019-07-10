PrimeCount = int(input("How many prime numbers would you like to generate?\n"))+1
unmark = []
for x in range(2, PrimeCount):
    unmark.append(x)
for x in range(2, PrimeCount + 1, 2):
    if x > len(unmark):
        break
    else:
        unmark.remove(x)
c = -1
for b in range(len(unmark)):
    c = c + 1
    if c >= len(unmark):
        break
    y = unmark[c]
    for a in range(unmark[c], unmark[-1] + 1, y):
        if a == y:
            continue
        if unmark.count(a)>0:
            unmark.remove(a)
for x in unmark:
    print(x)
