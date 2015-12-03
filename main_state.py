import random
import json
import os

from pico2d import *
from running_state import *

import game_framework
import title_state
import main_state2
import dead_state


name = "MainState"

boy = None
font = None
grass1 = None
airport = None
bg = None
bg2 = None
dead = None



def enter():
    global boy, grass1, airport, bg, bg2 ,dead
    boy = Boy()
    grass1 = [Grass()for i in  range(14)]
    airport = Airport()
    bg = Background1(1200, 600)
    bg2 = Background2(1200, 600)
    dead = Dead()



def exit():
    global boy, grass1, airport, bg, bg2, dead
    del(boy)
    for grass in grass1:#바닥 업데이트
        del(grass)
    del(grass1)
    del(airport)
    del(bg)
    del(bg2)
    del(dead)


def pause():
    pass


def resume():
    pass


def handle_events():
    global dead
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif dead.state == dead.dead_state:
            if event.type == SDL_KEYDOWN and event.key == SDLK_r:
                game_framework.change_state(dead_state)
        else:
            boy.handle_events(event)


def update():
    global boy, grass1, airport, bg, bg2, dead
    boy.update()
    for grass in grass1:#바닥 업데이트
        grass.update()
    airport.update()
    bg.update()
    bg2.update()
    for grass in grass1:
        if boy.state == boy.running_state:
                if (collide(grass, boy) == False) and (grass.x<237) and (grass.x>103) :#걷다가 바닥이 없을때
                    boy.y -= 10#떨어진다
                    boy.goingdead = 1
                elif collide(grass, boy) and boy.y == 109:#걷는다 바닥이 있다 해당줄에
                    boy.goingdaed = 0
        if boy.state == boy.down_state:

            if collide(grass,boy) and boy.goingdaed == 1:
                boy.state = boy.running_state

    if collide(airport, boy):
        dead.state = dead.dead_state
        boy.state = boy.dead_state
    elif boy.y < 0:
        dead.state = dead.dead_state
    for grass in grass1:
        if grass.count_num > 50:
            game_framework.change_state(main_state2)


def draw():
    global boy, grass1, airport, bg, bg2, dead
    clear_canvas()
    bg.draw()
    bg2.draw()

    for grass in grass1:#바닥 그리기
        grass.draw()
        grass.draw_bb()
    boy.draw_bb()
    boy.draw()
    airport.draw()
    airport.draw_bb()
    if dead.state == dead.dead_state:
        dead.draw()
    update_canvas()
    delay(0.03)


def collide(a , b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


