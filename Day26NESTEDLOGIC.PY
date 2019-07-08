#Task 
#Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

#If the book is returned on or before the expected return date, no fine will be charged (i.e.: FINE=0).
#If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,FINE=15HACKOS X (THE NO. OF DAYS LATE).
#If the book is returned after the expected return month but still within the same calendar year as the expected return date, the FINE=500HACKOS X (THE NO. OF MONTHS LATE).
#If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 HACKOS.

# Enter your code here. Read input from STDIN. Print output to STDOUT
d,m,y=map(int,raw_input().split(" "))
D,M,Y=map(int,raw_input().split(" "))
#d=int(raw_input())
#m=int(raw_input())
#y=int(raw_input())
#D=int(raw_input())
#M=int(raw_input())
#Y=int(raw_input())

if Y==y:
    if m==M:
        if d==D or d<D:
            fine=0
        elif d>D:
            fine=(d-D)*15
    elif m<M:
        fine=0
    elif m>M:
        fine=(m-M)*500
elif y<Y:
    fine=0
else:
    fine=10000
print fine