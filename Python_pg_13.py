#getting input from the user
input1=input("Enter First Numbers :")
input2=input("Enter Second Numbers :")
input3=input("Enter Third Numbers :")
input4=input("Enter Fout Numbers :")
input5=input("Enter Five Numbers :")
#finding biggest number using if elif and else
if ( (input1 > input2) and (input1 > input3) and (input1 > input4) and (input1 > input5) ):
    print "%d is the biggest of 5 Numbers"%input1
elif ( (input2 > input1) and (input2 > input3) and (input2 > input4) and (input2 > input5) ):
    print "%d is the biggest of 5 Numbers"%input2
elif ( (input3 > input1) and (input3 > input2) and (input3 > input4) and (input3 > input5) ):
    print "%d is the biggest of 5 Numbers"%input3
elif ( (input4 > input1) and (input4 > input2) and (input4 > input3) and (input4 > input5) ):
    print "%d is the biggest of 5 Numbers"%input4
else:
    print "%d is the biggest of 5 Numbers"%input5
