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

       model = self.loader.loadModel('models/sky_sphere')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/stars_1k_tex.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(0,0,0)
       model.setScale(50, 50, 50)
       model.setHpr(90, 0,0)


       model = self.loader.loadModel('models/Fighter')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/FighterTexture.tif')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(0, 10, 0)
       model.setScale(0.5, 0.5, 0.5)
       model.setHpr(-45, 0,0)

       model = self.loader.loadModel('models/banana')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/banana.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(-20, 5, 0)
       model.setScale(2, 2, 2)
       model.setHpr(0, 90, 0)

       model = self.loader.loadModel('models/candycane')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/candycane.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(-10, -5, 0)
       model.setScale(2, 2, 2)
       model.setHpr(0, 45, 0)

       model = self.loader.loadModel('models/planet_sphere')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/sun_1k_tex.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(15, 0, 0)
       model.setScale(6, 6, 6)
       model.setHpr(0, 0, 0)

       model = self.loader.loadModel('models/planet_sphere')
       model.reparentTo(self.render)

       base_texture = loader.loadTexture('models/venus_1k_tex.jpg')
       model.setTexture(base_texture)

       # model.setColor((1, 1, 1, 1))

       model.setPos(15, 0, 0)
       model.setScale(6, 6, 6)
       model.setHpr(0, 0, 0)

       base.camLens.setFov(90)

game = Game()
game.run()