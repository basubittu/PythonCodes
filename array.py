quantity=[1,2,3,4];
price=[100,300,400,800];
total=0;
for i   in range(len(quantity)):
    total= total+(quantity[i]*price[i]);

print("The sum is",total);