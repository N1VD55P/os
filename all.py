# ===================== DIVIDE & CONQUER =====================

# Binary Search
arr=[2,5,7,10,14,18]
key=10
low,high=0,len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print("Binary Search:",mid)
        break
    elif key<arr[mid]:
        high=mid-1
    else:
        low=mid+1


# Power of Number (Fast Exponentiation)
def power(x,n):
    if n==0: return 1
    if n%2==0:
        half=power(x,n//2)
        return half*half
    return x*power(x,n-1)

print("Power:",power(2,10))


# Fibonacci
def fib(n):
    if n<=1: return n
    return fib(n-1)+fib(n-2)

print("Fibonacci:",fib(6))


# Matrix Multiplication
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
C=[[0]*len(B[0]) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]
print("Matrix Multiplication:",C)


# Merge Sort
def merge(arr,l,m,r):
    L=arr[l:m+1]; R=arr[m+1:r+1]
    i=j=0;k=l
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i];i+=1
        else:
            arr[k]=R[j];j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i];i+=1;k+=1
    while j<len(R):
        arr[k]=R[j];j+=1;k+=1

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
def partition(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

def quick_sort(arr,l,h):
    if l<h:
        pi=partition(arr,l,h)
        quick_sort(arr,l,pi-1)
        quick_sort(arr,pi+1,h)

arr=[8,3,5,2]
quick_sort(arr,0,len(arr)-1)
print("Quick Sort:",arr)


# ===================== BASIC SORTING =====================

# Linear Search
arr=[5,3,7,1]
key=7
for i in range(len(arr)):
    if arr[i]==key:
        print("Linear Search:",i)

# Bubble Sort
arr=[5,2,9,1]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Bubble:",arr)

# Selection Sort
arr=[64,25,12]
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print("Selection:",arr)

# Insertion Sort
arr=[12,11,13]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("Insertion:",arr)


# ===================== GREEDY =====================

# Fractional Knapsack
w=[10,20,30]; p=[60,100,120]; cap=50
items=[(p[i]/w[i],w[i],p[i]) for i in range(len(w))]
items.sort(reverse=True)
total=0
for r,wt,val in items:
    if cap>=wt:
        cap-=wt; total+=val
    else:
        total+=r*cap; break
print("Knapsack:",total)


# Dijkstra
import heapq
g=[[(1,4),(2,1)],[(3,1)],[(1,2),(3,5)],[]]
dist=[float('inf')]*len(g)
dist[0]=0
pq=[(0,0)]
while pq:
    d,u=heapq.heappop(pq)
    for v,w in g[u]:
        if d+w<dist[v]:
            dist[v]=d+w
            heapq.heappush(pq,(dist[v],v))
print("Dijkstra:",dist)


# Prim
visited=[False]*len(g)
pq=[(0,0)]
cost=0
while pq:
    w,u=heapq.heappop(pq)
    if not visited[u]:
        visited[u]=True
        cost+=w
        for v,wt in g[u]:
            if not visited[v]:
                heapq.heappush(pq,(wt,v))
print("Prim:",cost)


# Kruskal
def find(p,i):
    if p[i]==i:return i
    return find(p,p[i])
def union(p,x,y):
    p[find(p,x)]=find(p,y)

edges=[(0,1,2),(1,2,3),(0,2,1)]
edges.sort(key=lambda x:x[2])
parent=list(range(3))
cost=0
for u,v,w in edges:
    if find(parent,u)!=find(parent,v):
        union(parent,u,v)
        cost+=w
print("Kruskal:",cost)


# Huffman Coding
import heapq
freq={'a':5,'b':9,'c':12,'d':13}
heap=[[wt,[ch,""]] for ch,wt in freq.items()]
heapq.heapify(heap)
while len(heap)>1:
    l=heapq.heappop(heap)
    r=heapq.heappop(heap)
    for p in l[1:]: p[1]='0'+p[1]
    for p in r[1:]: p[1]='1'+p[1]
    heapq.heappush(heap,[l[0]+r[0]]+l[1:]+r[1:])
print("Huffman:",heap)


# ===================== DYNAMIC PROGRAMMING =====================

# 0/1 Knapsack
wt=[10,20,30]; val=[60,100,120]; W=50
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
X="ABCBDAB"; Y="BDCAB"
m,n=len(X),len(Y)
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        if X[i]==Y[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print("LCS:",dp[m][n])


# Matrix Chain Multiplication
import sys
p=[30,35,15,5]
n=len(p)
dp=[[0]*n for _ in range(n)]
for l in range(2,n):
    for i in range(1,n-l+1):
        j=i+l-1
        dp[i][j]=sys.maxsize
        for k in range(i,j):
            q=dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
            dp[i][j]=min(dp[i][j],q)
print("MCM:",dp[1][n-1])


# Bellman-Ford
edges=[(0,1,4),(0,2,1),(2,1,2)]
V=3
dist=[float('inf')]*V
dist[0]=0
for _ in range(V-1):
    for u,v,w in edges:
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
print("Bellman-Ford:",dist)


# Floyd Warshall
INF=999
graph=[[0,5,INF],[INF,0,3],[INF,INF,0]]
n=len(graph)
dist=[row[:] for row in graph]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
print("Floyd Warshall:",dist)


# ===================== STRING MATCHING =====================

# Naive
t="aabbcbb"; p="bbc"
for i in range(len(t)-len(p)+1):
    if t[i:i+len(p)]==p:
        print("Naive Match:",i)


# KMP
def kmp(text,pat):
    lps=[0]*len(pat)
    j=0
    for i in range(1,len(pat)):
        while j>0 and pat[i]!=pat[j]:
            j=lps[j-1]
        if pat[i]==pat[j]:
            j+=1
            lps[i]=j
    j=0
    for i in range(len(text)):
        while j>0 and text[i]!=pat[j]:
            j=lps[j-1]
        if text[i]==pat[j]:
            j+=1
        if j==len(pat):
            print("KMP Match:",i-j+1)
            j=lps[j-1]

kmp("aabbcbb","bbc")


# ===================== BACKTRACKING =====================

# N-Queens
N=4
board=[-1]*N
def safe(r,c):
    for i in range(r):
        if board[i]==c or abs(board[i]-c)==abs(i-r):
            return False
    return True
def solve(r):
    if r==N:
        print("NQueen:",board)
        return
    for c in range(N):
        if safe(r,c):
            board[r]=c
            solve(r+1)
solve(0)


# Sum of Subsets
arr=[10,7,5,18,12]
target=35
def subset(i,cur,sum):
    if sum==target:
        print("Subset:",cur); return
    if i>=len(arr) or sum>target:
        return
    subset(i+1,cur+[arr[i]],sum+arr[i])
    subset(i+1,cur,sum)
subset(0,[],0)