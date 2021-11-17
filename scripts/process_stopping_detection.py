import time
import signal

s = 0
def handler(signum, frame):
    print("Process stopped for " + str(int(s)) + " seconds")
    exit(0)

signal.signal(signal.SIGINT, handler)
lastt = time.localtime()
while True:
    time.sleep(1)
    timediff = int(time.mktime(time.localtime()) - time.mktime(lastt))
    if timediff > 1:
        print("Detected stop: " + time.strftime("%H:%M:%S", lastt) + " -> " + time.strftime("%H:%M:%S", time.localtime()))
        s += timediff
    lastt = time.localtime()