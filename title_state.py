import game_framework
from pico2d import *
import main_state
import main_state2


name = "TitleState"
image = None
back = None

class background:
    def __init__(self):
        self.bgm = load_music('story.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global image, back
    back = background()
    image = load_image('title.png')


def exit():
    global image, back
    del(image)
    del(back)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(600, 300)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






