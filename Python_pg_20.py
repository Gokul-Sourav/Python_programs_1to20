i=0
j=1
temp=0
input1 = input("Enter the Range :")
#printing fibonacci series
print i
print j
for x in range(2,input1+1):
    temp=i+j
    print temp
    i=j
    j=temp
