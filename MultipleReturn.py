def checkMarks(marks1, marks2, marks3, marks4):
    total_marks = marks1 + marks2 + marks3 + marks4
    avg_marks = total_marks / 4

    if avg_marks >= 100:
        grade = "Pass"
    else:
        grade = "Fail"

    return total_marks, avg_marks, grade


math_marks = int(input("Enter mathematics marks: "))
physics_marks = int(input("Enter Physics marks: "))
chem_marks = int(input("Enter chemistry marks: "))
cs_marks = int(input("Enter computer science marks: "))

result = checkMarks(math_marks, physics_marks, chem_marks, cs_marks)
print("Total marks:", result[0])
print("Average marks:", result[1])
print("Grade:", result[2])

