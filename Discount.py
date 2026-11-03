amount=int(input("Enter the amount"));
dicount=0;
print("The Amount vcalue is",amount);
if(amount>=0 and amount<=5000):
    dicount=(amount *0.05);
    amount=(amount-dicount);
elif (amount>=5001 and amount <=10000):
    dicount=(amount *0.1);
    amount=(amount-dicount);
else:
    print("No discount");

print("The new amount value is",amount);