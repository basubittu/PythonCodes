dayCount=int(input("enter the dayCount"));
print("dayCount--->",dayCount);
dayName='';

if(dayCount==1):
    dayName='Sunday';
elif (dayCount==2):
    dayName='Monday';
elif (dayCount==3):
    dayName='Tuesday';
elif (dayCount==4):
    dayName='WednesDay';
elif (dayCount==5):
    dayName='ThursDay';
elif (dayCount==6):
    dayName='Friday';
else:
    dayName='SaturDay';


print("DayCount---->",dayCount,"dayName---->",dayName);

