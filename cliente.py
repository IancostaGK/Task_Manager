import socket, pickle, ferramentas, App, pygame, sys

def main():
    pygame.init()
    App.screen.fill(App.bg_color)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                s.close()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                requisicao()           
        
        ferramentas.CriarTexto("Aperte qualquer tecla para verificar status do servidor...", 25, 15, 15, App.green_bars).escrever()
        pygame.display.update()
            

def requisicao():
    
    try:
        y = 70
        s.connect((socket.gethostname(), 8999))
        msg = ' '
        ferramentas.CriarTexto('%CPU', 25, 15, 40, App.green_bars).escrever()
        ferramentas.CriarTexto('%MEM', 25, 75, 40, App.green_bars).escrever()
        ferramentas.CriarTexto('%DISK', 25, 140, 40, App.green_bars).escrever()
        ferramentas.CriarTexto('Pacotes Enviados(Kbps)', 22, 210, 43, App.green_bars).escrever()
        ferramentas.CriarTexto('Pacotes Recebidos(Kbps)', 22, 400, 43, App.green_bars).escrever()
        
        for i in range(25):
            
            s.send(msg.encode('ascii'))
            bytes = s.recv(1024)
            lista = pickle.loads(bytes)
            
            ferramentas.CriarTexto(f"{lista[0]:.1f}", 20, 22, y, App.green_bars).escrever()
            ferramentas.CriarTexto(f"{lista[1]:.1f}", 20, 82, y, App.green_bars).escrever()
            ferramentas.CriarTexto(f"{lista[2]:.1f}", 20, 147, y, App.green_bars).escrever()
            ferramentas.CriarTexto(f"{lista[3]:.2f}", 20, 280, y, App.green_bars).escrever()
            ferramentas.CriarTexto(f"{lista[4]:.2f}", 20, 470, y, App.green_bars).escrever()
            
            y += 20
            
            pygame.display.update()
            App.clock.tick(60)
            
        msg = 'fim'
        s.send(msg.encode('ascii'))
    except Exception as erro:
        print(str(erro))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main()