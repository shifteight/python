# Simulation of Hot Potato
# ------------------------
# Assume that the child holding the potato will be at the front of the queue.
# Upon passing the potato, the simulation will simply dequeue and then
# immediately enqueue that child, putting her at the end of the line.
# She will then wait until all the others have been at the front before
# it will be her turn again. After `num`` dequeue/enqueue operations,
# the child at the front will be removed permanently and another cycle
# will begin. This process will continue until only one name remains
# (the size of the queue is 1).

from queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
