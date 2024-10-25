import math

numbers = []
while True:
    data = input("Exam points and exercises completed:")
    if data != "":
        exam_points, exercises = map(int, data.split())
        numbers.append(
            {"exam_points": exam_points, "exercises": exercises})
    else:
        break

grades = []
total_for_div = 0

for object in numbers:
    current_exam = object['exam_points']
    current_excercises = math.floor(object['exercises'] / 10)
    current_total = current_exam + current_excercises
    total_for_div = total_for_div + current_total

    if current_exam < 10:
        grades.append(0)
    else:
        if current_total <= 14:
            grades.append(0)
        elif current_total <= 17 and current_total >= 15:
            grades.append(1)
        elif current_total <= 20 and current_total >= 18:
            grades.append(2)
        elif current_total <= 23 and current_total >= 21:
            grades.append(3)
        elif current_total <= 27 and current_total >= 24:
            grades.append(4)
        elif current_total <= 30 and current_total >= 30:
            grades.append(5)

average = total_for_div / len(numbers)
fails = grades.count(0)
pass_perc = (len(grades) - fails) / len(grades) * 100

print("Statistics:")
print("Points average: " + str(average))
print("Pass percentage: " + str(round(pass_perc, 1)))
print("Grade distribution: ")
print((" 5: " + "*" * grades.count(5)))
print((" 4: " + "*" * grades.count(4)))
print((" 3: " + "*" * grades.count(3)))
print((" 2: " + "*" * grades.count(2)))
print((" 1: " + "*" * grades.count(1)))
print((" 0: " + "*" * grades.count(0)))
