list1 = ['Gokul','Manish','Yogesh','Muthu','Siva']
str = raw_input("Enter a Name :")
count=0
#using in operator
if (str in list1):
    print "Using IN operator - The given Name is present in the list"
else:
    print "Using IN operator - The given Name is not present in the list"
#Without using in operator
for i in list1:
    if (i == str):
        count = 1
if(count == 0):
    print "Without Using IN operator - The given Name is not present in the list"
else:
    print "Without Using IN operator - The given Name is present in the list"
#printing elements in reverse
list1.reverse()
print "List in reverse order :",list1
