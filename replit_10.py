# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

num_of_students = 0
sum_heights=0

for height in student_heights:
    sum_heights += height
    num_of_students += 1

avg_height = sum_heights / num_of_students

print("Average height: ", round(avg_height, 2))
