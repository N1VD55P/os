#fcfs.py
n = int(input("Enter number of processes: "))

AT = list(map(int, input("Enter Arrival Times: ").split()))
BT = list(map(int, input("Enter Burst Times: ").split()))

CT = [0]*n
TAT = [0]*n
WT = [0]*n

CT[0] = AT[0] + BT[0]

for i in range(1, n):
    if AT[i] > CT[i-1]:
        CT[i] = AT[i] + BT[i]
    else:
        CT[i] = CT[i-1] + BT[i]

for i in range(n):
    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]

print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print("Average TAT:", sum(TAT)/n)
print("Average WT:", sum(WT)/n)

#SJF Non-Preemptive

n = int(input("Enter number of processes: "))

AT = list(map(int, input("Enter Arrival Times: ").split()))
BT = list(map(int, input("Enter Burst Times: ").split()))

completed = [False]*n
CT = [0]*n
TAT = [0]*n
WT = [0]*n

time = 0
count = 0

while count < n:
    idx = -1
    min_bt = 10**9

    for i in range(n):
        if AT[i] <= time and not completed[i]:
            if BT[i] < min_bt:
                min_bt = BT[i]
                idx = i

    if idx != -1:
        time += BT[idx]
        CT[idx] = time
        completed[idx] = True
        count += 1
    else:
        time += 1

for i in range(n):
    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]

print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print("Average TAT:", sum(TAT)/n)
print("Average WT:", sum(WT)/n)

#SJF Preemptive
n = int(input("Enter number of processes: "))

AT = list(map(int, input("Enter Arrival Times: ").split()))
BT = list(map(int, input("Enter Burst Times: ").split()))

remaining = BT[:]
CT = [0]*n

time = 0
completed = 0

while completed < n:
    idx = -1
    min_bt = 10**9

    for i in range(n):
        if AT[i] <= time and remaining[i] > 0:
            if remaining[i] < min_bt:
                min_bt = remaining[i]
                idx = i

    if idx != -1:
        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            CT[idx] = time
            completed += 1
    else:
        time += 1

TAT = [CT[i] - AT[i] for i in range(n)]
WT = [TAT[i] - BT[i] for i in range(n)]

print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print("Average TAT:", sum(TAT)/n)
print("Average WT:", sum(WT)/n)

# Priority Scheduling
n = int(input("Enter number of processes: "))

AT = list(map(int, input("Enter Arrival Times: ").split()))
BT = list(map(int, input("Enter Burst Times: ").split()))
P = list(map(int, input("Enter Priorities (lower = higher): ").split()))

completed = [False]*n
CT = [0]*n

time = 0
count = 0

while count < n:
    idx = -1
    highest = 10**9

    for i in range(n):
        if AT[i] <= time and not completed[i]:
            if P[i] < highest:
                highest = P[i]
                idx = i

    if idx != -1:
        time += BT[idx]
        CT[idx] = time
        completed[idx] = True
        count += 1
    else:
        time += 1

TAT = [CT[i] - AT[i] for i in range(n)]
WT = [TAT[i] - BT[i] for i in range(n)]

print("\nP\tAT\tBT\tP\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{AT[i]}\t{BT[i]}\t{P[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print("Average TAT:", sum(TAT)/n)
print("Average WT:", sum(WT)/n)

#Round Robin
from collections import deque

n = int(input("Enter number of processes: "))
AT = list(map(int, input("Enter Arrival Times: ").split()))
BT = list(map(int, input("Enter Burst Times: ").split()))

quantum = 3

remaining = BT[:]
CT = [0]*n
queue = deque()

time = 0
visited = [False]*n

while True:
    for i in range(n):
        if AT[i] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if not queue:
        if all(r == 0 for r in remaining):
            break
        time += 1
        continue

    i = queue.popleft()
    exec_time = min(quantum, remaining[i])
    remaining[i] -= exec_time
    time += exec_time

    for j in range(n):
        if AT[j] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    if remaining[i] > 0:
        queue.append(i)
    else:
        CT[i] = time

TAT = [CT[i] - AT[i] for i in range(n)]
WT = [TAT[i] - BT[i] for i in range(n)]

print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print("Average TAT:", sum(TAT)/n)
print("Average WT:", sum(WT)/n)

#Producer-Consumer
import threading
import time

buffer = []
size = 5

def producer():
    for i in range(10):
        while len(buffer) == size:
            pass
        buffer.append(i)
        print("Produced:", i)
        time.sleep(1)

def consumer():
    for i in range(10):
        while len(buffer) == 0:
            pass
        item = buffer.pop(0)
        print("Consumed:", item)
        time.sleep(2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()


#bankers algorithm
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

print("Enter Allocation Matrix:")
allocation = [list(map(int, input().split())) for _ in range(n)]

print("Enter Maximum Matrix:")
maximum = [list(map(int, input().split())) for _ in range(n)]

print("Enter Available Resources:")
available = list(map(int, input().split()))

# Calculate Need Matrix
need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

finish = [False] * n
safe_sequence = []

work = available[:]

while len(safe_sequence) < n:
    found = False

    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]

                safe_sequence.append(i)
                finish[i] = True
                found = True

    if not found:
        break

# Output
print("\nNeed Matrix:")
for row in need:
    print(row)

if len(safe_sequence) == n:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in safe_sequence))
else:
    print("\nSystem is NOT in safe state")