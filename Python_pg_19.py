#Using for loop
print "\nFor loop:"
for i in range(1,101):
    if(i==50):
        break
    elif(i==10 or i==20 or i==30 or i==40 ):
        continue
    elif (i%2==0):
        print i
    else:
        continue
#Using while loop
print "\nWhile loop:"
i=1
while i < 101:
    i=i+1
    if(i==90):
        break
    elif(i==60 or i==70 or i==80):
        continue
    elif (i%2==0):
        print i
    else:
        continue
