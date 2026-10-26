name = "Vin Sovichhay"
age = 19
major = "Data Science"
gpa = 3.5
is_scholar = True

# a. Print a profile card exactly like the one below. The GPA must always show 2 decimals (hint: f"{gpa: 2f})
print("=" * 30)
print(f"Name:   {name}")
print(f"Age:    {age}")
print(f"Major:  {major}")
print(f"GPA:  {gpa:.2f}")
print(f"Scholar:  {is_scholar}")

# b.  Below the card, print every value followed by the name of its type, using type(value).__name__.
print("=" * 30)
print(f"'{name}'  -> {type(name).__name__}")
print(f"{age}  -> {type(age).__name__}")
print(f"{major}  -> {type(major).__name__}")
print(f"{gpa}  -> {type(gpa).__name__}")
print(f"{is_scholar}  -> {type(is_scholar).__name__}")

# c. Re-assign age = "20" and print type(age) again. What does this tell you about dynamic typing?
age = "20"
print("=" * 30)
print(f"{age}   -> {type(age).__name__}")
