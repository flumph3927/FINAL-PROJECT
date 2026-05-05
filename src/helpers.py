#Functions that will help with the main code

import pygame

class Button:
    def __init__(self,width,height,color,hover_color,text,x,y):
        self.color = color
        self.hover_color = hover_color
        self.text = text
        # rectangle needed for collision detection
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.SysFont('Arial',30)

    def draw(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(screen,current_color,self.rect)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        # Check if the mouse click happened inside the button's rectangle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False