import socket
import pickle
from Dados_pages import cpu_data, disk, memory, net_info

class App:

    def __init__(self):
        self.socket_servidor = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.porta = 8999
        self.resposta = []
        self.socket_servidor.bind((self.host, self.porta))
        self.socket_servidor.listen()
        print("Servidor de nome", self.host,"esperando conexão na porta", self.porta)
        (self.socket_cliente, addr) = self.socket_servidor.accept()
        print("Conectado a:", str(addr))

        App.running = True

    def run(self):
        while App.running:
            msg = self.socket_cliente.recv(4)
            if msg.decode('ascii') == 'fim':
                break
            
            self.resposta.clear()
            self.resposta = self.obtem_dados()
            bytes_resp = pickle.dumps(self.resposta)
            self.socket_cliente.send(bytes_resp)

        self.socket_cliente.close()
        self.socket_servidor.close()

    def obtem_dados(self):
        data_cpu = cpu_data.CPU.cpu_information()
        
        data_mem = memory.memory()
        data_mem = data_mem.retornar_dados()
        
        data_disk = disk.disk()
        data_disk = data_disk.retornar_dados()
        
        net_data = net_info.net_pacotes()
        net_data = net_data.retornar_dados()
        
        self.resposta.append(data_cpu[0])
        self.resposta.append(data_mem[0])
        self.resposta.append(data_disk[0])
        self.resposta.append(net_data[0]/1024)
        self.resposta.append(net_data[1]/1024)

        return self.resposta

if __name__ == '__main__':
    App().run()