# Input variable to enter the string
inp=raw_input("Enter the string \n")
length=len(inp)
print length
revinp=''
for i in range(length-1,-1,-1):
 revinp=revinp+inp[i]
print revinp
 
