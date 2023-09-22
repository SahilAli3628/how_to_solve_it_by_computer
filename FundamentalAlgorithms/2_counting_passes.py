#program to count howmany studenta have attained marks above the passing marks (50)

passing_marks = 50
input_string = input("Enter marks of students seperated by space: ")
marks_list = input_string.split()
pass_count = 0
for i in marks_list:
    if int(i) >= passing_marks:
        pass_count += 1

print("Total number of students that passed: {}".format(pass_count))
print(f"Total number of marks: {len(marks_list)}")
print("Percentage pass rate: {}".format((pass_count/len(marks_list)*100)))

