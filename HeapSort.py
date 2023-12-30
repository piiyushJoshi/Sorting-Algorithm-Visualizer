import time
 
def heapify(data, N, i,drawData,timeTick):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and data[largest] < data[l]:
        largest = l

    if r < N and data[largest] < data[r]:
        largest = r
 
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data)
        time.sleep(timeTick)
        heapify(data, N, largest,drawData,timeTick)
 
def heapSort(data,drawData,timeTick):
    N = len(data)
 
    for i in range(N//2 - 1, -1, -1):
        heapify(data, N, i,drawData,timeTick)
 
    for i in range(N-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawData(data)
        time.sleep(timeTick)
        heapify(data, i, 0,drawData,timeTick)