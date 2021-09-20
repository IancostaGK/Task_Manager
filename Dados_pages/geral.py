import psutil, pygame, App, ferramentas, socket

class menu():
    def __init__(self) -> None:
        pass
    
    def base_information():
        global cpu_bar, memory_bar, disk_bar
        
        cpu = psutil.cpu_percent(interval=1, percpu=False)
        cpu_bar = pygame.Rect(140, App.altura_tela - 100 - (cpu*5), 50, cpu*5)
        
        memory = psutil.virtual_memory()
        memory_percent = memory[2]
        memory_bar = pygame.Rect(255, App.altura_tela - 100 - (memory_percent*5), 50, memory_percent*5)
        
        disk_usage = psutil.disk_usage('.')
        disk_percent = disk_usage.percent
        disk_bar = pygame.Rect(375, App.altura_tela - 100 - (disk_percent*5), 50, disk_percent*5)
        
    def front_menu():
        porcentagem = 100 #inserir a porcentagem do lado esquerdo da tela
        App.screen.fill(App.bg_color)
            
        hostname = socket.gethostname()
        ipv4 = socket.gethostbyname(hostname)
        
        for i in range(5,App.largura_tela-100, 50): #inserir a porcentagem do lado esquerdo da tela
            ferramentas.CriarTexto(f'{porcentagem}%', 24, 5, i, App.green_bars).escrever()
            porcentagem -= 10

        for i in range(0,App.largura_tela-100, 50): #inserir as barras finas para medir a porcentagem
            bg_bars = pygame.Rect(50, i, App.largura_tela-140, 1)
            pygame.draw.rect(App.screen, App.green_bars, bg_bars)

        ferramentas.CriarRect(50, 0, 10,(App.altura_tela-100), App.green_bars).desenha_rect()
        ferramentas.CriarRect((App.largura_tela-100), 0, 10,(App.altura_tela-100), App.green_bars).desenha_rect()
        ferramentas.CriarRect(50, (App.altura_tela- 100), (App.largura_tela-140),10, App.green_bars).desenha_rect()
        ferramentas.CriarTexto("More info", 24, (App.largura_tela-83), 10, App.green_bars).escrever()         

        #inserir_att_App
            
        pygame.draw.rect(App.screen, App.green_bars, cpu_bar)
        ferramentas.CriarTexto("CPU", 24, 150, App.altura_tela-50, App.green_bars).escrever()

        pygame.draw.rect(App.screen, App.green_bars, memory_bar)
        ferramentas.CriarTexto("Memory", 24, 250, (App.altura_tela-50), App.green_bars).escrever()
        
        pygame.draw.rect(App.screen, App.green_bars, disk_bar)
        ferramentas.CriarTexto("Disk usage", 24, 360, (App.altura_tela-50), App.green_bars).escrever()

        ferramentas.CriarTexto(ipv4, 15, 10, (App.altura_tela-20), App.green_bars).escrever()
            
        #menu
        ferramentas.CriarTexto("C:", 40, (App.largura_tela-60), 65, App.green_bars).escrever()
        ferramentas.CriarTexto("Digite 'c'", 20, (App.largura_tela-78), 95, App.green_bars).escrever()
        ferramentas.CriarTexto("para + info", 20, (App.largura_tela-82), 107, App.green_bars).escrever()