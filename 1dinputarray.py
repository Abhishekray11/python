# getting input from user using for loop 

from array import *
stu_roll =array('i',[])
n = int(input("enter no of element"))

for i in range(n):
  stu_roll.append(int(input(('enter element'))))
  
for i in range(len(stu_roll)):
    print(stu_roll[i])
    
    
i=0
j=0

while i<n:
    stu_roll.append(int(input("enter elements")))
    i+=1
    
while (j<len(stu_roll)):
    print(stu_roll[j])                
    j+=1