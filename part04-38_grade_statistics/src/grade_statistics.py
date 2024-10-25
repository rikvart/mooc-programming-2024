import math

def input_from_user():
    numbers = []
    while True:
        data = input("Exam points and exercises completed:")
        if data != "":
            exam_points, exercises = map(int, data.split())
            numbers.append({"exam_points": exam_points, "exercises": exercises})
        else:
            break

        
    return numbers

def statistics(stats: list):

    divide = len(stats)
    grades = []
    total_for_div = 0
    
    for object in stats:
        current_exam = object['exam_points']
        current_excercises = math.floor(object['exercises'] / 10)
        current_total = current_exam + current_excercises
        total_for_div = total_for_div + current_total

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

    


        
        print("exam score: " + str(object['exam_points']) + " excercises: " + str(object['exercises']) + "current" +str(current_excercises))

    print(grades)

    
    return stats

if __name__ == "__main__":

    print(statistics(input_from_user()))



# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point
# 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. 
# The number of exercise points granted is an integer value, rounded down.
# Statistics:
#Points average: 14.5
#Pass percentage: 75.0
#Grade distribution:
#  5:
#  4:
#  3: *
#  2:
#  1: **
#  0: *

