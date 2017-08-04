import random as r

from domain.BirdRepository import BirdRepository

class Game:
    def __init__(self,no_answers):
        self.__level = 0
        self.__no_answers = no_answers
        self.__question = None
        self.__answers = None
        self.__previous_questions = []

    def new_qestion(self):
        if self.__question not None:
            self.__previous_questions.append(self.__question)
            self.__question = None
            self.__answers = None
        if self.__level = 0:
            self.__question = self.__generate_question_by_difficulty(1)
            self.__answers = self.__generate_answers(self.__question,False)

    def __generate_question_by_difficulty(self,difficulty):
        bird_repository = BirdRepository()
        no_birds = bird_repository.no_birds()
        MAX_ITERATIONS = 100
        counter = 0
        while counter < MAX_ITERATIONS:
            bird_id_candidate = r.randint(0,no_birds - 1)
            bird_candidate = bird_repository.get_bird_by_id(bird_id_candidate)
            if not bird_id_candidate in self.__previous_questions:
                if bird_candidate.get_difficulty() == difficulty:
                    return bird_id_candidate
                    #break
            counter += 1
        if counter >= MAX_ITERATIONS:
            raise Exception("Probably there are not enough bird present with difficulty " + str(difficulty))

    def __generate_answers(self,question_id,same_order):
        bird_repository = BirdRepository()
        no_birds = bird_repository.no_birds()
        question_name = bird_repository.get_bird_by_id(question_id).get_name()
        answer_list = []
        if same_order:
            question_order = bird_repository.get_bird_by_id(question_id).get_order()
            bird_ids_same_order = bird_repository.get_bird_ids_by_order(question_order)
            while len(answer_list) < self.__no_answers:
                if len(bird_ids_same_order) > 0:
                    candidate_id = bird_ids_same_order.pop(r.randint(0,len(bird_ids_same_order)-1))
                    candidate_name = bird_repository.get_bird_by_id(candidate_id).get_name()
                    if question_name != candidate_name:
                        for answer in answer_list:
                            if candidate_name == bird_repository.get_bird_by_id(answer).get_name():
                                continue
                        answer_list.append(candidate_id)
                else:
                    break
        while len(answer_list) < self.__no_answers:
            candidate_id = r.randint(0,no_birds-1)
            candidate_name = bird_repository.get_bird_by_id(candidate_id).get_name()
            if question_name != candidate_name:
                for answer in answer_list:
                    if candidate_name == bird_repository.get_bird_by_id(answer).get_name():
                        continue
                answer_list.append(candidate_id)
        return answer_list
