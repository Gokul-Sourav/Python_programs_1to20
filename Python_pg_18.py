#Using for loop to print 1 to 100 and 100 to 1
print "\nFor loop:"
for i in range(1,201):
    if (i<=100):
        print i
    else:
        print 201-i
#Using while loop to print 1 to 100 and 100 to 1
print "\nWhile loop:"
temp=1
while temp < 201 :
    if (temp<=100):
        print temp
    else:
        print 201-temp
    temp +=1
#printing each character in mystring
mystring ="Hello world"
print "\nMystring characters in separate line :"
for i in mystring:
    print i
