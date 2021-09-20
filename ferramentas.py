import pygame, App

class CriarTexto():
    def __init__(self, text, font_size, pos_x, pos_y, color):
        self.text = text
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        
    def escrever(self):
        fonte = pygame.font.Font(None, self.font_size)
        
        create_text = fonte.render(self.text, 1, self.color)
        App.screen.blit(create_text, (self.pos_x, self.pos_y))
        
class CriarRect():
    def __init__(self, x, y, pos_x, pos_y, color):
        self.largura = x
        self.altura = y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        
    def desenha_rect(self):
        rect = pygame.Rect(self.largura, self.altura, self.pos_x, self.pos_y)
        pygame.draw.rect(App.screen, self.color, rect)
        
def loading():
    App.screen.fill(App.bg_color)
    CriarTexto("Loading...", 50, (App.largura_tela/2 - 90), (App.altura_tela/2 -20), App.green_bars).escrever()
    pygame.display.update() 

def desenha_seta():
    pygame.draw.line(App.screen, App.green_bars, (560, App.altura_tela-30), (575, App.altura_tela-40), 3)
    pygame.draw.line(App.screen, App.green_bars, (560, App.altura_tela-50), (575, App.altura_tela-40), 3)
    pygame.draw.line(App.screen, App.green_bars, (550, App.altura_tela-30), (535, App.altura_tela-40), 3)
    pygame.draw.line(App.screen, App.green_bars, (550, App.altura_tela-50), (535, App.altura_tela-40), 3)