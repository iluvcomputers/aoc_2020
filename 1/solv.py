
import timeit

contents = open('input.txt').read().splitlines()
contents = list(map(int, contents))

def crunch():
    for i in contents:
        for j in contents:
            for k in contents:
                if i + j + k == 2020:
                    print("i, j, k: ", i,j,k," | i*j*k: ",i*j*k)


dur = timeit.timeit(crunch, number=10)
print(dur)
