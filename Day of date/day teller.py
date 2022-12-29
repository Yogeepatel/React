def year(n):
    yodd=0
    x=(n//100) * 100
    y=n-x-1
    x1=x%400
    if x1==0:
        yodd=0
    elif x1==100:
        yodd=5
    elif x1==200:
        yodd = 3
    elif x1==300:
        yodd = 1
    leapyrs=y//4
    y1=((leapyrs)*2)%7
    y2=(y-leapyrs)%7
    yodd  = yodd + y1 + y2
    return yodd

def month(n):
    d={1:3,2:0,3:3,4:2,5:3,6:2,7:3,8:3,9:2,10:3,11:2,12:3}
    modd=0
    for i in range(1,n):
        modd = modd + d[i]
    modd = modd % 7
    return  modd


days={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}

odddays=0
date=input("Enter date in format dd-mm-yyyy or dd/mm/yyyy : ")
if "-" in date:
    l=list(date.split("-"))
else:
    l = list(date.split("/"))

d=int(l[0])
m=int(l[1])
y=int(l[2])
if y%100==0 and y%400==0:
    odddays=1
elif y%100 != 0 and y%4==0:
    odddays = 1
else:
    odddays=0

ans = days[((month(m) + year(y) + odddays + (d%7))%7)]


print(ans)