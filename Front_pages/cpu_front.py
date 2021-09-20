import ferramentas, App, pygame, time
from Dados_pages import cpu_data

def cpu_screen():
    global lista_cpu

    lista_cpu = cpu_data.CPU.cpu_information()
    #return cpu ,processador, arquitetura, processadores_logicos, qtd_nucleos, freq_total, arquitetura_arch   
    
    cpu_bar_page = pygame.Rect(450, App.altura_tela - 50 - (lista_cpu[0]*5), 50, lista_cpu[0]*5)
    
    ferramentas.CriarRect(65, 65, 320, 420, App.black).desenha_rect()    
    ferramentas.CriarRect(75, 75, 300, 400, App.green_bars).desenha_rect()
    pygame.draw.line(App.screen, App.black, (65, 275), (380, 275), 5) #divisao pela metade do fundo dos nucleos
    desenha_nucleos()
    for x in range(105, 125 + (30*8) + 1, 30): #linhas verticais para dividir os nucleos
        pygame.draw.line(App.screen, App.black, (x, 65), (x, 475), 3)
    
    ferramentas.CriarRect(440, 40, 70, 520, App.black).desenha_rect()
    ferramentas.CriarRect(450, 50, 50, 500, App.green_bars).desenha_rect()
    pygame.draw.rect(App.screen, App.red, cpu_bar_page)
    ferramentas.CriarTexto("Uso de CPU por nucleo: ", 24, 75, 50, App.green_bars).escrever()
    ferramentas.CriarTexto(f"{lista_cpu[0]}%", 50, 445, 10, App.green_bars).escrever()
    ferramentas.CriarTexto(f"processador: {lista_cpu[1]}", 20, 20, 500, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Arquitetura: {lista_cpu[7]}, {lista_cpu[2]} (bits)", 20, 20, 520, App.green_bars).escrever()       
    ferramentas.CriarTexto(f"Processadores logicos: {lista_cpu[3]}", 20, 20, 540, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Nucleos: {lista_cpu[4]} ", 20, 20, 560, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Velocidade base: {(lista_cpu[5]/1000):.3f} Ghz", 20, 20, 580, App.green_bars).escrever()
    ferramentas.CriarTexto(f"Velocidade: {(lista_cpu[6]/1000):.3f} Ghz", 24, 220, 550, App.green_bars).escrever()
    ferramentas.CriarTexto(f"{time.ctime()} | chamada: {time.time():.2f}, clock da CPU: {time.process_time():.2f}", 15, 220, 580, App.green_bars).escrever()
    ferramentas.CriarTexto("CPU", 50, 5, 7, App.green_bars).escrever()
    ferramentas.desenha_seta()

def desenha_nucleos():
    #lista_qtd_nucleos = cpu_data.CPU.cpu_information()[8]
    x_nucleo = 75
    nucleos_counter = 1
    for nucleo in lista_cpu[8]:
        if nucleos_counter > 10:
            y_nucleo = 475 - (nucleo*(1.5))
        else:   
            y_nucleo = 275 - (nucleo*(1.5))
        nucleos_counter +=1
        nucleo = pygame.Rect(x_nucleo, y_nucleo, 30, (nucleo*(1.5)))
        pygame.draw.rect(App.screen, App.red, nucleo)
        x_nucleo += 30
        if x_nucleo >= 375:
            x_nucleo = 75