import pygame, time, os, pygame_textinput, random, csv
pygame.init()
#screen
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ornithology')
#filename birds
folder_images = "images\\"
folder = "D:\\Dateien\\Informatik\\Python\\Ornithology\\"
#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
skyblue = (112,128,144)
#textinput
textinput = pygame_textinput.TextInput()
textinput.set_text_color(white)
textinput.set_cursor_color(white)
#clock
clock = pygame.time.Clock()

def get_bird_name(filename):
    #austerfischer_01.jpg -> Austernfischer
    return filename.split('_')[0].capitalize()

def print_image(filename):
    #Malt das Bild zentriert
    image = pygame.image.load(filename)
    image_rect = image.get_rect()
    w = image_rect.width//2
    h = image_rect.height//2
    screen.blit(image,(display_width//2-w,display_height//2-h))
    
def text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface,textSurface.get_rect()

def print_text(text):
    #Malt Text zentriert
    my_font = pygame.font.Font('vgafix.fon',1515)
    TextSurf, TextRect = text_objects(text, my_font)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf,TextRect)

def print_textinput():
    #Malt Textbox zentriert
    x = (display_width/2) - (textinput.get_surface().get_rect().width/2)
    screen.blit(textinput.get_surface(),(x,display_height-50))

def random_list(l):
    new_list = list()
    for i in range(3):
        new_list.append(l.pop(random.randint(0,len(l)-1)))
    return new_list

def csv_handler(csvfilename):
    with open(csvfilename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filenames = []
        for row in readCSV:
            if row[3] == '1':#schwierigkeit 1
                if row[0].endswith(".jpg"):#sicher ist sicher
                    filenames.append(row[0])
    return filenames

def menu_loop():
    menuExit = False
    while not menuExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                menuExit = True
        screen.fill(white)
        print_text("Press any key!")
        pygame.display.update()
        clock.tick(30)

def game_loop():
    #neues Spiel
    gameExit = False
    answer = ""
    score = 0
    #Liste dateinamen im Ordner images
    birds = csv_handler("birds.csv")
    #
    #birds = os.listdir(folder_images)
    bird = birds.pop(len(birds)-1)
    #loop
    while not gameExit:    
        #event handler
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #textinput
        if textinput.update(events):
            answer = textinput.get_text()
            #answer right?
            if answer == get_bird_name(bird):
                score += 1
            else:
                score -= 1
            #next image bird?
            if len(birds) > 0 :
                bird = birds.pop(len(birds)-1)
            else:
                score=10000
        #painting
        screen.fill(black)
        print_image(folder_images+bird)
        print_text(str(score))
        print_textinput()

        pygame.display.update()
        clock.tick(30)

#lets go
menu_loop()        
game_loop()
pygame.quit()
quit()
