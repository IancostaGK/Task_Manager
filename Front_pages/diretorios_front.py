import App, pygame, ferramentas, time
from Dados_pages import diretorios

def diretorios_screen():
    ini = time.time()
    
    dic = diretorios.diretorio()
    dic = dic.retornar_dados()

    titulo = '{:11}'.format("Tamanho")  # 10 caracteres + 1 de espaço
    titulo = titulo + '{:27}'.format("Data de Modificação")
    titulo = titulo + '{:27}'.format("Data de Criação")
    titulo = titulo + "Nome"
    
    y = 10
    ferramentas.CriarTexto(titulo, 24, 10, y, App.green_bars).escrever()

    for i in dic:
        kb = (dic[i][0])/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb)) + ' KB')

        ferramentas.CriarTexto(f"{tamanho}", 15, 12, y+28, App.green_bars).escrever()
        ferramentas.CriarTexto(f"{time.ctime(dic[i][2])}", 15, 120, y+28, App.green_bars).escrever()
        ferramentas.CriarTexto(f"{time.ctime(dic[i][1])}", 15, 290, y+28, App.green_bars).escrever()
        ferramentas.CriarTexto(f"{i}", 15, 450, y+28, App.green_bars).escrever()
        y += 15
        
    pygame.draw.rect(App.screen, App.green_bars, (90,0,5,App.altura_tela-75))
    pygame.draw.rect(App.screen, App.green_bars, (270,0,5,App.altura_tela-75))
    pygame.draw.rect(App.screen, App.green_bars, (430,0,5,App.altura_tela-75))
    pygame.draw.rect(App.screen, App.green_bars, (0,App.altura_tela-75, App.largura_tela,5))
    
    fim = time.time()  
    ferramentas.CriarTexto(f"Tempo de loading dos diretorios: {fim - ini} s", 20, (App.largura_tela/2 - 200), (App.altura_tela-20), App.green_bars).escrever()