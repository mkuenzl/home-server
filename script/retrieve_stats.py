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
    return {"processCount": processCount, "processCpuPercentage": processCpuPercentage}
    

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
    return {"memoryTotal": total, "memoryUsed": used, "memoryFree": free, "memoryAvailable": available}
    

def ping_information():
    proc = subprocess.check_output("ping -c 4 www.stackoverflow.com | tail -1 | awk '{print $4}'", shell=True)
    pingData = proc.decode('UTF-8').split('/')
    min = pingData[0].strip()
    avg = pingData[1].strip()
    max = pingData[2].strip()
    deviation = pingData[3].strip()
    # print(f"ping | min:{min} avg:{avg} max:{max} dev:{deviation}")
    return {"pingMin": float(min), "pingAvg": float(avg), "pingMax": float(max), "pingDeviation": float(deviation)}


def server_information():
    # Returns a datetime object containing the local date and time
    dateTime = datetime.now()
    serverName = subprocess.check_output("hostname").decode('UTF-8')
    serverName = serverName.strip()
    # print(f"server | date:{dateTime} name:{serverName}")
    return {"dateTime": dateTime.strftime("%Y-%m-%d %H:%M:%S"), "serverName": serverName}


def temperature_information():
    cpuTemp = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
    cpuTemp = float(cpuTemp) / 1000
    gpuTemp = subprocess.getoutput("vcgencmd measure_temp | sed \"s/[^0-9.]//g\"")
    # print(f"temperature | cpu:{cpuTemp} gpu:{gpuTemp}")
    return {"tempCpu": cpuTemp, "tempGpu": float(gpuTemp)}
    

if __name__ == '__main__':
    stats_arr = {**memory_information(), 
        **server_information(), 
        **process_information(), 
        **ping_information(), 
        **temperature_information()}
    print(json.dumps([stats_arr], sort_keys=False, indent=4))