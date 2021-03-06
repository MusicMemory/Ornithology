import pygame
from domain.BirdRepository import BirdRepository
from domain.Game import Game
from domain.ImageRepository import ImageRepository
from gui.GUIProcessor import GUIProcessor

pygame.init()
display_width = 800
display_height = 800
no_questions = 10;
no_answers = 4;
key_map = {
    pygame.K_1 : 0,
    pygame.K_2 : 1,
    pygame.K_3 : 2,
    pygame.K_4 : 3,
    pygame.K_5 : 4,
    pygame.K_6 : 5,
    pygame.K_7 : 6,
    pygame.K_8 : 7
}

bird_repo = BirdRepository("birds.csv")
image_repo = ImageRepository("images")
gui_proc = GUIProcessor(display_width, display_height)
clock = pygame.time.Clock()


game = Game(bird_repo.no_of_birds(), no_questions, no_answers)

for q in range(0, no_questions):
    bird_id = game.get_bird_id_of_question(q)
    bird = bird_repo.find_bird_by_id(bird_id)
    image = image_repo.find_image_by_name(bird.get_filename())
    gui_proc.clear()
    gui_proc.set_image(image)
    for a in range(0, no_answers):
        answer_id = game.get_bird_id_of_answer_of_question_(q, a)
        bird_answer = bird_repo.find_bird_by_id(answer_id)
        gui_proc.set_nth_text(a, bird_answer.get_name())

    gui_proc.update()
    clock.tick()

    keypressed = False
    while not keypressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                try:
                    answer = key_map[event.key]
                    if answer >= no_answers:
                        continue
                except:
                    continue

                keypressed = True
                if game.is_correct(q, answer):
                    gui_proc.alert(True, bird.get_difficulty())
                    game.add_points(bird.get_difficulty())
                else:
                    gui_proc.alert(False, 0)

            gui_proc.update()
            pygame.time.wait(500)
            # clock.tick(30)

gui_proc.final(game.get_points())
gui_proc.update()

keypressed = False
while not keypressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()