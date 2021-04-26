import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Jogo Breakout")
pausado = False

cores = {
  "branco" : (255,255,255),
  "azulEscuro" : (36,90,190),
  "azulClaro" : (0,176,240),
  "vermelho" :(255,0,0),
  "laranja" : (255,100,0),
  "amarelo" : (255,255,0),
}

score = 0
vidas = 3

clock = pygame.time.Clock()

todosSprites = pygame.sprite.Group()

paddle = Paddle(cores["azulClaro"],100,10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(cores["branco"],10,10)
ball.rect.x = 345
ball.rect.y = 195

pause = pygame.image.load('./icon-pause-512.png')
pause = pygame.transform.scale(pause,(100,100))

todosBlocos = pygame.sprite.Group()
for i in range(7):
  bloco = Brick(cores["vermelho"],80,30)
  bloco.rect.x = 60 + i*100
  bloco.rect.y = 60
  todosSprites.add(bloco)
  todosBlocos.add(bloco)
for i in range(7):
  bloco = Brick(cores["laranja"],80,30)
  bloco.rect.x = 60 + i*100
  bloco.rect.y = 100
  todosSprites.add(bloco)
  todosBlocos.add(bloco)
for i in range(7):
  bloco = Brick(cores["amarelo"],80,30)
  bloco.rect.x = 60 + i*100
  bloco.rect.y = 140
  todosSprites.add(bloco)
  todosBlocos.add(bloco)

todosSprites.add(paddle)
todosSprites.add(ball)

jogando = True

while jogando:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      jogando = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        pausado = True
        tela.blit(pause, (0,500))
        pygame.display.update()
  while pausado:
    pygame.time.wait(100)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          pausado = False
      elif event.type == pygame.QUIT:
          pausado = False
          jogando = False

  tela.fill(cores["azulEscuro"])


  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    paddle.moverParaEsquerda(7)
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    paddle.moverParaDireita(7)


  if ball.rect.x >= 790 or ball.rect.x <= 0:
    ball.velocity[0] = -ball.velocity[0]
  if ball.rect.y < 40:
    ball.velocity[1] = -ball.velocity[1]
  if ball.rect.y > 590:
    ball.velocity[1] = -ball.velocity[1]
    vidas -= 1
    if vidas == 0:
      font = pygame.font.Font(None,74)
      text = font.render("Você Perdeu",1,cores["branco"])
      tela.blit(text,(250,300))
      font = pygame.font.Font(None,30)
      text = font.render(f"Sua Pontuação: {str(score)}",1,cores["branco"])
      tela.blit(text,(320,350))
      pygame.display.flip()
      pygame.time.wait(3000)

      jogando = False
  
  colisaoBlocosLista = pygame.sprite.spritecollide(ball,todosBlocos,False)
  for bloco in colisaoBlocosLista:
    ball.bounce()
    score += 100
    bloco.kill()
    if len(todosBlocos) == 0:
      font = pygame.font.Font(None,74)
      text = font.render("Você Ganhou",1,cores["branco"])
      tela.blit(text,(250,300))
      font = pygame.font.Font(None,30)
      text = font.render(f"Sua Pontuação: {str(score)}",1,cores["branco"])
      tela.blit(text,(320,350))
      pygame.display.flip()
      pygame.time.wait(3000)

      jogando = False

  pygame.draw.line(tela, cores["branco"], [0,38], [800,38],2)

  font = pygame.font.Font(None, 34)
  text = font.render("Pontuação: " + str(score),1,cores["branco"])
  tela.blit(text,(20,10))
  text = font.render("Vidas: " + str(vidas),1,cores["branco"])
  tela.blit(text,(700,10))
  
  if pygame.sprite.collide_mask(ball,paddle):
    ball.rect.x -= ball.velocity[0]
    ball.rect.y -= ball.velocity[1]
    ball.bounce()
  

  todosSprites.update()

  todosSprites.draw(tela)

  pygame.display.flip()

  clock.tick(60)


pygame.quit()