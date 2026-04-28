#menus file, accessory to main function

import pygame

# Clayton Baird, Main Menu

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

# basic skeleton for main menu, still need to make

def main_menu():
    pygame.init()
    current_screen = pygame.display.set_mode((1000,1000))
    # bg_image = pygame.image.load("placeholder").convert
    # bg_image = pygame.transform.scale(bg_image, (1000, 1000))


    while True:
        current_screen.fill((255,255,255))

        
        quit_button = Button(400,100,(255,0,0),(0,255,0), "Quit Game",400,700) # still need to figure out what the x and y will be, as well as the colors
        demo_button = Button(400,100,(255,0,0),(0,255,0),"Try Demo",400,300)
        load_button = Button(400,100,(255,0,0),(0,255,0),"Load/Create Game",400,500)

        quit_button.draw(current_screen)
        demo_button.draw(current_screen)
        load_button.draw(current_screen)


        for event in pygame.event.get():
            quit_clicked = quit_button.is_clicked(event)
            if quit_clicked:
                return 1,"Quit"
            demo_clicked = demo_button.is_clicked(event)
            if demo_clicked:
                print("Demo")
                pass
            load_clicked = load_button.is_clicked(event)
            if load_clicked:
                while True:
                    # clear other buttons
                    current_screen.fill((255,255,255))
                    return_button = Button(400,100,(255,0,0),(0,255,0),"Return to Main Menu",400,700)
                    save_one = Button(400,100,(255,0,0),(0,255,0),"Load Save File One",400,100)
                    save_two = Button(400,100,(255,0,0),(0,255,0),"Load Save File Two",400,300)
                    save_three = Button(400,100,(255,0,0),(0,255,0),"Load Save File Three",400,500)

                    return_button.draw(current_screen)
                    save_one.draw(current_screen)
                    save_two.draw(current_screen)
                    save_three.draw(current_screen)

                    return_clicked = return_button.is_clicked(event)
                    if return_clicked:
                        break

                    one_clicked = save_one.is_clicked(event)
                    if one_clicked:
                        return 2,"One"

                    two_clicked = save_two.is_clicked(event)
                    if two_clicked:
                        return 2,"Two"

                    three_clicked = save_three.is_clicked(event)
                    if three_clicked:
                        return 2,"Three"
                    
                    pygame.display.flip()
                    
        
        pygame.display.flip()



main_menu()
    # if quit button is pressed, just kill loop
    # if demo button is pressed, run run_generation function, set demo_run to true to it kicks user back to main menu once run ends
    # if load button is pressed, open load menu (gives user options for 3 different save files)


