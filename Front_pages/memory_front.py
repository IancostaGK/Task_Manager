import pygame, App, ferramentas
from Dados_pages import memory

def memory_page():
    lista_memory = memory.memory()
    lista_memory = lista_memory.retornar_dados()

    memory_bar_page = pygame.Rect(450, App.altura_tela - 50 - (lista_memory[0]*5), 50, lista_memory[0]*5)

    ferramentas.CriarRect(440, 40, 70, 520, App.black).desenha_rect()
    ferramentas.CriarRect(450, 50, 50, 500, App.green_bars).desenha_rect()
    pygame.draw.rect(App.screen, App.red, memory_bar_page)
    ferramentas.CriarTexto("MEMORY", 50, 5, 7, App.green_bars).escrever()
    ferramentas.desenha_seta()
    ferramentas.CriarTexto(f"{lista_memory[0]}%", 50, 445, 10, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Free: {lista_memory[2]/(1024*1024*1024):.2f} GB", 50, 100, 200, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Used: {lista_memory[1]/(1024*1024*1024):.2f} GB", 50, 100, 250, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Total: {lista_memory[3]/(1024*1024*1024):.2f} GB", 50, 100, 350, App.green_bars).escrever()