import pygame
import sys

pygame.init()

class game():
    width = 1000
    height = 600
    exit_game = False
    def __init__(self):
        self.display = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("White Board")
        self.clock = pygame.time.Clock()
        self.fps = 40
        self.writing = False
        self.text = []
        self.color = "black"
        self.size = 5
        self.rubberactivate = False
        self.maxsize = 15
        self.minsize = 2

    def gameloop(self):
        display = self.display
        while not self.exit_game:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()

                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.writing = True

                if e.type == pygame.MOUSEBUTTONUP:
                    self.writing = False

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_g:
                        self.color = "green"
                    
                    if e.key == pygame.K_b:
                        self.color = "black"

                    if e.key == pygame.K_p:
                        self.color = "purple"
                    
                    if e.key == pygame.K_y:
                        self.color = "yellow"

                    if e.key == pygame.K_c:
                        self.text.clear()
                    
                    if e.key == pygame.K_a:
                        if self.size<self.maxsize:
                            self.size+=1
                            
                    if e.key == pygame.K_d:
                        if self.size>self.minsize:
                            self.size-=1

                    if e.key == pygame.K_r:
                        if self.rubberactivate:
                            self.rubberactivate=False
                        else:
                            self.rubberactivate=True
                
                    
            display.fill("white")
            
            for x,y,color,size in self.text:
                pygame.draw.circle(display,color,(x,y),size)

            # creating the eraser here
            if self.rubberactivate:
                pygame.draw.rect(display,(225, 217, 209),((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]), (100,50)))

            if not self.rubberactivate:
                if self.writing:
                    self.text.append([pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],self.color,self.size])
            if self.rubberactivate:
                if self.writing:
                    length = len(self.text)
                    removingarr = []
                    for i in range(length):
                        try:
                            if self.text[i][0]>pygame.mouse.get_pos()[0] and self.text[i][0]<pygame.mouse.get_pos()[0]+110 and self.text[i][1]>pygame.mouse.get_pos()[1]-2 and self.text[i][1]<pygame.mouse.get_pos()[1]+60:
                                if self.text.__contains__(self.text[i]):
                                    removingarr.append(self.text[i])
                        except Exception as e:
                            break
                    
                    for i in range(len(removingarr)):
                        self.text.remove(removingarr[i])

                    # if len(self.text)==1:
                    #     self.text.clear()
                    
                            
            
            pygame.display.update()

            self.clock.tick(100)
    

game = game()
game.gameloop()
