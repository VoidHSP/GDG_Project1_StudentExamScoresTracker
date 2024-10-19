Student_1 = {
    "Name" : "Joker",
    "Scores" : list(map(int,input("Enter the marks of Joker with spaces ").split()))
}
Student_2 = {
    "Name" : "Heron",
    "Scores" : list(map(int,input("Enter the marks of Heron with spaces ").split()))
}
Student_3 = {
    "Name" : "Ranger",
    "Scores" : list(map(int,input("Enter the marks of Ranger with spaces ").split()))
}

print(Student_1)
scores = Student_1["Scores"]
average = float(sum(scores)/len(scores))
highest = max(scores)
lowest = min(scores)
print(f"Average Score of {Student_1['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
print(Student_2)
scores = Student_2["Scores"]
average = float(sum(scores)/len(scores))
highest = max(scores)
lowest = min(scores)
print(f"Average Score of {Student_2['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
print(Student_3)
scores = Student_3["Scores"]
average = float(sum(scores)/len(scores))
highest = max(scores)
lowest = min(scores)
print(f"Average Score of {Student_3['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
Record ={
      "1" : "Student_1" , "2" : "Student_2" , "3" : "Student_3"
}
Name = input("Enter the NAme of Student\n")
if Student_1['Name']== Name:
    del Student_1["Name"]
    del Student_1["Scores"]
    print(Student_1)
elif Student_2['Name']== Name:
    del Student_2["Name"]
    del Student_2["Scores"]
    print(Student_2)
elif Student_3['Name']== Name:
    del Student_3["Name"]
    del Student_3["Scores"]
    print(Student_3)
else :
    print("Invalid Name ")
choice = input("If you want to update scores Enter The name of Student\n")
if Student_1['Name']== choice:
    Student_1["Scores"] = list(map(int,input("Enter the marks of Joker with spaces ").split()))
    print(Student_1)
    scores = Student_1["Scores"]
    average = float(sum(scores)/len(scores))
    highest = max(scores)
    lowest = min(scores)
    print(f"Average Score of {Student_1['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
elif Student_2['Name']== choice:
    Student_2["Scores"] = list(map(int,input("Enter the marks of Heron with spaces ").split()))
    print(Student_2)
    scores = Student_2["Scores"]
    average = float(sum(scores)/len(scores))
    highest = max(scores)
    lowest = min(scores)
    print(f"Average Score of {Student_2['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
elif Student_3['Name']== choice:
    Student_2["Scores"] = list(map(int,input("Enter the marks of Ranger with spaces ").split()))
    print(Student_2)
    scores = Student_3["Scores"]
    average = float(sum(scores)/len(scores))
    highest = max(scores)
    lowest = min(scores)
    print(f"Average Score of {Student_3['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
else :
    print("Wrong Name ")
Choice_1 = input("If you want to ADD a Student enter Yes\n")
if Choice_1=="Yes" or Choice_1=="yes":
    Student_4 ={}
    Student_4["Name"]=input("Enter the NAme of Student")
    Student_4["Scores"] = list(map(int,input("Enter the marks of  with spaces ").split()))
    print(Student_4)
    scores = Student_4["Scores"]
    average = float(sum(scores)/len(scores))
    highest = max(scores)
    lowest = min(scores)
    print(f"Average Score of {Student_4['Name']} is {average},highest marks is {highest} and lowest marks is {lowest} ")
else : 
    print("Wrong word")
Choice_2 = input("If you want to display all students enter Yes")
if Choice_2=="Yes" or Choice_2=="yes":
    print(Student_1)
    print(Student_2)
    print(Student_3)
    print(Student_4)
else :
    print("Program ends here ")










