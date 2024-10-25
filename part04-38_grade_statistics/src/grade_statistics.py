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
    
    for object in stats:
        current_exam = object['exam_points']
        current_excercises = math.floor(object['exercises'] / 10)

        
        print("exam score: " + str(object['exam_points']) + " excercises: " + str(object['exercises']) + "current" +str(current_excercises))


    
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

