def get_status(current_attendance, percent_required, lec_needed, can_miss, maximum_attendance):

    if current_attendance >= percent_required:
        return "Safe"

    elif maximum_attendance < percent_required:
        return "Failed."

    elif can_miss > 0:
        return "Caution"

    else:
        return "Danger!"