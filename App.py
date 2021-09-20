import pygame, sys, ferramentas, time, sched, socket
from Dados_pages import geral, ip_info
from Front_pages import cpu_front, disk_front, memory_front, net_infot_front, diretorios_front
        
def main():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        telas()
    
def telas():
    menu = True
    cpu_tela = memory_tela = disk_tela = ip_tela = diretorios_tela = ip_tela2 = False
    
    while True:
        while menu:
            screen.fill(bg_color)
            geral.menu.base_information()
            geral.menu.front_menu()           
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        menu = False
                        cpu_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_LEFT:
                        ip_tela = True
                        menu = False
                        ferramentas.loading()
                    if event.key == pygame.K_c:
                        diretorios_tela = True
                        menu = False
                        ferramentas.loading()
                        
            pygame.display.update()
            clock.tick(60) 

        while cpu_tela:
            screen.fill(bg_color)
            cpu_front.cpu_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        cpu_tela = False
                        memory_tela = True
                        ferramentas.loading() 
                    if event.key == pygame.K_LEFT:
                        menu = True
                        cpu_tela = False
                        ferramentas.loading() 
                    if event.key == pygame.K_SPACE:
                        cpu_tela = False
                        menu = True
                        ferramentas.loading() 
            
            pygame.display.update()
            clock.tick(60) 

        while memory_tela:
            screen.fill(bg_color)
            memory_front.memory_page()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        memory_tela = False
                        disk_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_LEFT:
                        memory_tela = False
                        cpu_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_SPACE:
                        memory_tela = False
                        menu = True
                        ferramentas.loading()
                        
            pygame.display.update()
            clock.tick(60)

        while disk_tela:
            screen.fill(bg_color)
            disk_front.disk_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        disk_tela = False
                        ip_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_LEFT:
                        disk_tela = False
                        memory_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_SPACE:
                        disk_tela = False
                        menu = True
                        ferramentas.loading()
            
            pygame.display.update()
            clock.tick(60)  
            
        while ip_tela:
            screen.fill(bg_color)
            net_infot_front.ip.ip_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ip_tela = False
                        menu = True
                        ferramentas.loading()
                    if event.key == pygame.K_LEFT:
                        ip_tela = False
                        memory_tela = True
                        ferramentas.loading()
                    if event.key == pygame.K_SPACE:
                        ip_tela = False
                        menu = True
                        ferramentas.loading()
                    if event.key == pygame.K_p:
                        ip_tela2 = True
                        ip_tela = False
                        ferramentas.loading()        
                        
            pygame.display.update()
            clock.tick(60)
            
        ferramentas.loading()

        while ip_tela2:
            screen.fill(bg_color)
            ip_info.scan_host(ipv4)
            ip_info.scan_blit(ipv4)
            ip_info.ip_more_data()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ip_tela2 = False
                        ip_tela = True
                        ferramentas.loading()        
                        
            pygame.display.update()
            clock.tick(60) 
                
        while diretorios_tela:
            screen.fill(bg_color)
            scheduler.enter(0, 0, diretorios_front.diretorios_screen)
            scheduler.run()      
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        diretorios_tela = False
                        menu = True
                        ferramentas.loading()
                        
            pygame.display.update()
            clock.tick(60)

# cores
green_bars = (50,205,50)
bg_color = (30,30,30)
botao_color = (0,50,0)
red = (255, 0, 0)
black = (0,0,0)
largura_tela = 600
altura_tela = 600

#screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((largura_tela,altura_tela))

#dados 
scheduler = sched.scheduler(time.time, time.sleep)
hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname) 

if __name__ == "__main__":
    logo = pygame.image.load('imagens\\logo.png')
    pygame.display.set_caption('Task Manager')
    pygame.display.set_icon(logo)
    pygame.init()
    main()