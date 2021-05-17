a = list(map(int, input().split()))
"""
Brute force
T.C.-O(nlog(n))
S.C.-O(1)

a.sort()
for i in range(len(a)-1):
  if a[i]==a[i+1]:
    print(a[i])
    break 
 
using frequency array   
T.C.-O(n)
S.C.-O(n)

f = [0]*len(a)
for i in a:
  if f[i]!=0:
    print(i)
    break
  else:
    f[i] = 1
    
Optimal approach tortoise method
Tc- O(n)
Sc- O(1)

"""

slow = a[0]
fast = a[0]

while True:
  slow = a[slow]
  fast = a[a[fast]]
  if slow == fast:
    break

fast = a[0]
while slow!=fast:
  slow = a[slow]
  fast = a[fast]
  
    
  


print(slow)
  
  



