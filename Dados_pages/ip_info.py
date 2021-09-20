import nmap, wmi, psutil, ferramentas, App

def scan_host(host):
    global peguei_dados_rede, nm

    nm = nmap.PortScanner()
    nm.scan(host)
    
    peguei_dados_rede = True 

def scan_blit(host):
    ferramentas.CriarTexto("Dados de rede", 50, 10, 10, App.green_bars).escrever()
        
    y = 400       
    ferramentas.CriarTexto((f"Dados de portas do ip: {host}"), 24, 20, 350, App.green_bars).escrever()     
    
    for proto in nm[host].all_protocols():

        ferramentas.CriarTexto(('Protocolo : %s' % proto), 24, 20, 370, App.green_bars).escrever()        
        lport = nm[host][proto].keys()
        
        for port in lport:
            ferramentas.CriarTexto(('Porta: %s     -    Estado: %s' % (port, nm[host][proto][port]['state'])), 24, 20, y, App.green_bars).escrever()
            y += 20
            
def ip_more_data():
    
    wmi_obj = wmi.WMI()
    wmi_sql = "select IPSubnet,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
    wmi_out = wmi_obj.query( wmi_sql )

    for dev in wmi_out:
        ferramentas.CriarTexto((f"Máscara de sub-rede: {dev.IPSubnet[0]}"), 24, 20, 70, App.green_bars).escrever()     
        ferramentas.CriarTexto((f"Gateway padrão:  {dev.DefaultIPGateway[0]}"), 24, 20, 90, App.green_bars).escrever()     
        
    y = 140

    dados_net_interface = psutil.net_io_counters(pernic=True)
    #print(f"{i}: Pacotes enviados: {(dados_net_interface[i][0]/1024):.2f}Kbps, Pacotes recebidos:  {(dados_net_interface[i][1]/1024):.2f}Kbps")
    
    for i in dados_net_interface:
        ferramentas.CriarTexto((f"{i}: Pacotes enviados: {(dados_net_interface[i][0]/(1024*1024)):.2f}Mbps, Pacotes recebidos:  {(dados_net_interface[i][1]/(1024*1024)):.2f}Mbps"), 20, 20, y, App.green_bars).escrever()  
        y += 14