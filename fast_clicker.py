from random import choice
from time import time

import pygame

from settings import Settings
from sprites import Label
pygame.init()

class Game:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.running = True
        self.settings = Settings()
        self.scene = pygame.display.set_mode((self.settings.scr_width,
                                               self.settings.scr_height))
        pygame.display.set_caption(self.settings.game_name)
        self.scene.fill(self.settings.bg_color)
        self.rectangles = []
        self.create_rectangles()
        self.wait = 0
        self.active_rectangle = None
        self.timer_text = Label(xcord=10, ycord=10)
        self.score_text = Label(xcord=400, ycord=10)
        self.seconds = 0 
        self.score = 0
        self.start_time = time()
        
    def create_rectangles(self):
        xcord = 50
        for i in range(self.settings.amount_rects):
            rectangle = Label(xcord=xcord)
            rectangle.set_text(self.settings.click_text, 'black')
            self.rectangles.append(rectangle)
            xcord += 110

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.check_collisions(event)

    def check_collisions(self, event):
        x, y = event.pos
        if self.active_rectangle.collide_point(x, y):
            self.active_rectangle.color = 'green'
            self.score += 1
        else:
            for i in range(4):
                if self.rectangles[i].collide_point(x, y):
                    self.rectangles[i].color = 'red'
    
    def run(self):
        while self.running:
            self.handle_events()
            self.scene.fill(self.settings.bg_color)
            for rectangle in self.rectangles:
                rectangle.draw_rect(self.scene)
                rectangle.draw_borders(self.scene, color='black')
            if self.wait == 0:
                self.active_rectangle = choice(self.rectangles)
                self.active_rectangle.add_text(self.scene)
                self.wait = 20
            else:
                self.wait -= 1
                if self.active_rectangle:
                    self.active_rectangle.add_text(self.scene)
                    for rectangle in self.rectangles:
                        rectangle.color = 'yellow'
            self.timer_text.set_text(f'Таймер:{self.seconds}')
            self.timer_text.add_text(self.scene)
            if time() - self.start_time > 1:
                self.seconds += 1
                self.start_time = time()
            self.score_text.set_text(f'Очки:{self.score}')
            self.score_text.add_text(self.scene)
            self.clock.tick(self.settings.fps)
            pygame.display.update()
            
if __name__ == "__main__":
    game = Game()
    game.run()

