def letter_grade(score):
    try:
        if score < 0 or score > 100:
            return "Invalid"
        elif score >= 97:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid"
    
# a. Test the function with the given list below
for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    grade = letter_grade(score)
    print(f"{score:5} -> {grade}")
    
# b. Why must A+ come before A?
#   The A+ condition (score >= 97) must come before the A condition (score >= 90).
#   If you put score >= 90 first, a score of 99 would satisfy that condition and return "A" immediately. 
#   Python would never reach the A+ condition."""
