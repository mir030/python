import threading
import time


def func():
    print('ran')
    time.sleep(1)
    print('done')
    time.sleep(0.8)
    print("now done")


x = threading.Thread(target=func)
x.start()
print("Active thread count: ", threading.active_count())
time.sleep(1)
print("finally")
