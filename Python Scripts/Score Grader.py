print("Hi! Let me help you with grading your score")
marks = input('enter your score\n')
try:
    score = int(marks)
    if score >= 100:
        print ('Please, input within the range of 1 - 100')
    else:
        if score >= 70:
            print ('Congratulations! You had an A!')        
        elif score >= 60:
            print ('Congratulations! You had a B!')
        elif score >= 50:
            print ('Nice try! You had a C!')
        elif score >= 45:
            print ('Better luck next time, You had a D!')
        elif score < 45:
            print ('I am sorry, you had an F!')
except:
    print ('Please, input a correct option')