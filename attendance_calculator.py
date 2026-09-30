def calculate_attendance(total_lec, lec_attended, lec_absent, percent_required):

    lec_held = lec_attended + lec_absent
    lec_remaining = total_lec - lec_held

    current_attendance = round((lec_attended / total_lec) * 100, 2)

    lec_needed = 0

    while ((lec_attended + lec_needed) / total_lec) * 100 < percent_required and (lec_needed < lec_remaining):
        lec_needed += 1

    can_miss = lec_remaining - lec_needed

    final_attendance = round(((lec_attended + lec_needed) / total_lec) * 100, 2)
    maximum_attendance = round(((lec_attended + lec_remaining) / total_lec) * 100, 2)

    return (lec_remaining, current_attendance, lec_needed, can_miss, final_attendance, maximum_attendance)