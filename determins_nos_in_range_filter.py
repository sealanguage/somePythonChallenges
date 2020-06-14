ages =(4, 5, 7, 3, 4, 7, 8, 5, 8, 5)

def primary_schools ( age ) :
    if 11 >= age >= 5 :
        return True
    else :
        return False
primary_school_age = filter(primary_schools, ages)

for age in primary_school_age :
    print(age)