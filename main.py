from input_handler import get_course_data
from attendance_calculator import calculate_attendance
from status_manager import get_status
from summary import display_summary
from validators import when_posi_int


courses = []
remaining = []
needed = []
status = []

course_count = when_posi_int("Enter number of courses: ")

for i in range(course_count):

    print("\n---------- COURSE", i + 1, "----------")

    course_name, total_lec, lec_attended, lec_absent, percent_required = get_course_data()

    (
        lec_remaining,
        current_attendance,
        lec_needed,
        can_miss,
        final_attendance,
        maximum_attendance
    ) = calculate_attendance(
        total_lec,
        lec_attended,
        lec_absent,
        percent_required
    )

    stat = get_status(
        current_attendance,
        percent_required,
        lec_needed,
        can_miss, 
        maximum_attendance
    )

    print("\nFor your course", course_name, "-")
    print("Current overall attendance:", current_attendance, "%")
    print("Lectures remaining:", lec_remaining)
    print("Lectures needed for required attendance:", lec_needed)
    print("Lectures you can miss:", can_miss)
    print("Attendance after needed lectures:", final_attendance, "%")
    print("Maximum possible attendance:", maximum_attendance, "%")
    print("STATUS:", stat)

    courses += [course_name]
    remaining += [lec_remaining]
    needed += [lec_needed]
    status += [stat]


display_summary(courses, remaining, needed, status)