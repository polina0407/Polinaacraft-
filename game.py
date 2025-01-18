from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager()
       self.land.loadLand("land.txt")

       x, y = self.land.loadLand("land.txt")
       self.hero = Hero((x // 2, y // 2, 2), self.land)

       model = self.loader.loadModel('models/backgrounds/sky_sphere')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/backgrounds/stars_1k_tex.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(11,10,10)
       model.setScale(50, 50, 50)
       model.setHpr(90, 0,0)


       model = self.loader.loadModel('models/grass/shrubbery')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/grass/img.png')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(0,0,0)
       model.setScale(10,10,10)
       model.setHpr(90, 0,0)


       base.camLens.setFov(90)

game = Game()
game.run()