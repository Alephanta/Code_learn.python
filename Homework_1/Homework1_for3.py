school = [
    {'school_class': '1a', 'scores': [5,5,4,4,3,3,2,2]},
    {'school_class': '2b', 'scores': [3,2,4,5,5,3,3,3,4,4,4]},
    {'school_class': '3c', 'scores': [2,2,2,2,5,5,5,5,4,4,4,3,3]},
]

sum_scores = 0
count = 0
for school_class in school:
    scores = school_class['scores']
    for number in scores:
        sum_scores = sum_scores + number
        count = count + 1

print(sum_scores) 
print(count)
print(f"average score: {sum_scores/(count)}")

for school_class in school:
    scores = school_class.get('scores')
    sum_scores = 0
    count = 0
    for number in scores:
        sum_scores = sum_scores + number
        count = count + 1
    print(school_class.get("school_class"))
    print(f"average score: {sum_scores/(count)}")