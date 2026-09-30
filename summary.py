def display_summary(courses, remaining, needed, status):

    print("\n\nxx------------ ATTENDANCE SUMMARY -------------xx")

    for i in range(len(courses)):
        print( courses[i], ":",
              "\t\tRemaining lectures:", remaining[i],
              "\t\tNeeded lectures:", needed[i],
              "\t\tSTATUS:", status[i] )