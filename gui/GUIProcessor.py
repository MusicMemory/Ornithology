import pygame
from pygame.rect import Rect

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)

no_answer_lines = 2;
height_answer = 40;
width_answer = 400;

class GUIProcessor:

    def __init__(self, width, height):
        self.screen = screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.margin_left = width // 8;
        self.font_answer = pygame.font.SysFont('Comic Sans MS', 30)
        self.font_correct = pygame.font.SysFont('Comic Sans MS', 40)


    def clear(self):
        self.screen.fill(black)

    def set_image(self, image):
        image_scaled = pygame.transform.scale(image, (600, 450))
        rect = image_scaled.get_rect()
        w = rect.width//2
        self.screen.blit(image_scaled, (self.width//2-w, 50))

    def set_nth_text(self, n, text):
        textsurface = self.font_answer.render(str(n+1) + '. ' + text, True, white)
        text_margin_top = self.height - no_answer_lines * height_answer - 100;
        text_y_coord = text_margin_top + n//2 * height_answer;
        if (n % 2 == 0):
            self.screen.blit(textsurface,(self.margin_left, text_y_coord))
        else:
            self.screen.blit(textsurface,(self.margin_left + width_answer, text_y_coord))

    def alert(self, trueOrFalse, points):
        text = "richtig   +" + str(points) if trueOrFalse else "falsch"
        color = green if trueOrFalse else red
        pygame.draw.rect(self.screen, color, Rect((200,520),(400,70)))
        textsurface = self.font_correct.render(text, True, white)
        self.screen.blit(textsurface,(360, 543))

    def final(self, sum_points):
        self.screen.fill(black)
        text = "Sie haben " + str(sum_points) + " Punkte erreicht."
        textsurface = self.font_correct.render(text, True, white)
        self.screen.blit(textsurface,(250, 400))

    def update(self):
        pygame.display.update()