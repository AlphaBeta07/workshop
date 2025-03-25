# 13. Student Grade Calculator
# 📌 Create a function that takes a student's marks and returns their grade based on the following
# criteria:
# ● 90-100: A
# ● 80-89: B
# ● 70-79: C
# ● 60-69: D
# ● Below 60: F

def Grade():
    marks = int(input("enter marks "))
    if marks > 90 and marks < 100:
        print("grade is A")
    elif marks > 80 and marks < 89:
        print("grade is B")
    elif marks > 70 and marks < 79:
        print("grade is C")
    elif marks > 60 and marks < 69:
        print("grade is D")
    else:
        print("grade is F")

Grade()