# ===================== DIVIDE & CONQUER =====================

# Matrix Multiplication
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = [[0]*len(B[0]) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication:", C)


# Binary Search
arr = [2,5,7,10,14,18]
key = 10
low, high = 0, len(arr)-1

while low <= high:
    mid = (low+high)//2
    if arr[mid] == key:
        print("Binary Search Found at:", mid)
        break
    elif key < arr[mid]:
        high = mid-1
    else:
        low = mid+1


# Merge Sort
def merge(arr,l,m,r):
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    i=j=0;k=l
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]; i+=1
        else:
            arr[k]=R[j]; j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]; i+=1; k+=1
    while j<len(R):
        arr[k]=R[j]; j+=1; k+=1

def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

arr=[8,3,5,2]
merge_sort(arr,0,len(arr)-1)
print("Merge Sort:",arr)


# Quick Sort
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr=[8,3,5,2]
quick_sort(arr,0,len(arr)-1)
print("Quick Sort:",arr)


# ===================== BASIC SORTING =====================

# Bubble Sort
arr=[5,2,9,1]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Bubble Sort:",arr)


# Selection Sort
arr=[64,25,12,22]
for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_idx]:
            min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
print("Selection Sort:",arr)


# Insertion Sort
arr=[12,11,13,5]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("Insertion Sort:",arr)


# ===================== GREEDY =====================

# Fractional Knapsack
weights=[10,20,30]
profits=[60,100,120]
capacity=50

items=[]
for i in range(len(weights)):
    items.append((profits[i]/weights[i],weights[i],profits[i]))

items.sort(reverse=True)

total=0
for ratio,w,p in items:
    if capacity>=w:
        capacity-=w
        total+=p
    else:
        total+=ratio*capacity
        break
print("Knapsack:",total)


# Dijkstra
import heapq
graph=[[(1,4),(2,1)],[(3,1)],[(1,2),(3,5)],[]]
dist=[float('inf')]*len(graph)
dist[0]=0
pq=[(0,0)]

while pq:
    d,node=heapq.heappop(pq)
    for nei,w in graph[node]:
        if d+w<dist[nei]:
            dist[nei]=d+w
            heapq.heappush(pq,(dist[nei],nei))
print("Dijkstra:",dist)


# Prim
import heapq
graph=[[(1,2),(3,6)],[(0,2),(2,3)],[(1,3)],[(0,6)]]
visited=[False]*len(graph)
pq=[(0,0)]
cost=0

while pq:
    w,node=heapq.heappop(pq)
    if not visited[node]:
        visited[node]=True
        cost+=w
        for nei,wt in graph[node]:
            if not visited[nei]:
                heapq.heappush(pq,(wt,nei))
print("Prim MST:",cost)


# Kruskal
def find(parent,i):
    if parent[i]==i: return i
    return find(parent,parent[i])

def union(parent,x,y):
    parent[find(parent,x)]=find(parent,y)

edges=[(0,1,2),(1,2,3),(0,3,6)]
edges.sort(key=lambda x:x[2])
parent=list(range(4))
cost=0

for u,v,w in edges:
    if find(parent,u)!=find(parent,v):
        union(parent,u,v)
        cost+=w
print("Kruskal MST:",cost)


# ===================== DYNAMIC PROGRAMMING =====================

# 0/1 Knapsack
wt=[10,20,30]
val=[60,100,120]
W=50
n=len(wt)

dp=[[0]*(W+1) for _ in range(n+1)]

for i in range(1,n+1):
    for w in range(W+1):
        if wt[i-1]<=w:
            dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
        else:
            dp[i][w]=dp[i-1][w]
print("0/1 Knapsack:",dp[n][W])


# LCS
X="ABCBDAB"
Y="BDCAB"
m=len(X); n=len(Y)
dp=[[0]*(n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        if X[i]==Y[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print("LCS Length:",dp[m][n])


# ===================== STRING MATCHING =====================

# Naive String Matching
text="aabbcbbcabbb"
pattern="bbc"

for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)]==pattern:
        print("Pattern found at:",i)


# ===================== BACKTRACKING =====================

# N-Queens (4)
N=4
board=[-1]*N

def safe(r,c):
    for i in range(r):
        if board[i]==c or abs(board[i]-c)==abs(i-r):
            return False
    return True

def solve(r):
    if r==N:
        print("Solution:",board)
        return
    for c in range(N):
        if safe(r,c):
            board[r]=c
            solve(r+1)

solve(0)