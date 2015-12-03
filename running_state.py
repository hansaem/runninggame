from pico2d import *
import random

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

class Background1:
    image = None
    def __init__(self, w, h):
        self.bgm = load_music('kuki.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()
        if Background1.image == None:
            self.image = load_image('test5.png')
        self.speed = 3
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0,0, self.screen_width-w,
        self.screen_height, w, 0)
    def update(self):
        self.left = (self.left + self.speed) % self.image.w





class Background2:
    image = None
    def __init__(self, w, h):
        if Background2.image == None:
            self.image = load_image('test.png')
        self.speed = 2
        self.left = 0
        self.screen_width = w
        self.screen_height = h
    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0,0, self.screen_width-w,
        self.screen_height, w, 0)
    def update(self):
        self.left = (self.left + self.speed) % self.image.w


class Grass:
    image = None
    image2 = None
    invisible_state, visible_state, down_state, up_state = 1, 2, 3, 4
    count_num = 0
    grass_number = 0    #생성되있는 바닥의 표시
    def __init__(self):
        print(Grass.grass_number)
        Grass.grass_number +=1       #생성되면 바닥 갯수 1개 증가
        self.x = 48+(Grass.grass_number -1) * 96    #바닥의 x좌표 각각 달라야 됨
        self.y = 48
        self.state = self.visible_state
        if Grass.image == None:
            self.image = load_image('badak.png')
        if Grass.image2 == None:
            self.image2 = load_image('badak(off).png')

    def draw(self):
        if self.state == self.invisible_state:
            self.image2.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)
    def update(self):
        if self.x == -48:
            self.x = 1296
            if self.state ==self.invisible_state or self.state == self.down_state or self.up_state:
                self.state = self.visible_state
                self.y = 48
            Grass.count_num += 1
            if (Grass.count_num % 20) == 18 or (Grass.count_num % 21) == 0:
                self.state = self.invisible_state
                self.y = 900
            elif (Grass.count_num %13) == 0 and self.state == self.visible_state:
                self.state = self.down_state
            elif (Grass.count_num %25) == 0 and self.state == self.visible_state:
                self.state = self.up_state

        self.x = self.x - 12
        if self.state == self.down_state and self.x <850 :
            self.y -= 5
        elif self.state == self.up_state and self.x <850 :
            self.y += 30

    def get_bb(self):
        return self.x - 50, self.y +32, self.x +50, self.y +35
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def __del__(self):
        Grass.count_num = 0
        Grass.grass_number = 0

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
        if (Grass.count_num > 10):
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



class Boy:
    jump_sound = None
    time =0
    running_state,  jump_state , down_state, db_state, dead_state = 0, 1, 2, 3, 4
    def __init__(self):
        self.goingdaed = 0
        self.totaljump = 0
        self.jumpnumber = 0
        self.x, self.y = 170, 109
        self.state = self.running_state
        self.frame = 0
        self.image = load_image('run.png')
        self.image2 = load_image('jump.png')
        self.image3 = load_image('badak(off).png')
        if Boy.jump_sound == None:
            Boy.jump_sound = load_wav('jump.wav')
            Boy.jump_sound.set_volume(32)

    def update(self):
        if self.state == self.running_state:
            self.frame = (self.frame +1) % 5
        elif self.state == self.jump_state:
            #print("jump")
            self.totaljump +=17
            self.time += 0.7
            self.frame = (self.frame +1) % 2
            self.y +=17
            if self.time >5:
                self.state = self.down_state
                self.time = 0
        elif self.state == self.db_state:
            #print("db")
            self.totaljump +=17
            self.time += 0.7
            self.frame = (self.frame +1) % 2
            self.y +=17
            if self.time >5:
                self.state = self.down_state
                self.time = 0
        elif self.state == self.down_state:
            #print("downnnnn")
            self.time = 0
            self.frame = (self.frame +1) % 2
            #if self.y == 109:
            #    self.time = 0
            #    self.state = self.running_state
            #    return
            self.y -=8

    def get_bb(self):
        return self.x - 18, self.y -26, self.x +18, self.y +25
    def draw_bb(self):
        draw_rectangle(*self.get_bb())



    def draw(self):
        if self.state == self.running_state:
            self.image.clip_draw(self.frame*45, 0, 40, 48, self.x, self.y)
        elif self.state == self.jump_state:
            self.image2.clip_draw(self.frame*49, 44, 36, 40, self.x, self.y)
        elif self.state == self.db_state:
            self.image2.clip_draw(self.frame*49, 44, 36, 40, self.x, self.y)
        elif self.state == self.down_state:
            self.image2.clip_draw(self.frame*62, 0, 51, 35, self.x, self.y)
        elif self.state == self.dead_state:
            self.image3.draw(self.x, self.y)
    def state_change(self):
        if self.state == self.running_state:
            self.state = self.jump_state
        elif self.state == self.jump_state:
            self.time = 0
            self.state = self.db_state

    def handle_events(self, event):
            if event.type == SDL_KEYDOWN and event.key == SDLK_x:
                self.jump_sound.play()
                if self.state == self.jump_state or self.state == self.down_state:
                    self.jumpnumber += 1
                    self.state = self.db_state
                    self.time = 0
                else:
                    self.state = self.jump_state
                    self.jumpnumber += 1
                    self.goingdaed = 1
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                if self.state == self.running_state:
                    pass
                else:
                    self.time = 0
                    self.state = self.down_state

# Game object class here

#def handle_events():
 #   global running
  #  events = get_events()
   # for event in events:
#        if event.type == SDL_QUIT:
 #           running = False
  #      elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
   #         running = False
#        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
 #           if boy.state == boy.jump_state or boy.state == boy.down_state:
  #              boy.state = boy.db_state
   #             boy.time = 0
    #        boy.state = boy.jump_state
     #   elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
      #      boy.state = boy.down_state





# finalization code

