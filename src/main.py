prelim_grade = 0
midterm_grade = 0
final_grade = 0
semester_grade = 0

prelim_grade = float (input("Enter prelim grade: "))
midterm_grade = float (input("Enter midterm grade: "))
final_grade = float (input ("Enter final grade: "))

semester_grade = (prelim_grade * 0.3) + (midterm_grade* 0.3) + (final_grade * 0.4)

print ("Semester_grade: %.2f" %(semester_grade))

if semester_grade < 60:
    print ("Faild.")
else : 
    #DISPLAY
    print ("Passed.")
    
    