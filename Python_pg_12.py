#Intialising lists
input1=[]
below=[]
above=[]
equal=[]
average=0
#getting input from the user
print "Enter the ten Numbers :"
for i in range(10):
    temp = float(input())
    input1.insert(i,temp)
#finding average
for i in input1:
    average += i
average /= len(input1)
print "Average :",average
b=a=e=0
#finding below and above and equal numbers Corresponding to average
for i in input1:
    if (i<average):
        below.insert(b,i)
        b+=1
    elif(i>average):
        above.insert(a,i)
        a+=1
    else:
        equal.insert(e,i)
        e+=1
print "%d numbers are less than average :"%len(below),below
print "%d numbers are above than average :"%len(above),above
print "%d numbers are equal to average :"%len(equal),equal
