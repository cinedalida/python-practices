grade = int(input("Enter your grade:"))

# min, max, point, remark

grade_scales = [
    (97, 100, 4.0, "Excellent"),
    (93, 96, 4.0, "Excellent"),
    (90, 92, 3.7, "Very Good"),
    (87, 89, 3.3, "Good"),
    (83, 86, 3.0, "Good"),
    (80, 82, 2.7, "Satisfactory"),
    (77, 79, 2.3, "Satisfactory"),
    (73, 76, 2.0, "Pass"),
    (70, 72, 1.7, "Pass"),
    (67, 69, 1.3, "Pass"),
    (63, 66, 1.0, "Pass"),
    (60, 62, 0.7, "Fail"),
    (0, 59, 0.0, "Fail")
]

def get_grade_info(grade):
    for min_grade, max_grade, point, remark in grade_scales:
        if min_grade <= grade <= max_grade:
            return point, remark
    return None, "invalid grade"
    
point, remark = get_grade_info(grade)
if point is not None:
    print(f"Your grade point is {point} and remark is '{remark}'.")
else:
    print(remark)
    