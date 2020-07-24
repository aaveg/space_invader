from game_files.functions import load_image

class background():
    def __init__(self,im_name,screen_size):
        self.image, self.rec = load_image(im_name, size=screen_size)
        self.image1, self.rec1 = load_image(im_name, size=screen_size)
        self.rec1.topleft = self.rec.bottomleft
        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = screen_size[1]
        self.velocity = [0, 1]
        self.cur_pos = [self.x, self.y]
        self.cur_pos1 = [self.x1, self.y1]

    def update_position(self):
        [self.x, self.y] = [self.x + self.velocity[0], self.y + self.velocity[1]]
        [self.x1, self.y1] = [self.x1 + self.velocity[0], self.y1 + self.velocity[1]]

        if self.rec1.bottomleft[1] <= 480:
            self.rec.topleft = self.rec1.bottomleft
        if self.rec.bottomleft[1] <= 480:
            self.rec1.topleft = self.rec.bottomleft
        if self.rec.topleft[1] >= 0:
            self.rec1.bottomleft = self.rec.topleft
        if self.rec1.topleft[1] >= 0:
            self.rec.bottomleft = self.rec1.topleft

        self.cur_pos = [self.x, self.y]
        self.cur_pos1 = [self.x1, self.y1]

    def move(self):
        self.rec = self.rec.move(self.velocity)
        self.rec1 = self.rec.move(self.velocity)
        self.update_position()

    def draw(self,screen):
        screen.blit(self.image, self.rec)
        screen.blit(self.image1, self.rec1)

