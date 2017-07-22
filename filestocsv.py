import csv
import os
import Bird

csv_filename = 'birds.csv'

def filename_to_name(filename):
    name = filename.split('_')[0].capitalize()
    return name
#start
with open(csv_filename,'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    birds = []
    for row in readCSV:
        if row[0] != "filename":
            birds.append(Bird.Bird(row[0],row[1],row[2],row[3]))
csvfile.close()
#birds ist eine liste entstanden aus der bereits existierenden csv datei
#filename ist eine liste von strings aus dem folder /images
filenames = os.listdir("images/")
with open(csv_filename,'w') as csvfile:
    csvfile_writer = csv.writer(csvfile,delimiter=';',lineterminator='\n')
    csvfile_writer.writerow(['filename','name','order','difficulty'])
    for bird in birds:
        #erst die bereits existierende csv datei "neu" schreiben

        #FEHLER WENN FILENAME NICHT DA ABER IN BIRDS
        
        filenames.remove(bird.get_filename())#keine doppelten filenames

        csvfile_writer.writerow([bird.get_filename(),bird.get_name(),bird.get_order(),bird.get_difficulty()])
    print(filenames)
    for filename in filenames:
        #name = name.rstrip()
        name = filename_to_name(filename)
        csvfile_writer.writerow([filename,name,'','','1'])
csvfile.close()
