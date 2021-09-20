import psutil, cpuinfo

class CPU:
    
    def __init__(self, cpu):
        self.cpu = cpu
    
    def cpu_information():
        nucleos = psutil.cpu_percent(percpu=True)
        cpu = psutil.cpu_percent(percpu=False)
        freq = psutil.cpu_freq(percpu=False)
        freq_atual = freq[0]
        info = cpuinfo.get_cpu_info()
        processadores_logicos = info['count']
        qtd_nucleos = psutil.cpu_count(logical=False)
        processador = info['brand_raw']
        arquitetura = info['bits']
        arquitetura_arch = info['arch']
        freq_total = freq[2]
        
        return cpu ,processador, arquitetura, processadores_logicos, qtd_nucleos, freq_total, freq_atual, arquitetura_arch, nucleos