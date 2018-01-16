input1= input('Enter the First number :')
input2= input('Enter the Second number :')
input3= input('Enter the Third number :')
# Checking input1
if ( (input1 > input2) and (input1 > input3) ):
    print "%d is the Bigger than %d and %d"%(input1,input2,input3)
    # Checking input2
elif ( (input2 > input3) and (input2 > input1) ):
    print "%d is the Bigger than %d and %d"%(input2,input1,input3)
    # Checking input3
else:
    print "%d is the Bigger than %d and %d"%(input3,input1,input2)
