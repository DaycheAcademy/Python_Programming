import shelve

names = ['Mehdi', 'Ali', 'Ahmad']
age = [18, 23, 36]
cities = ['Tehran', 'Arak', 'Kermanshah']

# with shelve.open('specifications', writeback=True) as p_file:
with shelve.open('specifications',) as p_file:
    p_file['names'] = names
    p_file['age'] = age
    p_file['cities'] = cities

    p_file['names'].append('Naser')
    # p_file['age'].append(17)

    temp_list = p_file['age']
    temp_list.append(17)
    p_file['age'] = temp_list

    for item in p_file:
        print(item, '\t', p_file[item])




