tasks_count = 12
duration = 1.5
course_name = "Python"
duration_per_one = round(duration / tasks_count, 3)

print('Курс: ' + course_name + ', всего задач: ' + str(tasks_count) + ', затрачено часов: ' + str(duration) + ', среднее время выполнения ' + str(duration_per_one) + ' часа.')

print(f'Курс: {course_name}, всего задач: {tasks_count}, затрачено часов: {duration}, среднее время выполнения {duration_per_one} часа.')
