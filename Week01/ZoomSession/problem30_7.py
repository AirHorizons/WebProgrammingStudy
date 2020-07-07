korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    min_score = None
    max_score = None
    for score in args:
        if min_score is None:
            min_score = score
            max_score = score
        elif score < min_score:
            min_score = score
        elif score > max_score:
            max_score = score
    return min_score, max_score
    
def get_average(**kwargs):
    total = 0.0
    subjectnum = 0
    for key, value in kwargs.items():
        total += value
        subjectnum += 1
    return total/subjectnum

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
