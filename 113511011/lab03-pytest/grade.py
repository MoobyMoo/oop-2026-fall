def letter_grade(score):

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    #put your code here

    if score <= 100 and score >= 90:
        return "A"

    if score <= 89 and score >= 80:
        return "B"

    if score <= 79 and score >= 70:
        return "C"

    if score <= 69 and score >= 60:
        return "D"
    
    if score <= 59 and score >= 0:
        return "F"

    
    #put your code here
def average(scores):
    if len(scores) == 0:
        raise ValueError("scores cannot be empty")

    return sum(scores) / len(scores)