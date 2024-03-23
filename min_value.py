# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
minimun_score = student_scores[0]
for score in student_scores:
  if score < minimun_score:
    minimun_score = score
print(f"The minimum score in the class is: {minimun_score}")    
