# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/12 22:30'
"""
主要模拟步骤
1. 创建打印任务的队列，每个任务都有个时间戳。队列启动的时候为空。
2. 每秒（currentSecond）：
    是否创建新的打印任务？如果是，将 currentSecond 作为时间戳添加到队列。
    如果打印机不忙并且有任务在等待
    从打印机队列中删除一个任务并将其分配给打印机
    从 currentSecond 中减去时间戳，以计算该任务的等待时间。
    将该任务的等待时间附件到列表中稍后处理。
    根据打印任务的页数，确定需要多少时间。
    打印机需要一秒打印，所以得从该任务的所需的等待时间减去一秒。
    如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲。
3. 模拟完成后，从生成的等待时间列表中计算平均等待时间。
"""
import random
from base.queue import Queue


class Printer:

    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.get_pages() * 60/self.pagerate


class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if new_print_task():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.wait_time(currentSecond))
            labprinter.start_next(nexttask)

        labprinter.tick()

    average_wait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, printQueue.size()))


def new_print_task():
    num = random.randrange(1, 181)

    return num == 180


for i in range(10):
    simulation(3600, 5)