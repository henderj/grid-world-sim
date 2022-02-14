from cProfile import run
import pygame as py

WIDTH, HEIGHT = (640, 480)

def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    
    running = True

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                break
            else:
                print(event)
        
        screen.fill((120,120,120))
        py.display.flip()
    
    py.quit()
            

if __name__ == "__main__":
    main()