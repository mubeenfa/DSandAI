print("-----------------------------")

# Get total employees with error handling
while True:
    try:
        employees = int(input("Enter total Employees: "))
        if employees <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get days per week with error handling
while True:
    try:
        days_per_week = int(input("Enter days per week: "))
        if days_per_week <= 0 or days_per_week > 7:
            print("Please enter a number between 1 and 7.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("-----------------------------\n")
empdict = {}

for e in range(1, employees + 1):
    emp_name = input(f"\nEnter Employee #{e} Name: ")
    attend_list = []
    total_attendance = 0

    for w in range(1, 5):  # 4 weeks
        while True:
            try:
                attendance = int(input(f"Enter attendance for Week-{w} (out of {days_per_week}): "))
                if attendance < 0 or attendance > days_per_week:
                    print(f"Invalid. Please enter a number between 0 and {days_per_week}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        attend_list.append(attendance)
        total_attendance += attendance

    avg = (total_attendance / (days_per_week * 4)) * 100.0
    empdict[emp_name] = avg

    # Print feedback for this employee
    print(f"\nAttendance Average for {emp_name}: {avg:.2f}%")
    if avg > 80:
        print("Good Job, 5000 bonus")
    elif avg == 80:
        print("At Risk")
    else:
        print("Needs Improvement")

# Optionally print all data
print("\n-----------------------------")
print("Employee Attendance Summary:")
for name, avg in empdict.items():
    print(f"{name}: {avg:.2f}%")