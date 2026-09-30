def when_posi_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def when_non_nega_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value >= 0:
                return value
            else:
                print("Please enter 0 or a positive number.")

        except ValueError:
            print("Please enter a valid whole number.")


def when_percentage(prompt):
    while True:
        try:
            value = float(input(prompt))

            if 0 <= value <= 100:
                return value
            else:
                print("Percentage must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def valid_lec_count(total_lec, lec_attended, lec_absent):
    if lec_attended + lec_absent <= total_lec:
        return True
    else:
        return False