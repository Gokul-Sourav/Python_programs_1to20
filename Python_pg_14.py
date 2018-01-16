list1 = [391832,391834,391835,391837,391838,391840,391854,391864,391862,391874]
list2 = ['Gokul','Manish','Yogesh','Muthu','Siva','Sampath','Ranjith','Mahendran','Thiyanesh','Jagan']
for x in list2:
    print x
index=input("\nEnter the Index :")
#Performing Corresponding operations on list
print "Corresponding value to index :",list1[index],list2[index]
print "\nNames from 4th position to 9th position :",list2[4:10]
print "\nAll names from 3rd position till end of the list :",list2[3:]
times=input('\nEnter the Nth value for N number of times :')
print "\nRepeated list elements :",list1*times,list2*times
print "\nConcatenation :",list1+list2
print "\nTwo list values side by side :"
for i in range(10):
    print list1[i],list2[i]
    print "\n"
