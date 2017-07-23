import csv

from base.Singleton import Singleton
from domain.Bird import Bird

class BirdRepository(metaclass=Singleton):

    def __init__(self, csvfile_name):
        self.__birds = []
        self.init(csvfile_name)

    def safe_bird(self, id, bird):
        self.__birds[id] = bird

    def find_bird_by_id(self, id):
        return self.__birds[id]

    def no_of_birds(self):
        return len(self.__birds)

    def init(self, csvfile_name):
        with open(csvfile_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                if row[0].upper().endswith(".JPG"):
                    bird = Bird(row[0], row[1], row[2], row[3])
                    self.__birds.append(bird)


##############################
# TEST-CODE
##############################

# repo = BirdRepository("../birds.csv")
# repo2 = BirdRepository()
# print(repo == repo2)
# for i in range(0, repo.no_of_birds()):
#     print(repo.find_bird_by_id(i))


