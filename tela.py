from pygame.locals import *

from sys import exit

pygame.init()

#criando tela
largura = 640
altura = 480
tela = pygame.display.setmode((largura, altura))

#alterando o nome do jogo
pygame.display.set_caption('Super Cin Brother')

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
  pygame.display.update()    
