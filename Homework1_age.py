age = int(input('How old are you? ')) #Получилось 
duties = age

def duties(age):
    if age <= 2:
        return "a newly born child"
    elif 2 <= age <= 6:
        return "kindergarden child"
    elif 7 <= age <= 18:
        return "school teenager"
    elif 19 <= age <= 23:
        return "university student"
    elif 24 <= age <= 70:
        return "worker"
    elif 71 <= age <= 171:
        return "pensioner"
    

print(duties(age))