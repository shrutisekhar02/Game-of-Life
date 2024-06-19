import pygame
import time
import random
import numpy as np

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0) 
yellow= (255,255,0) 
grey=(128,128,128)

display_width = 800
display_height = 800 

tile_size=int(input("Enter tile size (pixels)\n[Note: Enter values between 5 and 50] :"))

grid_height=display_width//tile_size
grid_width=display_height//tile_size


gameDisplay = pygame.display.set_mode((display_width, display_height))   
pygame.display.set_caption('Game of Life') 
clock = pygame.time.Clock() 


def draw_grid(positions):
    
    #to make a box yellow when clicked- postions gives the row,column of mouse click
    for position in positions:
        x,y=position
        pygame.draw.rect(gameDisplay,yellow,(x*tile_size,y*tile_size,tile_size,tile_size))

    #(0,0) is top left
    for x in range(grid_height):
        pygame.draw.line(gameDisplay,black,(0,x*tile_size),(display_width,x*tile_size))
    for y in range(grid_width):
        pygame.draw.line(gameDisplay,black,(y*tile_size,0),(y*tile_size,display_height)) 
        
def next_gen(positions):  #returns the positons of next generation

    #positions is a set of all live cells in a given generation
    all_nn=set() #set of all neighbours    
    new_positions=set() #set of the next gen positions

    def get_neigh(position): #gets ALL neighbours of a cell
        x, y = position
        neighbors = []
        for dx in [-1, 0, 1]:
            if x + dx <  0 or x + dx > grid_width:# end cases
                continue
            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > grid_height:# end cases
                     continue
                if dx == 0 and dy == 0:# same cell
                      continue
                neighbors.append((x + dx, y + dy))
    
        return neighbors

    for pos in positions: 
          
          neighbours=get_neigh(pos) 
          all_nn.update(neighbours) 

          live_neighbours=[n for n in neighbours if n in positions]#list of all live neighbours of a given cell 

          #only adding cells with 2 or 3 neighbours to the next generation (underpopulation and overpopulation handled)
          if len(live_neighbours) in [2,3]:  
              new_positions.add(pos)

        #reproduction
    for pos in all_nn: 
            #for a position which is a neighbour to a live cell, get the number of live neighbours and if equal 3,position becomes a live cell. 

            neighbours=get_neigh(pos)  
            live_neighbours=[n for n in neighbours if n in positions]#list of all live neighbours of a given cell  
            
            if len(live_neighbours)==3:
                new_positions.add(pos)  

    return new_positions


    
def main(): 
    
    running=True  
    play=False  
    step_mode=False
    
    fps=5
    positions=set()  

    patterns_position = {
        "Boat": {(1, 1), (1, 2), (2, 1), (2, 3), (3, 2)},
        "Pulsar": {
            (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
            (4, 2), (4, 7), (4, 9), (4, 14),
            (5, 2), (5, 7), (5, 9), (5, 14),
            (6, 2), (6, 7), (6, 9), (6, 14),
            (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
            (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
            (10, 2), (10, 7), (10, 9), (10, 14),
            (11, 2), (11, 7), (11, 9), (11, 14),
            (12, 2), (12, 7), (12, 9), (12, 14),
            (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)
        },
        "Glider": {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    }



    while running:
        clock.tick(fps)  
        pygame.display.set_caption("Game of Life: Playing" if play else "Game of Life: Paused")

        for event in pygame.event.get(): 
            # quit game if window is closed
            if event.type == pygame.QUIT: 
                pygame.quit()
                return  
            
            elif event.type== pygame.KEYDOWN:  

                #pause if space is pressed
                if event.key==pygame.K_SPACE: 
                    play= not play   
 
                #clear grid if z is pressed
                elif event.key == pygame.K_z:
                    positions = set()
                    play = False
                    
                #generates random positions if r is pressed  
                elif event.key == pygame.K_r: 
                    def gen(num):
                        return set([(random.randrange(0, grid_height), random.randrange(0, grid_width)) for _ in range(num)])
                    positions = gen(random.randrange(4, 10) * grid_width) 
                
                #press enter to toggle between step mode and continuous simulation
                elif event.key == pygame.K_RETURN:
                    step_mode = not step_mode
                    play=not step_mode 
  
                 #right arrow to view simulation step by step
                elif event.key==pygame.K_RIGHT and step_mode: 
                    positions=next_gen(positions)

                elif event.key == pygame.K_UP and not step_mode:
                    fps += 1  # increase FPS to speed up continuous simulation
                elif event.key == pygame.K_DOWN and not step_mode:
                    fps = max(1, fps - 1)  # decrease FPS to slow down continuous simulation 

                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]: 
                    patterns_name = {
                        pygame.K_1: "Boat",
                        pygame.K_2: "Pulsar",
                        pygame.K_3:'Glider'
                    } 
                    pattern= patterns_name.get(event.key) 
                    positions=patterns_position.get(pattern)
            

            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos() 
                col = pos[0]// tile_size
                row = pos[1] // tile_size
                pos = (col, row)  #gives u the row,col of the mouse click


                if pos in positions: #if already present then we remove existing tile
                    positions.remove(pos)
                else:
                    positions.add(pos)  

        if play and not step_mode:
            positions = next_gen(positions) 

        gameDisplay.fill(grey)  
        draw_grid(positions) 
        pygame.display.update() 

    pygame.quit()


if __name__ == '__main__':
    main()