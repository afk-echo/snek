# snek
An open source Python library for the Snake retro game.

## Installation:

Pre-requisites: pygame - can be installed by running `pip install pygame`

1. Grab the latest release of snek [here](https://github.com/afk-echo/snek/releases).
2. Place it in your project's local directory.

### Usage

`import snek`

## The snek.Snek object:

```python
from snek import Snek
import pygame

width = 600
height = 450
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

player = Snek(600, 450, 15) #initialise the window boundaries for the Snek object(required for detecting collisions at the boundary) and delta(increment/decrement value for moving the Snek per frame)
```
### Methods for manipulating the snek.Snek object:
1. **snek.Snek.move(foodPos:list)**
```python
player.move([150,150]) #moves the Snek object by the delta value initialised earlier.
```
2. **player.draw(win:pygame.display)**
```python
player.draw(win) #draws the Snek object on the specified screen.
```
3. **snek.Snek.headCollidesWith(collideList:list)**
```python
player.headCollidesWith([[0,15], [15,30], [30,225], [90,60]]) #checks if the Snek object's head collides with the co-ordinates given in collideList
```
