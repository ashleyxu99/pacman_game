
# pacman_game

We're implementing some important functionality for a fully playable mini Pac-Man game. 
You could open it up in the Processing Python mode environment in the Processing lab.

## Pinky's AI

We'd like to give Pinky some rudimentary AI, so that Pinky chases Pac-Man around the maze.

* Pinky needs to decide which direction to go whenever he is at an intersection. Whether he goes up, down, right, or left should depend on where Pac-Man is with respect to Pinky.
* The Processing coordinate space increases along the X axis from left to right, and increases along the Y axis from top to bottom. So the upper left corner's coordinates are `0, 0` the lower right corner's coordinates (in this canvas) are `599, 599`.
* Dividing a number by its absolute value (`abs()`) is a handy way to isolate the number's sign.
* Pinky's eye movements, as currently implemented, follow the location of Pac-Man. 

## Eating the dots

To get the dot-eating functionality working, we worked on `pacman.py`, `maze.py`, and `dots.py`. We figured out:  

* How the objects relate to each other in the game. Which object has access to which other objects?
* How the individual dots are displayed, and how the full collection of dots is represented within the context of the maze?
* How the conditions for winning (setting game controller's player_wins attribute) are evaluated?

## Implement tests
Run Pytest from the command line in your sketch's directory. I have implemened the tests so that they successfully test the dot-eating functionality.

![pacman](https://user-images.githubusercontent.com/76242903/129495595-5749a94d-28f2-4709-afcc-e4f41dc2b188.png)
