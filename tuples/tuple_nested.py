student = ("Rajiu", 21, (85, 90, 92))
print(student)

scores = student[2]
print(scores)
second_scores = student[2][1]
print(second_scores)

class_data = (("Math", 78), ("Science", 88))
for subject, score in class_data:
    print(subject, score)
