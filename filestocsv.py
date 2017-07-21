import csv, os
filenames = os.listdir("images/")
print(filenames)
with open('birds.csv','w') as csvfile:
    csvfile_writer = csv.writer(csvfile,delimiter=';',lineterminator='\n')
    csvfile_writer.writerow(['filename','name','order','difficulty,hallighooge'])
    for name in filenames:
        #name = name.rstrip()
        csvfile_writer.writerow([name,'','','','1'])
csvfile.close()
