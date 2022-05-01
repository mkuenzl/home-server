import subprocess
from datetime import datetime
import json
#https://phoenixnap.com/kb/linux-commands-check-memory-usage
#https://www.baeldung.com/linux/monitor-disk-io
#https://www.elektronik-kompendium.de/sites/raspberry-pi/1911241.htm#:~:text=Prozessor%2DAuslastung&text=Die%20aktuelle%20Gesamtauslastung%20kann%20man,die%20Liste%20nach%20der%20Speicherbelegung.

def process_information():
    proc = subprocess.check_output("ps axo pid,cpu,%cpu,%mem", shell=True)
    processData = proc.decode('UTF-8')
    processData = processData.splitlines()[1:]
    processCount = len(processData)
    processCpuPercentage = 0.0
    for data in processData:
        processCpuPercentage += float(data.split()[2])
    # print(f"process | count:{processCount}, percentage:{processCpuPercentage}")
    return {"process_count": processCount, "process_cpu_percentage": processCpuPercentage}
    

def memory_information():
    proc = subprocess.check_output("free", shell=True)
    memoryData = proc.decode('UTF-8')
    memoryData = memoryData.splitlines()[1]
    memoryData = memoryData.split()
    total = float(memoryData[1])/1000
    used = float(memoryData[2])/1000
    free = float(memoryData[3])/1000
    available = float(memoryData[6])/1000
    # print(f"memory | total:{total} used:{used} free:{free} available:{available}")
    return {"memory_total": total, "memory_used": used, "memory_free": free, "memory_available": available}
    

def ping_information():
    proc = subprocess.check_output("ping -c 4 www.stackoverflow.com | tail -1 | awk '{print $4}'", shell=True)
    pingData = proc.decode('UTF-8').split('/')
    min = pingData[0].strip()
    avg = pingData[1].strip()
    max = pingData[2].strip()
    deviation = pingData[3].strip()
    # print(f"ping | min:{min} avg:{avg} max:{max} dev:{deviation}")
    return {"ping_min": float(min), "ping_avg": float(avg), "ping_max": float(max), "ping_dev": float(deviation)}


def server_information():
    # Returns a datetime object containing the local date and time
    dateTime = datetime.now()
    serverName = subprocess.check_output("hostname").decode('UTF-8')
    serverName = serverName.strip()
    # print(f"server | date:{dateTime} name:{serverName}")
    return {"timestamp": dateTime.strftime("%Y-%m-%d %H:%M:%S"), "host": serverName}


def temperature_information():
    cpuTemp = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
    cpuTemp = float(cpuTemp) / 1000
    gpuTemp = subprocess.getoutput("vcgencmd measure_temp | sed \"s/[^0-9.]//g\"")
    # print(f"temperature | cpu:{cpuTemp} gpu:{gpuTemp}")
    return {"temp_cpu": cpuTemp, "temp_gpu": float(gpuTemp)}


def retrieve():
    stats_arr = {**memory_information(), 
        **server_information(), 
        **process_information(), 
        **ping_information(), 
        **temperature_information()}
    return stats_arr
    

if __name__ == '__main__':
    print(json.dumps([retrieve()], sort_keys=False, indent=4))