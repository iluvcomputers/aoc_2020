
with open('input.txt', 'r') as data:
    data = [line.strip().split() for line in data.read().split('\n\n')]

total = 0

for group in data:
    gsl = []
    for m in group:
        ms = set() 
        for s in m:
            ms.add(s)
        gsl.append(ms)
    total += len(set.intersection(*gsl))

print(total)
