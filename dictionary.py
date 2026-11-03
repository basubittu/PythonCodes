dict1={"name":"Abhishek Basu", "Age":30};
print(dict1);
l1=["basicSalary","hra","Providentfund"];
l2=[300000,20000,600000];
l4=zip(l1,l2);
d3=dict(l4);
print(d3);
print("basicSalary------>",d3['basicSalary']);
print(d3);
for i in d3:
    print(i,"=",d3[i]);