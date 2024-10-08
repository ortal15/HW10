# start
import random

# a
# פעולת ה TRY נותנת לנו את האופציה לשים הגנה על קטע
# קוד שיכול לגרום לקריסת התוכנית,
# פעולת ה EXCEPT בעצם נותנת לנו את האופציה
# לבחור מה סוג השגיאה ובכך נוכל לזהות ולתקן.

# b
# כדי שבעצם כשאנחנו בונים תוכנית ומכניסים שורה עם
# תנאי שיכול לשבור לנו את התוכנית אז יש לנו את האופציה להכניס את
# השורת קוד בתוכנית לרשת ביטחון עם האפשרות לתקן את השגיאה.

# c
x = None
while True:
    try:
        if x == 88 // 0:
            print(x)
    except ZeroDivisionError:
        print('Zero Division Error...')
        break

print('cannot be divided by 0')

# d
age: float = 0
while True:
    try:
        age = float(input('enter age: '))
        if not 18 <= age <= 25:
            raise ValueError
        break
    except ValueError as str:
        print('ValueError/age not in range..')
        continue
print(f"age is {age}")

# e
list_e: list[int] = [random.randint(1, 100) for i in range(4)]
print('list_e:', list_e)
x = 0
index = 0
while not x == -999:
    try:
        x = int(input('enter a number:'))
        if x != -999:
            index = x
            list_e.append(x)
            list_e.insert(x, index)
            print(f'index of {x} is:{list_e.index(index)}')
            print(list_e)
        else:
            break
    except ValueError as str:
        print('this is not a valid number')
        continue

print('list_e:', list_e)
print('done.')
