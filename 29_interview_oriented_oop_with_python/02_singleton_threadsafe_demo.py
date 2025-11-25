import threading


class ThreadSafeSingletonDemo():
    _instance = None
    _lock = threading.Lock

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock():
                if cls._instance is None:
                    cls._instance = super(
                        ThreadSafeSingletonDemo, cls
                    ).__new__(cls)

        return cls._instance


def create():
    cur_instance = ThreadSafeSingletonDemo()
    print(threading.current_thread().name, id(cur_instance))


threads_list = []
for idx in range(5):
    cur_thread = threading.Thread(target=create, name=idx+1)
    threads_list.append(cur_thread)
    cur_thread.start()

for cur_thread in threads_list:
    cur_thread.join()
