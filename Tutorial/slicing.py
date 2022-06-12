team= ['Seahawks', 2014, 'CenturyLink Field']
nums= [5, 10, 4, 5]
words= ['spam', 'ni']

grades= []
num= float(input('enter the first grade: '))
grades.append(num)
num= float(input('Enter the second grade: '))
grades.append(num)
num= float(input('Enter the third grade: '))
grades.append(num)
num= float(input('Enter the fourth grade: '))
grades.append(num)
num= float(input('Enter the fifth grade: '))
grades.append(num)

minimumGrade= min(grades)
grades.remove(minimumGrade)
minimumGrades= min(grades)
grades.remove(minimumGrades)
average= sum(grades)/len(grades)
print('Average Grade: {0: .2f}'.format(average))
