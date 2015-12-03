import random

from pico2d import *

class Badak:


    image1 = None
    badak_number = 0

    def __init__(self):
        Badak.badak_number += 1
        self.x, self.y = 1100, random.randint(180, 230)
        self.state = self.w_cat
        self.frame = 0
        self.total_frame = 0.0
        self.image = None
        self.hp = 250
        self.attack = 45
        self.hitted_system = False
        if DancingCat.image1 == None:
            DancingCat.image1 = load_image('badak.png')
        if DancingCat.image2 == None:
            DancingCat.image2 = load_image('dancingcat_run.png')
        if DancingCat.image3 == None:
            DancingCat.image3 = load_image('dancingcat_attack.png')
        if DancingCat.image4 == None:
            DancingCat.image4 = load_image('dancingcat_hit.png')

    def handle_stand_by_cat(self,frame_time):
        self.x = self.x + 0
        self.image = DancingCat.image1
    def handle_walk_cat(self,frame_time):
        distance = DancingCat.WALK_SPEED_PPS *frame_time
        self.total_frame += DancingCat.FRAME_PER_ACTION_WALK * DancingCat.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 6
        self.x += (-distance)
        self.image = DancingCat.image2
    def handle_attack_cat(self,frame_time):
        self.total_frame += DancingCat.FRAME_PER_ACTION_ATTACKT * DancingCat.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 6
        self.image = DancingCat.image3
    def handle_hit_cat(self,frame_time):
        if (self.hitted_system == False):
            self.hitted_x = self.x + 20
            self.hitted_system = True
            self.hitted_count = 1
        self.hitted_h = 1.7
        distance = DancingCat.WALK_SPEED_PPS *frame_time
        self.x += distance
        if self.x < self.hitted_x-10:
            self.y +=self.hitted_h^self.hitted_count
        elif (self.x >self.hitted_x-10) and (self.x<self.hitted_x):
            self.y -=self.hitted_h^self.hitted_count
        if self.x >= self.hitted_x:
            self.state = self.sb_cat
            self.hitted_system = False
            return





    def update(self, frame_time):
        self.handle_state[self.state](self,frame_time)
    def draw(self):
        self.draw_bb()
        if self.state == self.w_cat:
            self.image.clip_draw(self.frame*80, 0 , 60, 72, self.x, self.y)
        elif self.state == self.a_cat:
            self.image.clip_draw(self.frame*99, 0 , 99, 71, self.x, self.y)
        elif self.state == self.sb_cat:
            self.image.clip_draw(self.frame*0, 0 , 59, 71, self.x, self.y)
        elif self.state == self.h_cat:
            self.image.clip_draw(self.frame*0, 0 , 59, 71, self.x, self.y)

    def get_bb(self):
        return self.x-30 ,self.y - 35 , self.x +30 , self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    handle_state = {
                sb_cat: handle_stand_by_cat,
                w_cat: handle_walk_cat,
                a_cat: handle_attack_cat,
                h_cat: handle_hit_cat
                }




