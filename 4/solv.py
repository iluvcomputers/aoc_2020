
import re

with open('input.txt', 'r') as data:
    data = [dict(s.split(':') for s in line.strip().split()) for line in data.read().split('\n\n')]

valid = 0
indicators = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def validate(info):
    phcl = re.compile('^#[0-9a-f]{5}[0-9a-f]$')
    ppid = re.compile('^[0-9]{8}[0-9]$')
    ecls = ['amb','blu','brn','gry','grn','hzl','oth']
    try:
        if not 1920 <= int(info['byr']) <= 2002:
            return 0
        if not 2010 <= int(info['iyr']) <= 2020:
            return 0
        if not 2020 <= int(info['eyr']) <= 2030:
            return 0
        if 'in' in info['hgt']:
            if not 59 <= int(info['hgt'][:2]) <= 76:
                return 0
        elif 'cm' in info['hgt']:
            if not 150 <= int(info['hgt'][:3]) <= 193:
                return 0
        else:
            return 0
        if not phcl.match(info['hcl']):
            return 0
        if not any(i in info['ecl'] for i in ecls):
            return 0
        if not ppid.match(info['pid']):
            return 0

    except:
        return 0

    return 1 

for entry in data:
    if all(i in entry for i in indicators):
        valid += validate(entry)

print(valid, len(data))
