import pygame


class Area:
    def __init__(
            self, 
            width=80, 
            height=100, 
            color='yellow', 
            xcord=60, 
            ycord=200
            ) -> None:
        self.rect = pygame.Rect(xcord, ycord, width, height)
        self.color = color
        self.width = width
        self.height = height

    def draw_rect(self, scene):
        pygame.draw.rect(scene, self.color, self.rect)

    def draw_borders(self, scene, color):
        pygame.draw.rect(scene, color, self.rect, width=5)

    def collide_point(self, x, y):
        return self.rect.collidepoint(x, y)
    
class Label(Area):
    def set_text(self, text, text_color='black'):
        self.text_render = pygame.font.Font(None, 22).render(text,
                                                              True, text_color)
    
    def add_text(self, scene):
        scene.blit(self.text_render, (self.rect.x + self.width/4,
                                       self.rect.y + self.height/2))
        





