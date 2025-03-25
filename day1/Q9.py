# 9. Student Grades - Tuple
# 📌 A university stores student grades in tuples because they are immutable. Write a program
# that takes a student's grades for 5 subjects and prints the highest, lowest, and average grade.

grades = tuple(map(int, input("Enter grades for 5 subjects (separated by spaces): ").split()))
    
if len(grades) != 5:
    print("Please enter 5 grades ")
   
    
highest = max(grades)
lowest = min(grades)
average = sum(grades) / len(grades)
    
print("Highest Grade: ",highest)
print("Lowest Grade: ",lowest)
print("Average Grade: ",average)