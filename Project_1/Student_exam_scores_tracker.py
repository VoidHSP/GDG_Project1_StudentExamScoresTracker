class StudentExamScoresTracker:

    #This Function will keep a Dictionary to maintain record of students.
    def __init__(Record_list_dict):
        Record_list_dict.students = {}

    #This Function will add a new student to the record that was created initially. 
    
    def add_student(Record_list_dict, name, scores):
        if name in Record_list_dict.students:
            print(f"Student {name} already exists in the record.Either you can update scores with the update_scores option or just enter a new name to insert scores.")
        else:
            Record_list_dict.students[name] = scores
            print(f"Added student {name} with scores: {scores}")

    #This Function will update the scores after checking that a student with same name exists or not.

    def update_scores(Record_list_dict, name, scores):
        if name in Record_list_dict.students:
            Record_list_dict.students[name] = scores
            print(f"Updated scores for {name}: {scores}")
        else:
            print(f"Student {name} not found inside the record. Please add them first.")

    #This function will display all the students that is the whole record

    def display_students(Record_list_dict):
        if not Record_list_dict.students:
            print("No prior record is being found please enter some students with scores to display")
        else:
            print("Students and their scores:")
            for name, scores in Record_list_dict.students.items():
                print(f"Student: {name}, Scores: {scores}")

    #This function will calculate  the Statistics part that is Average,highest and lowest scores of a student

    def calculate_statistics(Record_list_dict, name):
        if name in Record_list_dict.students:
            scores = Record_list_dict.students[name]
            average = float(sum(scores) / len(scores))
            highest = max(scores)
            lowest = min(scores)
            return {
                "average": average,
                "highest": highest,
                "lowest": lowest,
            }
        else:
            print(f"Student {name} does not exist in the record.")
            return None
   
    #This function will remove a student from the MAin record 

    def remove_student(Record_list_dict, name):
        if name in Record_list_dict.students:
            del Record_list_dict.students[name]
            print(f"Removed student {name}.")
        else:
            print(f"Student {name} does not exist in the record.")

def main():
    Record = StudentExamScoresTracker()

    while True:
        print("\nOptions:")
        print("1. Add New Student")
        print("2. Update Scores")
        print("3. Display Students")
        print("4. Calculate Statistics")
        print("5. Remove Student")
        print("6. Exit")
        
        choice = input("Enter your choice in terms of numbers according to your favourable option: ")

        if choice == '1':
            name = input("Enter student name: ")
            scores = list(map(int,input("Enter scores separated by space: ").split()))
            Record.add_student(name, scores)

        elif choice == '2':
            name = input("Enter student name: ")
            scores = list(map(int,input("Enter new scores separated by space: ").split()))
            Record.update_scores(name, scores)

        elif choice == '3':
            Record.display_students()

        elif choice == '4':
            name = input("Enter student name: ")
            statistics = Record.calculate_statistics(name)
            if statistics is not None:
                print(f"Statistics for {name}: Average: {statistics['average']:.2f}, Highest: {statistics['highest']}, Lowest: {statistics['lowest']}")

        elif choice == '5':
            name = input("Enter student name to remove: ")
            Record.remove_student(name)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("You have choosen a wrong choice,please consider your choice and enter again ")

if __name__ == "__main__":
    main()
