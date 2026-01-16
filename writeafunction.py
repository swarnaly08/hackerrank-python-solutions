def is_leap(year):
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, it must also be divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            # Divisible by 4 but not 100
            leap = True
    else:
        # Not divisible by 4
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))