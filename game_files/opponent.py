from game_files.functions import load_image
import random

class opponent():
    def __init__(self,im_name,screen_size):
        self.image, self.rec = load_image(im_name)  # ,size=(100,90))
        self.x = (screen_size[0] - self.rec.width) * (random.random())
        self.y = 0
        self.velocity = [3, 0]
        self.cur_pos = [self.x, self.y]
        self.rec.topleft = tuple(self.cur_pos)

    def update_position(self):
        self.x, self.y = (self.rec.left, self.rec.top)
        self.cur_pos = [self.x, self.y]
        if self.x <= 0:
            self.velocity = [3, 0]
        if self.x >= (640 - self.rec.width):
            self.velocity = [-3, 0]

    def move(self):
        self.rec = self.rec.move(self.velocity)
        self.update_position()

    def draw(self,screen):
        screen.blit(self.image, self.rec)
