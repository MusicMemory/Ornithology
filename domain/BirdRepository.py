import csv
from domain.Bird import Bird

class BirdRepository:

    def __init__(self, csvfile_name):
        self.__birds = []
        self.init(csvfile_name)

    def safeBird(self, id, bird):
        self.__birds[id] = bird

    def findBirdById(self, id):
        return self.__birds[id]

    def noOfBirds(self):
        return len(self.__birds)

    def init(self, csvfile_name):
        with open(csvfile_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                if row[0].upper().endswith(".JPG"):
                    bird = Bird(row[0], row[1], row[2], row[3])
                    self.__birds.append(bird)


# repo = BirdRepository("../birds.csv")
# for i in range(0, repo.noOfBirds()):
#     print(repo.findBirdById(i))

