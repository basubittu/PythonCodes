n=int(input("Enter the Number"));

for i   in range (1,n+1,2):
    if(i==2):
        continue;
    print("The Value is",i);

for i in range(1,10):
    print(i)

numbers = [10, 20, 30, 40]

if numbers:
    mean = sum(numbers) / len(numbers)
    print("Mean:", mean)
else:
    print("The list is empty; mean cannot be calculated.")
