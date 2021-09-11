
def classify_triangle(a,b,c):

    if a == b == c:
        return  'Equilateral'
    elif a**2 + b**2 == c**2:
        return 'Right'
    elif a == b != c or a != b == c or a == c != b:
        return 'Isosceles'
    else:
        return 'Scalene'

print(classify_triangle(3,4,5))
