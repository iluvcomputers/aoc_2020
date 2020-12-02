

with open('input.txt', 'r') as data:
    data = [line.strip().split() for line in data.readlines()]

valid = 0
for row in data:
    bounds, tar, pwd = row
    lb,mb = bounds.split('-')
    td,_ = tar.split(':')
    cnt = pwd.count(td)
#    if int(lb) <= cnt and cnt <= int(mb):
#        valid +=1
    if (pwd[int(lb)-1] == td and pwd[int(mb)-1] != td) or (pwd[int(lb)-1] != td and pwd[int(mb)-1] == td):
        valid += 1

print(valid)
