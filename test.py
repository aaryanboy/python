import pygame
WIN=pygame.display.set_mode((300,300))

def main():
    run = True
    while run:
        print("Loop is running")  # Add this line for debugging
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False   
        WIN.fill((60,30,30))
        pygame.display.update()
         
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()