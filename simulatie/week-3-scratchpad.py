import pygame
import time
import random

pygame.init()
breedte = 800
hoogte = 600
backgroundColor = 0, 0, 0
screen = pygame.display.set_mode((breedte, hoogte))

muis = pygame.image.load("muis.png")
muis_rechthoek = muis.get_rect()
muis_snelheid = [1, 1]
muis_rechthoek = muis_rechthoek.move(random.randint(0, 400), random.randint(0,  250))

leeuw = pygame.image.load("leeuw-a.png")
leeuw_rechthoek = leeuw.get_rect()
leeuw_snelheid = [1, 1]
leeuw_rechthoek = leeuw_rechthoek.move(random.randint(0, 400), random.randint(0,  250))

# kaas = pygame.image.load("kaas.png")
# kaas_rechthoek = kaas.get_rect()
# kaas_rechthoek = kaas_rechthoek.move(200, 300)
# kaas_rechthoek = kaas_rechthoek.inflate(150, 150)
# kaas_rechthoek = kaas_rechthoek.inflate(150, 150)



while True:
  pygame.display.flip()
  screen.fill(backgroundColor)

  screen.blit(muis, muis_rechthoek)
  muis_rechthoek = muis_rechthoek.move(muis_snelheid)

  if muis_rechthoek.bottom < 0:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.bottom > 600:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.right < 0:
      muis_snelheid[0] = - muis_snelheid[0]

  if muis_rechthoek.right > 800:
      muis_snelheid[0] = - muis_snelheid[0]

  screen.blit(leeuw, leeuw_rechthoek)
  leeuw_rechthoek = leeuw_rechthoek.move(leeuw_snelheid)

  if leeuw_rechthoek.bottom < 0:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.bottom > 600:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.right < 0:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  if leeuw_rechthoek.right > 800:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  # screen.blit(kaas, kaas_rechthoek)
  #
  # if muis_rechthoek.colliderect(kaas_rechthoek):
  #   print('hap hap')
  #
  # else:
  #   print('ik heb honger')

  time.sleep(10 / 1000)

