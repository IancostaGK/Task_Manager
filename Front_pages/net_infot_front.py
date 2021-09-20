import App, ferramentas, socket, pygame
from Dados_pages import net_info

class ip():
    def __init__(self) -> None:
        pass

    def ip_screen():
        hostname = socket.gethostname()
        ipv4 = socket.gethostbyname(hostname)
        ip = socket.gethostbyaddr(hostname)
        ipv6 = ip[2][0]
        
        pacotes = net_info.net_pacotes()
        pacotes = pacotes.retornar_dados()

        ip_sent_bar = pygame.Rect(100, 200, ((pacotes[0])/1024), 40)
        ip_receive_bar = pygame.Rect(100, 300, ((pacotes[1])/1024), 40)
        
        ferramentas.CriarRect(0, 100, 600, 350, App.black).desenha_rect()
        
        ferramentas.CriarTexto("ETHERNET", 50, 5, 7, App.green_bars).escrever()
        
        ferramentas.CriarTexto(f"Enviar: {((pacotes[0])/1024):.1f} Kbps", 50, 100, 150, App.green_bars).escrever()
        pygame.draw.rect(App.screen, App.green_bars, ip_sent_bar)
        ferramentas.CriarTexto(f"Receber: {((pacotes[1])/1024):.1f} Kbps", 50, 100, 250, App.green_bars).escrever()
        pygame.draw.rect(App.screen, App.green_bars, ip_receive_bar)
        
        ferramentas.CriarTexto(f"Endereço Ipv4: {ipv4}", 24, 100, 350, App.green_bars).escrever()
        ferramentas.CriarTexto(f"Endereço Ipv6: {ipv6}", 24, 100, 370, App.green_bars).escrever()

        ferramentas.CriarRect((App.largura_tela-100), 100, 100, 350, App.black).desenha_rect()       
        ferramentas.CriarTexto(f"Diigite 'p' para obter mais informações sobre seu IP e conexões" , 24, 57, (App.altura_tela-85), App.green_bars).escrever()
        ferramentas.desenha_seta() 