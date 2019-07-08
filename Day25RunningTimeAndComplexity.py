
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
for j in range(int(raw_input())):
    flag=0
    num=int(raw_input())
    for i in range(2,int(math.sqrt(num))+1):
        #print "i=",i,"num=",num
        if num%i==0:
            flag=1
#while(range):
    if num==1:
        print "Not prime"
    elif flag==0:
        print "Prime"
    else:
        print "Not prime"
