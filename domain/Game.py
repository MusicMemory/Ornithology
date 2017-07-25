import random

from domain.BirdRepository import BirdRepository

class Game:

    """
    Erstellt ein Spiel: Der Konstruktor wählt zufällig no_questions (verschiedene) Vögel (-Ids)
    aus und dazu jeweils no_answers mögliche Anworten (in Form von Vogel-Ids), wobei genau eine
    Antwort richtig ist.
    """

    def __init__(self, no_images, no_questions, no_answers):
        self.__points = 0
        self.__question_bird_ids = [-1 for i in range(no_questions)]
        self.__answer_bird_ids = [[-1 for i in range(no_answers)] for j in range(no_questions)]

        for q in range(0, no_questions):
            # Nächsten Vogel zufällig bestimmen (ohne Wiederholung)
            while True:
                image_id_candidate = random.randint(0, no_images-1)             #Zahlen
                if (not (image_id_candidate in self.__question_bird_ids)):
                    self.__question_bird_ids[q] = image_id_candidate
                    break;

            # Erst werden no_answers falsche Antworten gerwählt
            #
            answer_list = []
            while len(answer_list) < no_answers:
                answer_id_candidate = random.randint(0, no_images-1)
                if (self.__is_answer_different_from_previous(q, answer_list, answer_id_candidate)):
                    answer_list.append(answer_id_candidate)

            # Anschließend wird die richtige Antwort an einer zufälligen Stelle
            # der bisherigen (falschen) Antworten überschrieben
            #
            right_answer = random.randint(0, no_answers-1)
            answer_list[right_answer] = self.__question_bird_ids[q]

            # Die fertige Antwortliste mit einer richitigen und dem Rest falschen
            # Antworten in die Member-Variabele...
            for a in range(0, no_answers):
                self.__answer_bird_ids[q][a] = answer_list[a]

    ##############################
    # Public
    ##############################

    # Gibt die Vogel-Id zur q-ten Frage zurück
    def get_bird_id_of_question(self, q):
        return self.__question_bird_ids[q]

    # Gibt die Vogel-Id der a-ten Antwort zur q-ten Frage zurück
    def get_bird_id_of_answer_of_question_(self, q, a):
        return self.__answer_bird_ids[q][a]

    # Testet, ob die a-te Antwort (von Benutzer gewählt) für der q-te Frage
    # richtig ist.
    def is_correct(self, q, a):
        return self.__question_bird_ids[q] == self.__answer_bird_ids[q][a]

    def add_points(self, points):
        self.__points += points

    def get_points(self):
        return self.__points


    ##############################
    # Private
    ##############################

    def __is_answer_different_from_previous(self, q, answer_list, answer_id_candidate):
        bird_name_of_question = self.__bird_name_by_bird_id(self.get_bird_id_of_question(q))
        bird_name_of_answer_candidate = self.__bird_name_by_bird_id(answer_id_candidate)
        if (bird_name_of_question == bird_name_of_answer_candidate):
            return False
        bird_names_of_previous_answers = self.__bird_names_by_bird_ids(answer_list)
        return not(bird_name_of_answer_candidate in bird_names_of_previous_answers)

    def __bird_name_by_bird_id(self, bird_id):
        birdRepoSingleton = BirdRepository()
        return birdRepoSingleton.find_bird_by_id(bird_id).get_name()

    def __bird_names_by_bird_ids(self, bird_ids):
        bird_names = []
        for id in bird_ids:
            bird_names.append(self.__bird_name_by_bird_id(id))
        return bird_names;


##############################
# TEST-CODE
##############################

# birdRepo = BirdRepository("../birds.csv")
# game = Game(50, 10, 4)
# for i in range(0, 10):
#     bird_id_question = game.get_bird_id_of_question(i)
#     print(str(bird_id_question) +
#           " -> " + birdRepo.find_bird_by_id(bird_id_question).get_name())
#     print("-----")
#     for j in range(0, 4):
#         bird_id_answer = game.get_bird_id_of_answer_of_question_(i, j)
#         print(str(bird_id_answer) +
#               " -> " + birdRepo.find_bird_by_id(bird_id_answer).get_name() +
#               " -> " + str(game.is_correct(i, j)))
#     print("=======================================")
