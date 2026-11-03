def getMaximumData(a):
    max=a[0];
    print("The value is",max);
    for i   in  range(len(a)):
        if(a[i]>=max):
            max=a[i];
    return max;


a=[10,70,98,89,87];
print("The maximum value is",getMaximumData(a));




