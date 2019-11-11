```python
import pygame
import time
pygame.init()
breedte = 800
hoogte = 600
backgroundColor = 0, 0, 0
screen = pygame.display.set_mode((breedte, hoogte))

muis = pygame.image.load("muis.png")
muis_rechthoek = muis.get_rect()
muis_snelheid = [0, 1]

leeuw = pygame.image.load("leeuw-a.png")
leeuw_rechthoek = leeuw.get_rect()
leeuw_snelheid = [1, 0]

while True:
  pygame.display.flip()
  screen.fill(backgroundColor)

  screen.blit(muis, muis_rechthoek)
  muis_rechthoek = muis_rechthoek.move(muis_snelheid)
  
  if muis_rechthoek.bottom < 0:
      muis_snelheid[1] = -muis_snelheid[1]

  if muis_rechthoek.bottom > 600:
      muis_snelheid[1] = -muis_snelheid[1]

  screen.blit(leeuw, leeuw_rechthoek)
  leeuw_rechthoek = leeuw_rechthoek.move(leeuw_snelheid)

  if leeuw_rechthoek.right < 0:
      leeuw_snelheid[0] = -leeuw_snelheid[0]

  if leeuw_rechthoek.right > 800:
      leeuw_snelheid[0] = -leeuw_snelheid[0]

  time.sleep(10 / 1000)
```

