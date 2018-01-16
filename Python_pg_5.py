import sys
#printing command line arguments separately
print sys.argv[1]
print sys.argv[2]
print sys.argv[3]
print sys.argv[4]
print sys.argv[5]
input1=int(sys.argv[1])
input2=int(sys.argv[2])
input3=int(sys.argv[3])
#checking input1
if ( (input1 > input2) and (input1 > input3) ):
    print "%d is the Biggest number in the First three command line arguments" %(input1)
    # Checking input2
elif ( (input2 > input3) and (input2 > input1) ):
    print "%d is the Biggest number in the First three command line arguments" %(input2)
    # Checking input3
else:
    print "%d is the Biggest number in the First three command line arguments" %(input3)
