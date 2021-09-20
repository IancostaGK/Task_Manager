import psutil

class memory():
    
    def __init__(self) -> None:
        memory = psutil.virtual_memory()
        self.memory_percent = memory[2]
        self.memory_used = memory[3]
        self.memory_free = memory[1]
        self.memory_total = memory[0]
        
    def retornar_dados(self):
        dados = [self.memory_percent, self.memory_used, self.memory_free, self.memory_total]
        return(dados)