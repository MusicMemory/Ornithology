import random as r

from domain.BirdRepository import BirdRepository

class Game:
    def __init__(self,no_birds,no_questions,no_answers,difficulty):
        self.__points = 0
        self.__no_answers = no_answers
        self.__questions = [-1 for i in range(no_questions)]
        self.__answers = [-1 for i in range(no_questions)]
        self.__bird_repository = BirdRepository()
        for q in range(0,no_questions):
            #Liste mit Zahlen füllen ohne Wiederholung
            while True:
                bird_id_candidate = r.randint(0,no_birds-1)
                bird_candidate = self.__bird_repository.get_bird_by_id(bird_id_candidate)
                if not bird_id_candidate in self.__questions:
                    #Alle Vögel sollen die Schwierigkeit 1 haben
                    # QUESTION: was wenn weniger vögel da sind als gebraucht?
                    if bird_candidate.get_difficulty() == difficulty:
                        self.__questions[q] = bird_id_candidate
                        break;
            answer_list = []
            while len(answer_list) < no_answers:
                bird_id_candidate = r.randint(0,no_birds-1)
                if len(answer_list) == 0:
                    answer_list.append(bird_id_candidate)
                else:
                    is_different = True
                    for a in answer_list:
                        if bird_id_candidate == a:
                            is_different = False
                            break;
                    if is_different:
                        if self.__bird_repository.get_bird_by_id(bird_id_candidate).get_name() != self.__bird_repository.get_bird_by_id(self.__questions[q]).get_name():
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
