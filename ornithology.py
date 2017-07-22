import pygame, pygame_textinput, random, csv
pygame.init()
#screen
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ornithology')
#filename birds
folder_images = "images/"
#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
skyblue = (112,128,144)
bright_skyblue = (130,140,200)
#textinput
textinput = pygame_textinput.TextInput()
textinput.set_text_color(white)
textinput.set_cursor_color(white)
#clock
clock = pygame.time.Clock()

class Bird:
    def __init__(self,filename,name,order,difficulty):
        #in python gint es keine expliziten konstruktoren
        #__name meint private, _name protected, name public 
        self.__filename=filename 
        self.__name=name
        self.__order=order
        self.__difficulty=difficulty

    def get_filename(self):
        return self.__filename

    def get_name(self):
        return self.__name

    def get_order(self):
        return self.__order

    def get_difficulty(self):
        return self.__difficulty

def get_bird_name(filename):
    #austerfischer_01.jpg -> Austernfischer
    return filename.split('_')[0].capitalize()

def print_image(filename):
    #Malt das Bild zentriert
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image,(800,600))
    image_rect = image.get_rect()
    w = image_rect.width//2
    h = image_rect.height//2
    screen.blit(image,(display_width//2-w,display_height//2-h))
    
def text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface,textSurface.get_rect()

def print_text(text):
    #Malt Text zentriert
    my_font = pygame.font.Font('freesansbold.ttf',20)
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

def csv_to_birds(csvfilename):
    with open(csvfilename,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        birds = []
        for row in readCSV:
            if row[0] != "filename":
                birds.append(Bird(row[0],row[1],row[2],row[3]))
    return birds

def draw_button(m,bx,by,bw,bh,c1,c2,t):
    #wenn maus im rechteck, dann andere Farbe -> interaktiv
    if bx + bw > m[0] > bx and by + bh > m[1] > by:
        pygame.draw.rect(screen,c1,(bx,by,bw,bh))
    else:
        pygame.draw.rect(screen,c2,(bx,by,bw,bh))
    my_font = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(t,my_font)
    #center of button
    textRect.center = ((bx+(bw/2)),(by+(bh/2)))
    screen.blit(textSurf,textRect)

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
        #hier soll ein button entstehen
        mouse = pygame.mouse.get_pos()
        #print(mouse_pos)
        draw_button(mouse,150,450,100,50,bright_skyblue,skyblue,"Start")
        draw_button(mouse,550,450,100,50,bright_skyblue,skyblue,"Start")

        print_text("Press any key!")
        pygame.display.update()
        clock.tick(15)

def game_loop():
    #neues Spiel
    gameExit = False
    answer = ""
    score = 0
    #Liste dateinamen im Ordner images
    birds = csv_to_birds("birds.csv")
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
