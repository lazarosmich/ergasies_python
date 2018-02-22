y=int(raw_input("DWSE TON XRONO:"))
m=int(raw_input("DWSE TON MHNA : "))

if m ==1:
    m+=12
    y-=1
elif m==2:
    m+=12
    y-=1

x=((1 + 2*m + int((3*(m+1))/5) + y + int(y/4) - int(y/100) + int(y/400) + 2))%7

if x==0:
    x=7

months={
1:{'name':'January','days':31}
,2:{'name':'February','days':28}
,3:{'name':'March','days':31}
,4:{'name':'April','days':30}
,5:{'name':'May','days':31}
,6:{'name':'June','days':30}
,7:{'name':'July','days':31}
,8:{'name':'August','days':31}
,9:{'name':'September','days':30}
,10:{'name':'October','days':31}
,11:{'name':'November','days':30}
,12:{'name':'December','days':31}
}

if m ==13:
    m-=12
    y+=1
elif m==14:
    m-=12
    y+=1

if months[m]['name']=="February":
    if y%4==0:
        if y%100!=0:
            end=months[m]['days']+1
        elif y%400==0:
            end=months[m]['days']+1
        else:
            end=months[m]['days']
    else:
        end=months[m]['days']
else:
    end=months[m]['days']
print"\n",months[m]['name'],y
print"S\tM\tT\tW\tT\tF\tS"
counter=0
counter2=0
dayprinter=1
for i in range (1,end+6+1):
    counter+=1
    if i<x or i>=end+1+counter2 :
        counter2+=1
        if counter%7==0:
            print "\t"
        else:
            print "\t",
    else:
        if counter%7==0:
            print dayprinter,"\t"
            dayprinter+=1
        else:
            print dayprinter,"\t",
            dayprinter+=1
