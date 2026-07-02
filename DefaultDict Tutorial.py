# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
f={}


for i in range(n):
    b=input()
    if b not in f.keys():
        f[b]=str(i+1)
    else:
        f[b]+=' '+str(i+1)
for i in range(m):
    c=input()
    if c in f.keys():
        print(f[c])
    else:
        print(-1) 
