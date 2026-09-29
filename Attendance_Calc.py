courses = []
remaining = []
needed = []
status = []

course_count = int(input("Enter number of courses- "))

for i in range(course_count):

    course_name = (input("Enter course name: ").strip().title())
    total_lec = abs(int(input("Enter total number of lectures for the course: ")))
    lec_attended = abs(int(input("Enter number of lectures attended so far: ")))
    lec_absent = abs(int(input("Enter number of lectures not attended so far: ")))
    percent_required = abs(float(input("Enter mandatory overall attendance percentage required: ")))
    print("\n\n\n")

    lec_held = lec_attended + lec_absent
    lec_remaining =total_lec - (lec_held)
 
    current_attendance = round((lec_attended/total_lec)*100, 2)

    print("For  your course", course_name,"-")
    print("Total lectures being:", total_lec)
    print("Number of lectures attended are:", lec_attended)
    print("Number of lectures not attended are:", lec_absent, "\n")
    print("Your current overall attendance percentage is", current_attendance, "%.")
    print("Whereas, the required overall attendance percentage is", percent_required,"%.\n")
    print("The number of lectures left in your course are", lec_remaining,".\n\n")

    can_miss = 0
    lec_needed = 0
    stat = "Unknown"

    if current_attendance >= percent_required:
        can_miss = lec_remaining
        stat = "Safe"
        print("Attendance STATUS: Safe\n")
        print("You have met the overall attendance percentage as the required overall attendance percentage was",
               percent_required, "%.")
        print("You can miss all", can_miss, "of your remaining lectures.")
        print("Have fun :)")
        print("\n\n")

    else:
        while ((lec_attended + lec_needed)/(total_lec))*100 < percent_required and lec_needed < lec_remaining:
            lec_needed += 1
            can_miss = lec_remaining - lec_needed
        
        if ((lec_attended + lec_needed)/(total_lec))*100 >= percent_required:
            if can_miss > 0:
                stat = "Caution"
                print("Attendance STATUS: Caution\n")
                print("The minimum number of lectures to be attended for mandatory attendance percentage is ",
                       lec_needed, "!", sep="")
                print("But you can still miss", can_miss, "lectures ;)")
                print("\n\n")

            else:
                stat = "Danger!"
                print("Attendance STATUS: Danger!\n")
                print("You would have to attend all the remaining lectures for required attendance percentage!")
                print("\n\n")
       
        else:
            stat = "Failed."
            print("Attendance STATUS: Failed.\n")
            print("Sorry, you would not be able to meet the mandatory overall attendance percentage. :(")
            print("The maximum possible attendance which can be achieved still is ",
                   (lec_attended + lec_remaining)/total_lec*100,"%.", sep="")
            print("\n\n")

    
    courses += [course_name]
    remaining += [lec_remaining]
    needed += [lec_needed]
    status += [stat]

print("\n\n------------ATTENDANCE SUMMARY--------------")

for i in range(course_count):
    print(courses[i], ":",
          "\tRemaining lectures:", remaining[i],
          "\tNeeded  lectures:", needed[i],
          "\tSTATUS:", status[i]
          )