import pygame
import sys

from domain.BirdRepository import BirdRepository
from domain.Game import Game
from domain.ImageRepository import ImageRepository
from gui.GUIProcessor import GUIProcessor

pygame.init()
display_width = 800
display_height = 800
no_questions = 10
no_answers = 4
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

bird_repository = BirdRepository("birds.csv")
image_repository = ImageRepository("images")
gui_processor = GUIProcessor(display_width, display_height)
clock = pygame.time.Clock()
#start:
gui_processor.start()
gui_processor.update()
keypressed = False
while not keypressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            try:
                difficulty = key_map[event.key]
                difficulty += 1
                print("keymap",key_map[event.key])
                print("difficulty",difficulty)
                if difficulty < 1 & difficulty > 3:
                    continue
            except:
                continue
            keypressed = True
#Spiel:
game = Game(bird_repository.no_birds(),no_questions,no_answers,difficulty)
for q in range(no_questions):
    question,answers = game.get_question(q)
    bird = bird_repository.get_bird_by_id(question)
    image = image_repository.load_image(bird.get_filename())
    gui_processor.clear()
    gui_processor.set_image(image)
    for a in range(len(answers)):
        bird_answer = bird_repository.get_bird_by_id(answers[a])
        gui_processor.set_nth_text(a,bird_answer.get_name())

    gui_processor.update()
    clock.tick()

    keypressed = False
    while not keypressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                try:
                    answer = key_map[event.key]
                    if answer >= no_answers:
                        continue
                except:
                    continue

                keypressed = True
                if game.is_correct(q,answer):
                    game.add_points(bird.get_difficulty())
                    gui_processor.alert(True,bird.get_difficulty())
                else:
                    gui_processor.alert(False,0)

            gui_processor.update()
            pygame.time.wait(500)
#Final
gui_processor.final(game.get_points())
gui_processor.update()

keypressed = False
while not keypressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
