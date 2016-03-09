import threading
import time

class XinThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        self.create_time = time.time()

    def run(self):
        time.sleep(1)
        print("Thread", self.num, "created")
        print(time.time() - self.create_time)
        print("Thread", self.num, "terminated")

for item in range(7):
    t = XinThread(item)
    t.start()
