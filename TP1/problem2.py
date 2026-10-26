total_seconds = 9875

# a. Compute hours, minutes and seconds, then print the sentence show below.
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} = {hours} h {minutes} min {seconds} s")

# b. Rebuild the total from the three parts and print whether it equals total_seconds
print(f"Check: {hours * 3600 + minutes * 60 + seconds == total_seconds} ")

print("=" * 40)
# c. Test your code with 3600, 59 and 86399 seconds
for total_sec in [3600, 59, 86399]:
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    seconds = total_sec % 60
    
    print(f"{total_sec} = {hours} h {minutes} min {seconds} s")
    
    print(f"Check: {hours * 3600 + minutes * 60 + seconds == total_sec} ")
print("=" * 40)
