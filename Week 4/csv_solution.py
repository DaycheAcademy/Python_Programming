
email = list()
year = list()
name = list()
surname = list()


with open('sample.csv') as csv_file:
    line = csv_file.readline().split(';')
    while line:
        email.append(line[0])
        year.append(line[1])
        name.append(line[2])
        surname.append(line[3])
        line = csv_file.readline().split(';')
