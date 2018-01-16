input1 = input("Enter the Range :")
list1=[]
#getting input from the user
print "Enter the %d Numbers :"%input1
for i in range(input1):
    x=input()
    list1.insert(i,x)
# finding biggest and Smallest nunber in the range
list1.sort()
print "The Biggest Number in the Range is :%d"%list1[len(list1)-1]
print "The Smallest Number in the Range is :%d"%list1[0]
