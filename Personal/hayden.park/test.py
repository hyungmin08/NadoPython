year = int(input())
if((year%4==0) and ((year%100!=0) or (year%400==0))):
    output=1
else:
    output=0
print(output)