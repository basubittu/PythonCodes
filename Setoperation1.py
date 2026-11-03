firstSet={10,20,30,40,50,60,70,80,90,100};
secondSet={30,40,50,60,70,80,90,100,200,300,400};
union_set=firstSet.union(secondSet);
print("union set---->",union_set);
intesectionset=firstSet.intersection(secondSet);
print("intersect data----->",intesectionset);
difference_set=firstSet.difference(secondSet);
print("Difference set----->",difference_set);
print(firstSet.issubset(secondSet))


