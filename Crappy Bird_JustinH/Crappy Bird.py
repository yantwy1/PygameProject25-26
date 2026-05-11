from gamelib import *

game = Game(800,600,"Flappy Bird")

#background image that scrolls left
day = Image("images/day.png",game) #image bg
day.resizeTo(game.width,game.height) #or 800,600
game.setBackground(day)

#bird animation
Red=Animation("images/Red.png",3,game,122/3,24,4)

Rockbot = Image("images/Rockbot.png",game)
Rock = Image("images/Rock.png",game)     

#bar
Plain=Animation("images/Plain.png",3,game,100/3,34,3)
Plain.resizeTo(game.width,110)
Plain.y = game.height -50

#coins
coin = Animation("images/ring2.png",64,game,512/8,512/8)
coin.x = 800
coin.setSpeed(2,90)

Rings = Animation("images/ring2.png",64,game,512/8,512/8)
Rings.x = 500
Rings.setSpeed(0,90)

f = Font(red,48,black,"Comic Sans MS")

Crappy = Image("images/Crappy.png",game)
Crappy.y = 100
Crappy.resizeTo(500,200)

Gameover = Image("images/Gameover.png",game)
Gameover.resizeTo(500,200)
Gameover.moveTo(420,200)

#sounds
point = Sound("sounds/point.ogg",0)
hit = Sound("sounds/hit.ogg",1)
die = Sound("sounds/die.ogg",2)
wing = Sound("sounds/wing.ogg",3)

Start = Image("images/Start.png",game)
Start.moveTo(150,500)
Start.resizeTo(260,200)

Quit = Image("images/Quit.png",game)
Quit.moveTo(180,500)
Quit.resizeTo(400,170)
#start screen
while not game.over:
  game.processInput()
  game.scrollBackground("left",4)
  Crappy.draw()
  Red.draw()
  Plain.draw()
  Start.draw()

  if keys.Pressed[K_SPACE]:
    game.over = True
  game.update(30)

#game screen
game.over = False
while not game.over:
  game.processInput()
  game.scrollBackground("left",4) #makes bg move

  Red.draw()
  coin.draw()
  Rock.draw()
  Rockbot.draw()
  Rockbot.moveTo(coin.x,coin.y + 230)
  Rock.moveTo(coin.x,coin.y - 200)
  Plain.draw()
  coin.move()
  Rings.draw()
  Rings.moveTo(750,game.height - 50)
  Rock.resizeTo(200,200)
  Rockbot.resizeTo(280,280)

  if keys.Pressed[K_SPACE]:
    Red.y -= 2 #decreases y of bird (move up)
    Red.rotateTo(10)#turns CCW
    wing.play()
  else:
      Red.y += 2
      Red.rotateTo(-10)

  if coin.x < -100:
    coin.visible = True
    coin.x = game.width + 100
    coin.y = randint(200,300)
     

  if Red.collidedWith(coin):
    game.score += 1
    coin.visible = False
    point.play()
    coin.speed += 1

  if (Red.collidedWith(Plain,"rectangle")
      or Red.collidedWith(Rock,"rectangle")
      or Red.collidedWith(Rockbot,"rectangle")
      or Red.y < 0):
    game.over = True
    hit.play()
  
  game.drawText(game.score,680,game.height - 85,f)

  game.update(70)

#end screen
die.play()
game.over = False
while not game.over:
  game.processInput()
  game.scrollBackground("left",3)
  Gameover.draw()
  Plain.draw()
  Quit.draw()

  if keys.Pressed[K_q]:
    game.over = True
  game.update(30)
game.quit()
