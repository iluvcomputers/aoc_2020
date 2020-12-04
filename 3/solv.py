
contents = open('input.txt').read().splitlines()

nrow = len(contents)
ncol = len(contents[0])
vectors = [(1,1),(3,1),(5,1),(7,1),(1,2)]
trees = 1

for v in vectors:
    
    endx = crow = ccol = ntrees = 0
    dx,dy = v
    
    while(endx < nrow):
        if contents[crow][ccol] == '#':
            ntrees += 1
        endx = (crow + dy)
        crow = endx%nrow
        ccol = (ccol + dx)%ncol

    trees *= ntrees

print(trees)
