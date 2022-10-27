import pygame  
pygame.init()  
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = (130,50,200)
color_light = (170,170,170)
color_dark = (100,100,100)
# assigning values to height and width variable   

screen_resolution=(326,422)

# creating the display surface object   
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode(screen_resolution)  
width = display_surface.get_width()
height = display_surface.get_height()
# set the pygame window name   
pygame.display.set_caption('Pedo-Window')  
  
# creating a surface object, image is drawn on it.   
# infinite loop   
while True:  
    display_surface.fill(WHITE)  
    display_surface.blit(image, (0, 0))  
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()

        
    # Draws the surface object to the screen.   
        
