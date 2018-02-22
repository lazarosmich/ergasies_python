import urllib2
import datetime
import json

today=datetime.datetime.now()
lathos=0

table_save_days=[]
table_save_wins=[]

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s

while True:
    print "DWSTE 10 ARITHMOUS(1-80):\n"
    nums= raw_input().split()
    if (len(nums)==1):
        nums=nums[0].split(",")

    nums=map(int,nums)

    if (len(nums)==10):
        for i in range(10):
            if(nums[i]>=1 and nums[i]<=80):
                lathos=1
            else:
                lathos=0
    else: print "DWSATE LATHOS ARI8MO"

    if (lathos==1): break
print 22*"~"

for i in range(31):
    today= today - datetime.timedelta(days=1)
    date_str= today.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']

    sum_wins_day=0
    for k in klhrwseis:
        tmp=k["results"]
        epitixies=compare_lists(nums,tmp)
        if (epitixies>4):
            sum_wins_day+=1

    table_save_wins.insert(i,sum_wins_day)
    table_save_days.insert(i,date_str)

max_wins=table_save_wins[1]
max_day=table_save_days[1]
for i in range(31):
    if (max_wins < table_save_wins[i]):
        max_wins=table_save_wins[i]
        max_day=table_save_days[i]

print "8A EIXATE PERISOTERES EPITIXIES STIS", max_day, "ME", max_wins, "EPITIXIES"
print 70*"~"
