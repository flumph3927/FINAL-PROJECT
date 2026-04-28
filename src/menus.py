#menus file, accessory to main function

import pygame

# Clayton Baird, Main Menu

class Button:
    def __init__(self,width,height,color,hover_color,text,x,y):
        self.color = color
        self.hover_color = color
        self.text = text
        # rectangle needed for collision detection
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.SysFont('Arial',30)

    def draw(self,screen):
        mouse_pos = pygame.get.mouse_pos()
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

def main_menu(screen):

    current_screen = screen
    while True:
        quit_button = Button(100,400, "Quit Game") # still need to figure out what the x and y will be, as well as the color
        demo_button = Button(100,400,"Try Demo")
        load_button = Button(100,400,"Load/Create Game")

        quit_button.draw(current_screen)
        demo_button.draw(current_screen)
        load_button.draw(current_screen)

        quit_clicked = quit_button.is_clicked()
        if quit_clicked:
            return "Quit"

        demo_clicked = demo_button.is_clicked()
        if demo_clicked:
            return "Demo"

        load_clicked = load_button.is_clicked()
        if load_clicked:
            while True:
                # clear other buttons
                return_button = Button(100,400,"Return to Main Menu")
                save_one = Button(100,400,"Load Save File One")
                save_two = Button(100,400,"Load Save File Two")
                save_three = Button(100,400,"Load Save File Three")

                return_button.draw(current_screen)
                save_one.draw(current_screen)
                save_two.draw(current_screen)
                save_three.draw(current_screen)

                return_clicked = return_button.is_clicked()
                if return_clicked:
                    break

                one_clicked = save_one.is_clicked()
                if one_clicked:
                    return "One"

                two_clicked = save_two.is_clicked()
                if two_clicked:
                    return "Two"

                three_clicked = save_three.is_clicked()
                if three_clicked:
                    return "Three"



    # if quit button is pressed, just kill loop
    # if demo button is pressed, run run_generation function, set demo_run to true to it kicks user back to main menu once run ends
    # if load button is pressed, open load menu (gives user options for 3 different save files)


