count = 0
sum_of_marks_obtained = 0
total = 500
while count < 5:
    count += 1
    marks_obtained = int(input())
    sum_of_marks_obtained += marks_obtained
    if sum_of_marks_obtained >= 500:
        break
    else:
        continue

percentage = (sum_of_marks_obtained / total)*100

print(sum_of_marks_obtained)
