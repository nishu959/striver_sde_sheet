
#declare a dp array to store result of subproblems
#to avoid repetative calculation
dp = [None]*(10000001)


#1st function 
#function process
def process(x):
    
    #if the given input is even
    if(x%2==0):
        return x//2
    
    #if the given input is odd
    else:
        return (3*x+1)//2

#2nd function
#function counter
#this returns the number of steps taken by a number to reach 1
def counter(y):
    
    #base cases
    #if number is 1 then it takes only 0 step to reach 1
    if(y==1):
        return 0
    
    #if number is 2 then it takes only 1 step to reach 1
    #i.e. 2/2 = 1
    if(y==2):
        return 1
  
    
    #to avoid index out of bound condition y<10000001 is used here
    #if the problem is already solve then return directly from dp
    if(y<10000001 and dp[y]!=None):
        return dp[y]
        
    #function process is called 
    a = process(y)
    
    #counter(a) will give number of steps taken by a to reach 1
    
    #number of steps taken by y to reach 1 = 
    ans = counter(a) + 1
    
    #to avoid index out of bound condition y<10000001 is used here
    if(y<10000001):
        dp[y] = ans
    
  
    return ans
    
   
    
#number of elements given 10000
for i in range(10000):
    #input in collected in p one by one
    p = int(input())
    print(counter(p))
  
  