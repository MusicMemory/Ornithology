import csv
with open('D:\\Dateien\\Informatik\\Python\\Ornithology\\birds.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    #print(readCSV)
    filenames = []
    names = []
    for row in readCSV:
        filename = row[0]
        name = row[1]
        filenames.append(filename)
        names.append(name)
            
    print(filenames)
    print(names[filenames.index('austernfischer_01.jpg')])
