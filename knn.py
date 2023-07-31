import time

while True:

    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time, end="\r")
    time.sleep(1)
