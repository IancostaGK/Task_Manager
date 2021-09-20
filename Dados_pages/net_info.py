import psutil, time

class net_pacotes():
    
    def __init__(self) -> None:
        ip_data = psutil.net_io_counters(pernic=False, nowrap=True)
        self.ip_sent = ip_data[0]
        self.ip_receive = ip_data[1]
        
    def retornar_dados(self):
        time.sleep(1)

        ip_data = psutil.net_io_counters(pernic=False, nowrap=True)
        self.ip_sent = ip_data[0] - self.ip_sent
        self.ip_receive = ip_data[1] - self.ip_receive

        return self.ip_sent, self.ip_receive