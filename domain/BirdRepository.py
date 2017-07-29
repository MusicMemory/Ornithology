import csv

from base.Singleton import Singleton
from domain.Bird import Bird

class BirdRepository(metaclass=Singleton):

    def __init__(self, csvfile_name):
        self.__birds = []
        self.init(csvfile_name)

    def safe_bird(self, id, bird):
        self.__birds[id] = bird

    def get_bird_by_id(self, id):
        return self.__birds[id]

    def get_id_by_bird(self,bird):
        return self.__birds.index(bird)

    def no_birds(self):
        return len(self.__birds)

    def no_birds_by_order(self,order):
        n = 0
        for bird in self.__birds:
            if bird.get_order() == order:
                n += 1
        return n

    def get_bird_ids_by_order(self,order):
        b_id = []
        for bird in self.__birds:
            if bird.get_order() == order:
                b_id.append(self.get_id_by_bird(bird))
        return b_id

    def init(self, csvfile_name):
        with open(csvfile_name,encoding='utf-8') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                if row[0].upper().endswith(".JPG"):
                    bird = Bird(row[0], row[1], row[2], row[3])
                    self.__birds.append(bird)
