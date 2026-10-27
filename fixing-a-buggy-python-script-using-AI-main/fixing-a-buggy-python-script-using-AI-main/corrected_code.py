%%writefile student_utils.py

PASS_MARK = 40

def calculate_average(marks):
    total = 0

    for m in marks:
        total = total + m

    return total / (len(marks))


def is_passing(mark):
    if mark >= PASS_MARK:
        return True

    return False


def get_grade(average):
    if average >= 90:
        return "Distinction"

    elif average >= 60:
        return "first"

    elif average >= 45:
        return "second"

    return "Fail"
print(calculate_average([80,90,100]))
