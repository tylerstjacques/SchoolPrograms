filename = 'file1'
f = open(filename, 'r')
lines = f.readlines()
atom_dict = {}
for line in lines:
    line = line.split(' ')
    index_name = line.pop(0)
    for num in line:
        num = float(num)
        line.append(num)
        line.pop(0)
    atom_dict[index_name] = line


