from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(90, 550)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
        self.state = random.randint(0, 1)

    def update(self):
        self.frame = (self.frame +1) % 8
        if self.state == 0:
            self.x += random.randint(1, 10)
            if self.x > 700:
                self.state = 1
        elif self.state == 1:
            self.x -= random.randint(1, 10)
            if self.x < 10:
                self.state = 0


    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)



# finalization code

close_canvas()