grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students)
students_list.sort()
avg_grades = [sum(x)/len(x) for x in grades]
print(dict(zip(students_list, avg_grades)))