data=input("Enter the Name");
print("The value is", data.upper());
count=0;
for d in data:
    if((d=='A' or d=='a') or (d=='E' or d=='e') or (d=='I' or d=='i') or  (d=='o' or d=='O') or (d=='u' or d=='U')):
        count=(count+1);

print("Total vowel count is",count);
      

