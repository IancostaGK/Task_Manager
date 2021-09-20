import psutil

class disk():
    
    def __init__(self) -> None:
        disk_usage = psutil.disk_usage('.')
        self.disk_percent = disk_usage.percent
        self.disk_used = disk_usage.used
        self.disk_free = disk_usage.free
        self.disk_total = disk_usage.total
        
    def retornar_dados(self):
        dados = [self.disk_percent, self.disk_used, self.disk_free, self.disk_total]
        return(dados)