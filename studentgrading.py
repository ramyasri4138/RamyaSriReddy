def studentgrading(percentage):
    if percentage>90:
        return 'A'
    if percentage>80:
        return "B"
    if percentage>70:
        return 'C'
    else:
        return "Fail"
studentname=input("enter the student name: ")
marks=[]
for i in range(1,6):
    mark=int(input(f"enter student marks of {i} subject: "))
    marks.append(mark)
totalmarks=sum(marks)
percentage=(totalmarks/500)*100
grade=studentgrading(percentage)
print(f"studentname: {studentname}")
print(f"totalmarks: {totalmarks}")
print(f"percentage: {percentage}")
print(f"grade: {grade}")