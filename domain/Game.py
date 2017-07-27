import random as r

from domain.BirdRepository import BirdRepository

class Game:
    def __init__(self,no_birds,no_questions,no_answers,difficulty):
        self.__points = 0
        self.__no_answers = no_answers
        self.__questions = [None for i in range(no_questions)]
        self.__answers = [None for i in range(no_questions)]

        bird_repository = BirdRepository()
        for q in range(0,no_questions):
            #Liste __questions mit Zahlen (ID) füllen ohne Wiederholung
            while True:
                bird_id_candidate = r.randint(0,no_birds-1)
                bird_candidate = bird_repository.get_bird_by_id(bird_id_candidate)
                if not bird_id_candidate in self.__questions:
                    #Alle Vögel sollen die Schwierigkeit 1 haben
                    # QUESTION: was wenn weniger vögel da sind als gebraucht?
                    if bird_candidate.get_difficulty() == difficulty:
                        self.__questions[q] = bird_id_candidate
                        break;
            #Liste __answers mit Zahlen (ID) füllen ohne Wiederholung
            #ohne gleichen Namen
            answer_list = []
            while len(answer_list) < no_answers:
                bird_id_candidate = r.randint(0,no_birds-1)
                if bird_repository.get_bird_by_id(bird_id_candidate).get_name() == bird_repository.get_bird_by_id(self.__questions[q]).get_name():
                    continue
                is_different = True
                for a in answer_list:
                    if bird_repository.get_bird_by_id(bird_id_candidate).get_name() == bird_repository.get_bird_by_id(a).get_name():
                        is_different = False
                        break;
                if is_different:
                    answer_list.append(bird_id_candidate)

            #richtige Antwort zufällig platzieren
            pos_right_answer = r.randint(0,no_answers-1)
            answer_list[pos_right_answer] = self.__questions[q]
            self.__answers[q] = answer_list
        print(self.__questions)
        print(self.__answers)

    def get_question(self,q):
        return self.__questions[q],self.__answers[q]

    def is_correct(self,q,a):
        return self.__questions[q] == self.__answers[q][a]

    def add_points(self,points):
        self.__points += points

    def get_points(self):
        return self.__points
