import threading


class ABC(threading.Thread):

    def run(self):
        print("{} : Inside run".format(threading.currentThread().getName()))


def func(i):
    print("{} : I am #{}".format(threading.currentThread().getName(), i))


threadList = []
if __name__ == "__main__":
    # for i in range(5):
    #     t = threading.Thread(name="MyThread_{}".format(i), target=func, args=(i,))
    #     threadList.append(t)
    #     t.start()
    # print(threadList)

    for i in range(5):
        t = ABC()
        t.start()