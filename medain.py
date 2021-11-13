import csv
with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range (len(filedata)):
    num=filedata[i][1] 
    newdata.append(float(num))
n=len(newdata)
print (n)
newdata.sort()
if n%2==0:
    m1=float(newdata[n//2])
    m2=float(newdata[n//2-1])
    median=(m1+m2)/2
else:
    median=newdata[n//2]  
print(str(median))