input1 = input("Enter a Number :")
count = 0
# checking with value 1
if ( input1 == 1):
    print "%d is Neither a prime nor composite"%input1
#checking the given number prime or not
else:
    for i in range(2,input1+1):
        if(input1 % i == 0):
            count+=1
    if(count == 1):
        print "%d is a Prime Number"%input1
    else:
        print "%d is a Not Prime Number"%input1
#checking the given number prime or not in a range
input2 = input("Enter a Range :")
for i in range(2,input2+1):
    count =0
    for j in range(2,i+1):
        if(i % j ==0 ):
            count +=1
    if(count == 1):
        print i
