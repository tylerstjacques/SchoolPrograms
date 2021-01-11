def is_file_sorted(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    lst = []
    for line in lines:
        lst.append(line)
    stripped_list = []
    for element in lst:
        new_element = element.strip('\n')
        stripped_list.append(new_element)
    stripped_list_copy = stripped_list[:]
    stripped_list_copy.sort()
    if stripped_list_copy == stripped_list:
        return True
    else:
        return False



trueFalse = is_file_sorted(filename)
