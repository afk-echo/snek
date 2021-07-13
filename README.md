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

player = Snek(600, 300, 15) #initialise the window boundaries for the snek object(required for detecting collisions at the boundary) and delta(increment/decrement value for moving the Snek per frame)
```
### Methods for manipulating the snek.Snek object:
1. **<Snek>.move()**
```python
player.move([150,150]) #moves the Snek object by the delta value initialised earlier.
```
