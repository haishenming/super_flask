import threading

def worker():
    print("i am thread")
    t = threading.currentThread()
    print(t.getName())

t = threading.currentThread()
print(t.getName())


new_t = threading.Thread(target=worker, name='new thread')
new_t.start()