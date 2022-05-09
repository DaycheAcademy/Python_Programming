# Path:
# Absolute : C:\Users\DaBigM\Desktop\python Dayche\GitHub\sample.txt
# Relative: \.
# C:\Users\DaBigM\Desktop\python Dayche\Scripts\myfile.txt
# ..\Scripts\myfile.txt

fid = open('sample.txt')
print(fid)
print('---------')
# for line in fid:
#     print(line)
fid.close()

# Context Manager: with

with open('sample.txt', 'r') as fid:
    # for line in fid:
    #     print(line)

    line = fid.readline().strip('\n')
    while line:
        print(line)
        line = fid.readline().strip('\n')

print('=' * 50)

with open('sample.txt') as fid:
    # for line in fid:
    #     print(line)

    lines = fid.readlines()
print(lines)

print('=' * 50)

with open('sample.txt') as fid:
    # for line in fid:
    #     print(line)

    txt = fid.read()
print(txt)

# ==========================

myContent = ['Data Science Class\n', str(34)+'\n', 'Python Foundation Masterclass\n']
with open('dayche.txt', 'w') as fid:
    # fid.write()
    # print('Dayche Python Class', file=fid)
    fid.writelines(myContent)















