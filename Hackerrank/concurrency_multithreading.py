import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")


"""Run Sequentially"""
start_time = time.time()

eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
print("total time required in sequential run: ", time.time() - start_time)


"""Run concurrently"""
start_time = time.time()

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# thread synchronization - main thread will wait for the following threads to synchronize and join
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
print("total time required in concurrent run: ", time.time() - start_time)