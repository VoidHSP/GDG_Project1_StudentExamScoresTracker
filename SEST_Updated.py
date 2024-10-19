Students = [
    {"Name" : "Harsh","Scores" : [15,16,17]},
    {"Name" : "Nisha","Scores" : [25,26,47]},
    {"Name" : "Rahul","Scores" : [35,66,87]}
]
def add_Student():
    Name = input("Enter the Name of Student : \n")
    for i in Students:
        if i['Name']== Name:
            print("Student Already Exists in the Record\n") 
            return
        else :
            Score=list(map(int,input("Enter the marks with spaces\n").split()))
            open_student={"Name":Name , "Scores":Score}
            Students.append(open_student)
            return
def update_Scores():
    Name = input("Enter the Name of Student : \n")
    for i in Students:
        if i['Name']== Name:
            Score = list(map(int,input("Enter the marks with spaces \n").split()))
            i['Scores']=Score
            return
    print("Name Does not exist in the record.\n")
    return
def Display():
    for i in Students:
        print(f"Name : {i['Name']} ,Scores : {i['Scores']}")
    return
def Cal_stats():
    Name = input("Enter the Name of Student : \n")
    for i in Students:
        if i['Name']== Name:
            Score = i['Scores']
            AVG = float(sum(Score)/len(Score))
            High = max(Score)
            LOW = min(Score)
            print(f"Avergae Marks,Highest marks and Lowest marks  of {i['Name']} are {AVG:.2f},{High} and {LOW} respectively \n")
            return
    print("Name Does not exist in the record.\n")
    return
def Remove_Student():
    Name = input("Enter the Name of Student : \n")
    for i in Students:
        if i['Name']== Name:
            print(f"Data of {i['Name']} is deleted")
            Students.remove(i)
            return
    print("Name Does not exist in the record.\n")
    return
def main():
    while True:
        print("\nOptions:")
        print("1. Add New Student")
        print("2. Update Scores")
        print("3. Display Students")
        print("4. Calculate Statistics")
        print("5. Remove Student")
        print("6. Exit")
        choice = input("Enter your option\n")
        if choice == "1":
            add_Student()
        elif choice == "2":
            update_Scores()
        elif choice == "3":
            Display()
        elif choice == "4":
            Cal_stats()
        elif choice == "5":
            Remove_Student()
        elif choice == "6":
            print("Exiting the Program")
            break
        else :
            print("Wrong choice filled try again ")
if __name__ == "__main__":
    main()


