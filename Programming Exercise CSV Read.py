import csv


def read_grades():
    # Open the CSV file in read mode
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        # Read and display header
        headers = next(reader)
        print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<8} {headers[3]:<8} {headers[4]:<8}")
        print("-" * 54)

        # Display each row in a tabular format
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")


# Run the function
if __name__ == "__main__":
    read_grades()