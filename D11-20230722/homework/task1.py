students_data = [
    {
        "name": "John",
        "mid_term_result" : {"math": 30, "science": 42},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 3},
            {"month": "augest", "total_working_days": 24, "leave": 0},
            {"month": "sept", "total_working_days": 25, "leave": 2}
        ]
    },
    {
        "name": "Emma",
        "mid_term_result": {"math": 20, "science": 49},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 6},
            {"month": "augest", "total_working_days": 24, "leave": 10},
            {"month": "sept", "total_working_days": 24, "leave": 5}
        ]
    },
    {
        "name": "Alex",
        "mid_term_result": {"math": 30, "science": 40},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 5},
            {"month": "augest", "total_working_days": 24, "leave": 6},
            {"month": "sept", "total_working_days": 24, "leave": 4}
        ]
    },
]


print("Students not eligible for the quarterly exam:")
for student in students_data:

    math_score = student["mid_term_result"]["math"]
    science_score = student["mid_term_result"]["science"]

    total_working_days = 0
    total_leaves = 0

    for attendance_data in student["attendance"]:
        total_working_days += attendance_data["total_working_days"]
        total_leaves += attendance_data["leave"]

    attendance_percentage = ( (total_working_days - total_leaves) / total_working_days ) * 100

    if (math_score < 35 or science_score < 35) and attendance_percentage < 80:
        print(student["name"])
