from game_files.functions import load_image

class attack():
    def __init__(self,character,velocity):
        self.owner = character
        self.image,self.rec = load_image('shot1.png',size=(6,18))
        self.velocity = velocity
        self.x= character.x+character.rec.width/2 - 6
        self.y= character.y
        self.curr_pos = [self.x,self.y]
        self.rec.topleft = self.curr_pos

    def death(self):
        if self.y<=0:
            self.owner.attacks.remove(self)
            del self
        else:
            return True

    def update_position(self):
        if self.death():
            self.y= self.rec.topleft[1]
            self.curr_pos = [self.x,self.y]

    def move(self,opponents):
        self.rec = self.rec.move(self.velocity)
        self.update_position()
        for i in opponents:
            if self.rec.colliderect(i.rec):
                opponents.remove(i)
                self.owner.attacks.remove(self)

    def draw(self,screen):
        screen.blit(self.image,self.rec)