# Import numpy for numerical operations
import numpy as np

# Load the CSV file into a numpy array
# Make sure your file path is correct, or use the CSV file in your repository
data = np.genfromtxt('student_grades.csv', delimiter=',', skip_header=1)

# Print the first few rows of the dataset to understand its structure
print("First 5 rows of the dataset:")
print(data[:5])

# Calculate and print statistics for each exam (column)
means = np.mean(data, axis=0)
medians = np.median(data, axis=0)
std_devs = np.std(data, axis=0)
mins = np.min(data, axis=0)
maxs = np.max(data, axis=0)

print("\nExam Statistics:")
print("Mean:", means)
print("Median:", medians)
print("Standard Deviation:", std_devs)
print("Minimum:", mins)
print("Maximum:", maxs)

# Flatten the data to get all grades combined
all_grades = data.flatten()

# Overall statistics for all exams combined
overall_mean = np.mean(all_grades)
overall_median = np.median(all_grades)
overall_std_dev = np.std(all_grades)
overall_min = np.min(all_grades)
overall_max = np.max(all_grades)

print("\nOverall Statistics:")
print("Mean:", overall_mean)
print("Median:", overall_median)
print("Standard Deviation:", overall_std_dev)
print("Minimum:", overall_min)
print("Maximum:", overall_max)

# Determine number of students who passed and failed each exam
passing_grades = data >= 60
passing_counts = np.sum(passing_grades, axis=0)  # Sum of True values (passed)
failing_counts = data.shape[0] - passing_counts  # Total students - passed students

print("\nPassing and Failing Counts per Exam:")
for i in range(data.shape[1]):
    print(f"Exam {i + 1}: Passed - {passing_counts[i]}, Failed - {failing_counts[i]}")

# Calculate overall pass percentage
total_passes = np.sum(passing_grades)
total_grades = data.size  # Total number of grades (students * exams)
pass_percentage = (total_passes / total_grades) * 100

print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

