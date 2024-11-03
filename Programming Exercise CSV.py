import csv


def write_grades():
    # Prompt instructor for number of students
    num_students = int(input("Enter the number of students: "))

    # Open the CSV file in write mode
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Collect and write data for each student
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student's information as a row in the CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Data written to grades.csv")


# Run the function
if __name__ == "__main__":
    write_grades()