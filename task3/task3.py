import psutil
import time
import json
import argparse


class task3:
    def __init__(self, t):
        self.t = t

    def txt(self):
        outfile: str = "task3.txt"
        count = 0
        while True:
            count = count + 1
            ln = str(count)
            l0 = str(time.asctime())
            l1 = str(psutil.cpu_times()[2])
            l2 = str(psutil.disk_usage('/')[1])
            l3 = str(psutil.virtual_memory()[3])
            ar_txt = "SNAPSHOT:" + ln + " Date:" + l0 + " SysCPU:" + l1 + " Mem:" + l2 + " VMem:" + l3
            with open(outfile, "a") as file:
                file.write(ar_txt + "\n")
            file.close()
            time.sleep(int(self.t))

    def json(self):
        outfile = 'task3.json'
        count = 0
        while True:
            count = count + 1
            l1 = psutil.cpu_times()
            l2 = psutil.disk_usage('/')
            l3 = psutil.virtual_memory()
            ar_json = {
                'SNAPSHOT': str(count),
                'Date': str(time.asctime()),
                'System CPU': str(l1[2]),
                'Memory': str(l2[1]),
                'Vmemory': str(l3[3])
            }
            with open(outfile, "a") as f_json:
                f_json.write(json.dumps(ar_json) + "\n")
            f_json.close()
            time.sleep(int(self.t))


parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()


def main():
    object_0 = task3(args.i)

    if args.t == "json":
        object_0.json()
    else:
        object_0.txt()


main()
