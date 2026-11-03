
def getMaximumValue(*args):
    print(args)
    max=args[0]
    for i in args:
        if(i>=max):
            max=i
    return max


maximumValue=getMaximumValue(100,500,200,800,12000,8000,3000);
print("Maximum value is",maximumValue)