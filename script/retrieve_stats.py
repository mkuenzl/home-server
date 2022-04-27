import subprocess
from datetime import datetime
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
    print(f"print output: {processCount}, {processCpuPercentage}")
    

def memory_information():
    proc = subprocess.check_output("free -h", shell=True)
    memoryData = proc.decode('UTF-8')
    memoryData = memoryData.splitlines()[1]
    memoryData = memoryData.split()
    total = memoryData[1]
    used = memoryData[2]
    free = memoryData[3]
    available = memoryData[6]
    print(f"print output: {total}, {used}, {free}, {available}")

def ping_information():
    proc = subprocess.check_output("ping -c 4 www.stackoverflow.com | tail -1 | awk '{print $4}'", shell=True)
    pingData = proc.decode('UTF-8').split('/')
    min = pingData[0]
    avg = pingData[1]
    max = pingData[2]
    deviation = pingData[3]

    print(f"pint output: {min}, {avg}, {max}, {deviation}")


def server_information():
    # Returns a datetime object containing the local date and time
    dateTime = datetime.now()
    cpuTemp = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
    cpuTemp = float(cpuTemp) / 1000
    gpuTemp = subprocess.getoutput("vcgencmd measure_temp | sed \"s/[^0-9.]//g\"")
    serverName = subprocess.check_output("hostname").decode('UTF-8')


    print(f"pint output: {dateTime}, {cpuTemp}, {gpuTemp}, {serverName}")


if __name__ == '__main__':
    memory_information()
    server_information()
    process_information()
    ping_information()