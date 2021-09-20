from Dados_pages import disk
import App, ferramentas, pygame

def disk_screen():
    
        lista_disk = disk.disk()
        lista_disk = lista_disk.retornar_dados()
        
        disk_bar_page = pygame.Rect(450, App.altura_tela - 50 - (lista_disk[0]*5), 50, lista_disk[0]*5)

        ferramentas.CriarRect(440, 40, 70, 520, App.black).desenha_rect()
        ferramentas.CriarRect(450, 50, 50, 500, App.green_bars).desenha_rect()
        pygame.draw.rect(App.screen, App.red, disk_bar_page)

        ferramentas.CriarTexto("DISK", 50, 5, 7, App.green_bars).escrever()
        ferramentas.desenha_seta()

        ferramentas.CriarTexto(f"{lista_disk[0]}%", 50, 445, 10, App.green_bars).escrever()
        ferramentas.CriarTexto(f"Free: {lista_disk[2]/(1024*1024*1024):.2f} GB", 50, 100, 200, App.green_bars).escrever()
        ferramentas.CriarTexto(f"Used: {lista_disk[1]/(1024*1024*1024):.2f} GB", 50, 100, 250, App.green_bars).escrever()
        ferramentas.CriarTexto(f"Total: {lista_disk[3]/(1024*1024*1024):.2f} GB", 50, 100, 350, App.green_bars).escrever()