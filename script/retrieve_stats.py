import subprocess
#https://phoenixnap.com/kb/linux-commands-check-memory-usage
#https://www.baeldung.com/linux/monitor-disk-io
#https://www.elektronik-kompendium.de/sites/raspberry-pi/1911241.htm#:~:text=Prozessor%2DAuslastung&text=Die%20aktuelle%20Gesamtauslastung%20kann%20man,die%20Liste%20nach%20der%20Speicherbelegung.

def process_information():
    proc = subprocess.check_output("ps axo pid,cpu,%cpu,%mem", shell=True)
    process_data = proc.decode('UTF-8')
    print(process_data)


def ping_information():
    proc = subprocess.check_output("ping -c 4 www.stackoverflow.com | tail -1 | awk '{print $4}'", shell=True)
    ping_data = proc.decode('UTF-8').split('/')
    min = ping_data[0]
    avg = ping_data[1]
    max = ping_data[2]
    deviation = ping_data[3]

    print(f"pint output: {min}, {avg}, {max}, {deviation}")


if __name__ == '__main__':
    ping_information()
    process_information()

