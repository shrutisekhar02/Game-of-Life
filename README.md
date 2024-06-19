# Game-of-Life 

This repository contains the code for Conway's Game of Life written using Pygame. 

## Rules of the Game   

Each cell interacts with its eight neighbors (horizontal, vertical, and diagonal).

* Any live cell with fewer than two live neighbors dies (underpopulation).
* Any live cell with two or three live neighbors lives on to the next generation (survival).
* Any live cell with more than three live neighbors dies (overpopulation).
* Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Simulation Control  

- **Space:** Pause/Play  
- **Return:** Toggles between continuous simulation and step mode 
- **Up/Down arrow keys:** Increase/Decrease speed of continuous simulation (default is 5 fps) 
- **Right arrow key:** Generate next generation in step mode 
- **z:** Clears all live cells from the grid
- **r:** Generates a random distribution of live cells 
- **Predefined Initialization options:**<br>
  1- Boat (Still Life) <br>
  2- Pulsar (Oscillator) <br>
  3- Glider (Spaceship)

## Instructions to play
When the python file is run, user must first input the tile size in the terminal (feature to specify size of grid). A tile size of 20 is optimal. The game is initially paused, user can either add live cells or press r to generate a random distribution (or any of the predefined initialization options).Note the game must be paused in order to manually add live cells and game automatically pauses when grid is cleared.Rest of the simulation controls are given above.

