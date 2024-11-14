import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_pos = (0,0)
        
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0]//32 == mole_pos[0] and pygame.mouse.get_pos()[1]//32 == mole_pos[1]:

                        mole_pos=(random.randrange(0,20), random.randrange(0,16))               
            screen.fill("light green")
            for i in range(20):
                    pygame.draw.line(screen, "black", (i*32,0),(i*32,512))
            for i in range(16):
                    pygame.draw.line(screen, "black", (0, i*32),(640,i*32))            
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos[0]*32, mole_pos[1]*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
