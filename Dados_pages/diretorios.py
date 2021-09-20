import os

class diretorio():
    
    def __init__(self) -> None:
        self.path = r'C:\\'
        self.files = os.listdir(self.path)
        self.dic = {} 
        
    def retornar_dados(self):
        for i in self.files:
        
            if os.path.isdir(os.path.join(self.path, i)) or os.path.isfile(os.path.join(self.path, i)):
                self.dic[i] = []
                self.dic[i].append(os.stat(os.path.join(self.path, i)).st_size) # Tamanho
                self.dic[i].append(os.stat(os.path.join(self.path, i)).st_atime) # Tempo de criação
                self.dic[i].append(os.stat(os.path.join(self.path, i)).st_mtime) # Tempo de modificação
                
        return self.dic