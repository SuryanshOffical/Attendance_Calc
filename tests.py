from attendance_calculator import calculate_attendance
from status_manager import get_status


print("------------ TESTING ATTENDANCE CALCULATOR ------------")


result = calculate_attendance(100, 80, 10, 75)

status = get_status(result[1], 75, result[2], result[3], result[5])

print("Test 1 - Expected: Safe")
print("Actual:", status)

if status == "Safe":
    print("PASS")
else:
    print("FAIL")


result = calculate_attendance(100, 60, 10, 75)

status = get_status(result[1], 75, result[2], result[3], result[5])

print("\nTest 2 - Expected: Caution")
print("Actual:", status)

if status == "Caution":
    print("PASS")
else:
    print("FAIL")


result = calculate_attendance(100, 74, 25, 75)

status = get_status(result[1], 75, result[2], result[3], result[5])

print("\nTest 3 - Expected: Danger!")
print("Actual:", status)

if status == "Danger!":
    print("PASS")
else:
    print("FAIL")

result = calculate_attendance(100, 50, 40, 75)

status = get_status(result[1], 75, result[2], result[3], result[5])

print("\nTest 4 - Expected: Failed.")
print("Actual:", status)

if status == "Failed.":
    print("PASS")
else:
    print("FAIL")