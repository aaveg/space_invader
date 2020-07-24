from game_files.functions import load_image
from game_files.attack import attack

class player():
    def __init__(self,im_name,screen_size):
        self.image, self.rec = load_image(im_name)#,size=(70,65))
        self.x= screen_size[0]/2 - self.rec.width/2.
        self.y= screen_size[1] - self.rec.height - 10
        self.velocity = [[0,0],[0,0]] # [[left,right],[up,down]]
        self.cur_pos=[self.x,self.y]
        self.attacks = []

    def create_attack(self,vel):
        self.attacks.append(attack(self,vel))

    def update_position(self):
        vx = sum(self.velocity[0])
        vy = sum(self.velocity[1])
        self.x, self.y = (self.x - vx, self.y - vy)
        self.cur_pos = [self.x, self.y]
        if self.x <= 0:
            self.x = 0
        if self.x >= (640-self.rec.width):
            self.x = 640-self.rec.width
        if self.y >= 480 - self.rec.height:
            self.y = 480 - self.rec.height
        if self.y <= 0:
            self.y = 0

    def move(self):
        vx = sum(self.velocity[0])
        vy = sum(self.velocity[1])
        self.rec=self.rec.move([vx,vy])
        self.update_position()

    def draw(self,screen):
        screen.blit(self.image,self.cur_pos)

