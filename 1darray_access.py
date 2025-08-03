from array import *
stu_roll =array('i',[0,1,2,3,4,5,6])

#using for loop
'''for el in stu_roll:
    print(el)'''

#using while loop

n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
   
   #append 
stu_roll.append(7)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1