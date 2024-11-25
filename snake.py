"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg
from tools import tracer_serpent
from collections import deque
from collections import namedtuple


pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
Cell=namedtuple('Cell',['x','y'])
snake = deque([Cell(x=10,y=15),Cell(x=11,y=15),Cell(x=12,y=15)])
direction = Cell(x=1,y=0)
running = True

pomme=Cell(x=5,y=5)

while running:

    clock.tick(20)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_RIGHT and direction != Cell(x=-1,y=0):
                direction = Cell(x=1,y=0)
            elif event.key == pg.K_LEFT and direction != Cell(x=1,y=0):
                direction = Cell(x=-1,y=0)
            elif event.key == pg.K_UP and direction != Cell(x=0,y=1):
                direction = Cell(x=0,y=-1)
            elif event.key == pg.K_DOWN and direction != Cell(x=0,y=-1):
                direction =Cell(x=0,y=1)

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
    screen.fill((0,0,0))


 #   for i in range (30):
#        for j in range (30):
 #           if (i+j)%2==0 : 
  #              x=i*20
   #             y=j*20
    #            width=20
     #           height=20
      #          rect=pg.Rect(x, y, width, height)
       #         pg.draw.rect(screen, (255,255,255), rect)

    
#    for z in snake:
 #       x=z[0]*20
  #      y=z[1]*20
   #     width=20
    #    height=20
     #   rect=pg.Rect(x, y, width, height)
      #  pg.draw.rect(screen, (255,0,0), rect)
    tracer_serpent(screen,snake)
        
    x=pomme.x*20
    y=pomme.y*20
    width=20
    height=20
    rect=pg.Rect(x, y, width, height)
    pg.draw.rect(screen, (0,255,0), rect)

    if Cell(x=snake[-1].x+direction.x,y=snake[-1].y+direction.y)==pomme : 
        snake.append(Cell(x=snake[-1].x+direction.x,y=snake[-1].y+direction.y))
        pomme=Cell(x=randint(0,29),y=randint(0,29))
        print (pomme)
    else : 
        snake.append(Cell(x=snake[-1].x+direction.x,y=snake[-1].y+direction.y))
        snake.popleft()

    for i in range(len(snake)):
        snake[i]=Cell(x=snake[i].x%30,y=snake[i].y%30)

    
    


    






    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()

