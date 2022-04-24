import subprocess


def pingAddress():
    proc = subprocess.check_output("ping -c 4 www.stackoverflow.com | tail -1 | awk '{print $4}'", shell=True)
    ping_information = proc.decode('UTF-8').split('/')
    min = ping_information[0]
    avg = ping_information[1]
    max = ping_information[2]
    deviation = ping_information[3]

    print(f"pint output: {min}, {avg}, {max}, {deviation}")


if __name__ == '__main__':
    pingAddress()

