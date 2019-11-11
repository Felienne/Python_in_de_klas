```python
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

while True:
  pygame.display.flip()
  screen.fill(backgroundColor)

  muis_rechthoek = muis_rechthoek.move(muis_snelheid)
  screen.blit(muis, muis_rechthoek)
  
  if muis_rechthoek.bottom < 0:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.bottom > 600:
      muis_snelheid[1] = - muis_snelheid[1]

  if muis_rechthoek.right < 0:
      muis_snelheid[0] = - muis_snelheid[0]

  if muis_rechthoek.right > 800:
      muis_snelheid[0] = - muis_snelheid[0]

  leeuw_rechthoek = leeuw_rechthoek.move(leeuw_snelheid)
  screen.blit(leeuw, leeuw_rechthoek)

  if leeuw_rechthoek.bottom < 0:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.bottom > 600:
      leeuw_snelheid[1] = - leeuw_snelheid[1]

  if leeuw_rechthoek.right < 0:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  if leeuw_rechthoek.right > 800:
      leeuw_snelheid[0] = - leeuw_snelheid[0]

  time.sleep(10 / 1000)
```

