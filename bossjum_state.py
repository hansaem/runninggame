from pico2d import *
from main_state2 import *
import random

class Background1:
    image = None
    def __init__(self, w, h):
        self.bgm = load_music('boss.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
        if Background1.image == None:
            self.image = load_image('boss.png')
        self.speed = 3
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        self.image.draw(600,300)
    def update(self):
        pass

class Dead:
    image = None
    life_state , dead_state = 0, 1
    def __init__(self):
        self.state = self.life_state
        if Dead.image == None:
            self.image = load_image('game_over.png')
    def draw(self):
        self.image.draw(600, 300)
    def update(self):
        pass

class GONG:
    a = 0
    image = None
    def __init__(self):
        if GONG.image == None:
            self.image = load_image('gong.png')
        GONG.a +=1
        self.x = 300
        self.y = 200 * GONG.a
    def draw(self):
       self.image.draw(self.x, self.y)
    def update(self):
        pass

class Grass11:
    image = None
    count_num = 0
    grass_number = 0    #생성되있는 바닥의 표시
    def __init__(self):
        self.x = 600    #바닥의 x좌표 각각 달라야 됨
        self.y = 48
        if Grass11.image == None:
            self.image = load_image('badak2.png')
    def draw(self):
            self.image.draw(self.x, self.y)
    def update(self):
       pass

    def get_bb(self):
        return self.x - 600, self.y -50, self.x +600, self.y +35
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Airport:
    image = None
    low_state, hi_state,  wait_state = 0, 1, 2
    def __init__(self):
        self.time = 0
        self.state = random.randint(0, 1)
        if Airport.image == None:
            self.image = load_image('airport.png')
        self.x = 1400
        if self.state == self.low_state:
            self.y = 100
        elif self.state == self.hi_state:
            self.y = 800

    def draw(self):
          self.image.draw(self.x, self.y)

    def update(self):
        if (Grass11.count_num > 10):
            self.time += 20

            if self.time > 4000:
                if self.state == self.hi_state:
                    self.x -= 10
                    if self.x > 600:
                        self.y -= 9
                    elif (self.x < 600) and (self.x > 520):
                        self.x -= 10
                    elif self.x <500:
                        self.y += 9
                    if self.x < -100:
                        self.state = self.wait_state
                        self.x, self.y = 2000, 2000
                elif self.state == self.low_state:
                    self.x -= 50
                    if self.x < -100:
                        self.state = self.wait_state
                        self.x, self.y = 2000, 2000
                elif self.state == self.wait_state:
                    self.time +=2
                    if self.time > 10000:
                        self.state = random.randint(0, 1)
                        if self.state == self.hi_state:
                            self.x, self.y = 1400, 800
                        else:
                            self.x, self.y = 1400, 100
                        self.time = 0
    def get_bb(self):
        return self.x - 135, self.y -70, self.x +135, self.y +75
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Boss:
    round = None
    ohpaca = None
    stome = None
    round_state, ohppaca_state, stom_state, airport_state, gaci_state = 0, 1, 2, 3, 4
    def __init__(self):
        self.state2 = 0# 0일경우 충돌놉놉 1일경우 충돌가능
        self.time = 0
        self.hp = 100
        self.x = 1100
        self.y = 120
        self.frame = 0
        self.frame2 = 0
        self.rs = 0
        self.dir = -1
        self.speed = 10
        self.state = self.round_state
        self.st_x = 0#스톰의 x좌표
        if Boss.round == None:
            Boss.round = load_image('run_boss.png')
        if Boss.ohpaca == None:
            Boss.ohpaca = load_image('ohpaaca.png')
        if Boss.stome == None:
            Boss.stome = load_image('stom.png')
        self.font = load_font('font_cat.TTF', 40)

    def draw(self):
        self.font.draw(1000, 550, 'boss_hp : %d'%self.hp, (232,126,4))
        if self.state == self.round_state and self.dir == -1:
            Boss.round.clip_draw(self.frame * 100, 0 * 100, 100, 100, self.x, self.y)
        elif self.state == self.round_state and self.dir == 1:
            Boss.round.clip_draw(self.frame * 100,  100, 100, 100, self.x, self.y)
        elif self.state == self.ohppaca_state and self.rs == 0:
            Boss.ohpaca.clip_draw(self.frame * 185,  0, 162, 71, self.x, self.y)
        if self.state == self.stom_state:
            if self.dir == 1:
                Boss.round.clip_draw(self.frame * 100,  100, 100, 100, self.x, self.y)

                if self.state2 == 0:
                    Boss.stome.clip_draw(self.frame2 * 71, 0, 71, 125, self.st_x, 130)
                elif self.state2 == 1:
                    self.time+=0.2
                if self.time > 4:
                    Boss.stome.clip_draw(self.frame2* 57, 170, 54, 607, self.st_x, 350)
                    if self.time >10:
                        self.state2 = 0
                        self.time = 0
            elif self.dir == -1:
                Boss.round.clip_draw(self.frame * 100, 0 * 100, 100, 100, self.x, self.y)
                if self.state2 == 0:
                    Boss.stome.clip_draw(self.frame2 * 71, 0, 71, 125, self.st_x, 130)
                elif self.state2 == 1:
                    self.time+=0.2
                if self.time > 8:
                    Boss.stome.clip_draw(self.frame2* 57, 170, 54, 607, self.st_x, 350)
                    if self.time >10:
                        self.state2 = 0
                        self.time = 0

    def update(self):
        if  50 < self.hp <60 and self.y <150 and self.state == self.round_state:
            self.state = self.ohppaca_state
            self.rs = 0
        if self.hp < 30 and self.state == self.round_state:
            self.state = self.stom_state
        if self.state == self.stom_state:
            self.frame = (self.frame+1) % 8
            if self.frame2+1 == 2:
                self.state2 = 1
            else:
                self.frame2 = (self.frame+1) % 2
            if self.state2 == 1:
                self.frame2 = (self.frame+1) % 5
            if self.time == 0:
                self.st_x = Boy.x
            self.time += 0.2
            if self.time > 10:
                self.time = 0
        if self.state == self.round_state:
            self.frame = (self.frame+1) % 8
            if self.rs == 0:# 아래 오른쪽에서 왼쪽방향
                self.dir = -1
                self.x += -self.speed
                if self.x <=20: #끝에 다다를경우
                    self.dir = 1
                    self.rs = 1
            elif self.rs == 1: #올라가는 상태
                self.y+= 10
                if self.y >=570: # 다올라갔을경우
                    self.rs = 2
            elif self.rs == 2:#위에서 왼쪽 -> 오른쪽이동
                self.x += self.speed
                if self.x >1100:
                    self.dir = -1
                    self.rs =3
            elif self.rs == 3:#내려가는 경우
                self.y -= self.speed
                if self.y<= 120:
                    if self.speed < 80:
                        self.speed += 10
                    self.rs = 0
        if self.state == self.ohppaca_state:
            self.frame = (self.frame+1) % 4
            if self.rs ==0:
                self.x -= 10
                if self.x < -50:
                    self.y = 120
                    self.rs =1
            elif self.rs ==1:
                self.x -= 40
                if self.x < -50:
                    self.x = 1300
                    self.y = 120
                    self.rs = 0
                    self.state = self.round_state

    def get_bb(self):
        return self.x - 80, self.y -35, self.x +75, self.y +35
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Stome(Boss):
    def __init__(self):
        Boss.__init__(self)

    def get_bb(self):
        return self.st_x -30, 137, self.st_x+30,  563
    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Tanmak:
    image = None
    bgm = None
    def __init__(self):
        if Tanmak.bgm == None:
            Tanmak.bgm = load_wav('shot.wav')
            Tanmak.bgm.set_volume(32)
        if Tanmak.image == None:
            Tanmak.image = load_image('tanmak.png')
        self.x , self.y = Boy.x +3, Boy.y
        self.state = True
        self.bs = Boy.state2
        self.frame = 0
    def update(self):
        if self.x > 1200:
            self.state = False
        if self.x < 0:
            self.state = False
        if self.bs == 0 or self.bs == 2:
            self.x += 20
        elif self.bs == 3 or self.bs == 1:
            self.x -= 20
        self.frame +=(self.frame + 1)% 2
    def draw(self):
        self.image.clip_draw(self.frame*10, 0, 5, 6, self.x, self.y)

    def get_bb(self):
        return self.x - 3, self.y -3, self.x +2, self.y +3
    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Boy:
    jump_sound = None
    time =0
    right_stop_state, left_stop_state, right_run_state, left_run_state , jump_state , down_state, db_state, stand_state, dead_state = 0, 1, 2, 3, 4, 5, 6, 7, 8
    x , y = 170, 109
    state2 = right_stop_state
    def __init__(self):
        self.totaljump = 0
        self.x, self.y = 170, 109
        self.state = self.stand_state
        Boy.state2 = self.right_stop_state
        self.frame = 0
        self.image = load_image('stop2.png')
        self.image2 = load_image('jump.png')
        self.lsi = load_image('stop2_revers.png')
        self.rri = load_image('run.png')
        self.lri = load_image('run2.png')
        self.sti = load_image('stop2_revers.png')
        self.lji = load_image('jump_revers2.png')
        self.image3 = load_image('badak(off).png')
        if Boy.jump_sound == None:
            Boy.jump_sound = load_wav('jump.wav')
            Boy.jump_sound.set_volume(32)


    def update(self):
        Boy.x, Boy.y = self.x, self.y
        if self.state == self.jump_state:
            self.runningstate()
            self.totaljump +=17
            self.time += 0.7
            self.frame = (self.frame +1) % 2
            self.y +=17
            if self.time >5:
                self.state = self.down_state
                self.time = 0
        elif self.state == self.db_state:
            self.runningstate()
            self.totaljump +=17
            self.time += 0.7
            self.frame = (self.frame +1) % 2
            self.y +=17
            if self.time >5:
                self.state = self.down_state
                self.time = 0
        elif self.state == self.down_state:
            self.frame = (self.frame +1) % 2
            self.runningstate()
            if self.y == 109:
                self.time = 0
                self.state = self.stand_state
                return
            self.y -=17
        elif self.state == self.stand_state:
            self.runningstate()
            if Boy.state2 == self.right_stop_state and self.state == self.stand_state: # 오른쪽을 보며 멈춰 잇을경우
                self.frame = (self.frame +1) % 4
            elif Boy.state2 == self.left_stop_state and self.state == self.stand_state: # 왼쪽을 보며 멈춰 있는 경우
                self.frame = (self.frame +1) % 4
            elif Boy.state2 == self.right_run_state and self.state == self.stand_state: # 오른쪽을 보며 달릴경우
                self.frame = (self.frame +1) % 5
            elif Boy.state2 == self.left_run_state and self.state == self.stand_state: # 왼쪽을 보며 달릴경우
                self.frame = (self.frame +1) % 5

    def runningstate(self):

        if Boy.state2 == self.right_stop_state:
            pass
        elif Boy.state2 == self.right_run_state:

            self.x += 10
        elif Boy.state2 == self.left_stop_state:
            pass
        elif Boy.state2 == self.left_run_state:

            self.x -= 10


    def get_bb(self):
        return self.x - 25, self.y -26, self.x +24, self.y +30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())



    def draw(self):
        if self.state2 == self.right_stop_state and self.state == self.stand_state: # 오른쪽을 보며 멈춰 잇을경우
            self.image.clip_draw(self.frame*58, 0, 50, 42, self.x, self.y)
        elif self.state == self.jump_state : #점프중
            if self.state2 == self.right_run_state or self.state2 == self.right_stop_state:
                self.image2.clip_draw(self.frame*49, 44, 36, 40, self.x, self.y)
            elif self.state2 == self.left_run_state or self.state2 == self.left_stop_state:
                self.lji.clip_draw(self.frame*49, 44, 36, 40, self.x, self.y)
        elif self.state == self.db_state: #2단점프중
            if self.state2 == self.right_run_state or self.state2 == self.right_stop_state:
                self.image2.clip_draw(self.frame*49, 44, 36, 40, v.x, self.y)
            elif self.state2 == self.left_run_state or self.state2 == self.left_stop_state:
                self.lji.clip_draw(self.frame*23, 44, 36, 40, self.x, self.y)
        elif self.state == self.down_state: # 점프 후 내려가는중
            if self.state2 == self.right_run_state or self.state2 == self.right_stop_state:
                self.image2.clip_draw(self.frame*62, 0, 51, 35, self.x, self.y)
            elif self.state2 == self.left_run_state or self.state2 == self.left_stop_state:
                self.lji.clip_draw(self.frame*62, 0, 51, 35, self.x, self.y)
        elif self.state2 == self.left_stop_state and self.state == self.stand_state: # 왼쪽을 보며 멈춰 있는 경우
            self.lsi.clip_draw(self.frame*58, 0, 50, 42, self.x, self.y)
        elif self.state2 == self.right_run_state and self.state == self.stand_state: # 오른쪽을 보며 달릴경우
            self.rri.clip_draw(self.frame*45, 0, 40, 48, self.x, self.y)
        elif self.state2 == self.left_run_state and self.state == self.stand_state: # 왼쪽을 보며 달릴경우
            self.lri.clip_draw(self.frame*45, 0, 40, 48, self.x, self.y)
        elif self.state == self.dead_state:
            self.image3.draw(self.x, self.y)



    def handle_events(self, event):
            if event.type == SDL_KEYDOWN and event.key == SDLK_x:
                self.jump_sound.play()
                if self.state == self.jump_state or self.state == self.down_state:
                    self.state = self.db_state
                    self.time = 0
                self.state = self.jump_state
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                self.state = self.down_state
            if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                Boy.state2 = self.left_run_state
            if Boy.state2 == self.left_run_state and event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Boy.state2 = self.right_run_state
            if event.type == SDL_KEYUP and event.key == SDLK_LEFT:
                if Boy.state2 == self.right_run_state:
                    pass
                else:
                    Boy.state2 = self.left_stop_state
            if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                Boy.state2 = self.right_run_state
            if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
                if Boy.state2 == self.left_run_state:
                    pass
                else:
                    Boy.state2 = self.right_stop_state

