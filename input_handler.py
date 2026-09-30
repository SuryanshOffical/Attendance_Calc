from validators import when_posi_int
from validators import when_non_nega_int
from validators import when_percentage
from validators import valid_lec_count


def get_course_data():

    course_name = input("Enter course name: ").strip().title()

    total_lec = when_posi_int(
        "Enter total number of lectures for the course: "
    )

    while True:

        lec_attended = when_non_nega_int(
            "Enter number of lectures attended so far: "
        )

        lec_absent = when_non_nega_int(
            "Enter number of lectures not attended so far: "
        )

        if valid_lec_count(total_lec, lec_attended, lec_absent):
            break

        print("Error: Attended + absent lectures cannot exceed total lectures.")
        print("Please enter the lecture counts again.")

    percent_required = when_percentage(
        "Enter mandatory overall attendance percentage required: "
    )

    return course_name, total_lec, lec_attended, lec_absent, percent_required