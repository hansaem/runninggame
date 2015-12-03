import random
import json
import os

from pico2d import *
from bossjum_state import *

import game_framework
import main_state



name = "MainState"

boy = None
font = None
grass1 = None
airport = None
bg = None
gong = None
boss = None
tanmak= None
stome = None
dead = None



def enter():
    global boy, grass1, airport, bg, gong, boss, tanmak, stome, dead
    boy = Boy()
    grass1 = [Grass11()for i in  range(14)]
    airport = Airport()
    bg = Background1(1200, 600)
    gong = [GONG()for i in range(2)]
    boss = Boss()
    tanmak = []
    stome = Stome()
    dead = Dead()



def exit():
    global boy, grass1, airport, bg, gong, boss, tanmak, stome, dead
    del(boy)
    del(grass1)
    del(airport)
    del(bg)
    del(gong)
    del(boss)
    del(tanmak)
    del(stome)
    del(dead)


def pause():
    pass


def resume():
    pass



def handle_events():
    global tanmak
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYUP and event.key == SDLK_z:
                t = Tanmak()
                t.bgm.play()
                tanmak.append(t)
        else:
            boy.handle_events(event)



def update():
    global boy, grass1, airport, bg, gong, boss, tanmak, stome, dead
    for tk in tanmak:
        tk.update()
        if tk.state == False:
            tanmak.pop(0)
    for tk in tanmak:
        if collide(tk, boss):
            tanmak.remove(tk)
            boss.hp -=1
    boy.update()
    if collide(boss, boy):
        dead.state = dead.dead_state
        boy.state = boy.dead_state
    for grass in grass1:#바닥 업데이트
        grass.update()
    airport.update()
    bg.update()
    boss.update()

def draw():
    global boy, grass1, airport, bg, gong, boss, tanmak, stome, dead
    clear_canvas()
    bg.draw()
    for gg in gong:#바닥 그리기
        gg.draw()
    for grass in grass1:#바닥 그리기
        grass.draw()
        grass.draw_bb()
    for tk in tanmak:
        tk.draw()
        tk.draw_bb()
    boy.draw_bb()
    boy.draw()
    airport.draw()
    airport.draw_bb()
    boss.draw()
    boss.draw_bb()
    stome.draw_bb()
    if dead.state == dead.dead_state:
        dead.draw()
    update_canvas()
    delay(0.05)


def collide(a , b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True



