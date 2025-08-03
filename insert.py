from array import *
stu_roll =array('i',[0,1,2,3,4,5,6])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
stu_roll.insert(1,106)
stu_roll.insert(3,107)

n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1