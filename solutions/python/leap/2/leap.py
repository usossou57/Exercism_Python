def leap_year(year):
    condition_1 = year % 4 == 0
    condition_2 = year % 100 == 0
    condition_3 = year % 400 == 0
    condition_4 = condition_2 and condition_3

    if condition_1:
        if condition_2:
            answer = condition_4
        else:
            answer = True
    else:
        answer = False
        
    return answer
