class Students:
    def __init__(self, name, number_group, academic_performance):
        self.name = name
        self.number_group = number_group
        self.academic_performance = academic_performance

def print_result(student):
    print('Имя студента: {name_student}\n'
          'Группа: {group_student}\n'
          'Средний балл: {score_student}\n'
          .format(name_student=student.name,
                  group_student=student.number_group,
                  score_student=student.academic_performance))

def sorted_list(start_list):
    end_list = []
    for i_student in start_list:
        if end_list == []:
            end_list.append(i_student)
        else:
            swith = 1
            reserve_list = end_list
            end_list = []
            for i_score in reserve_list:
                if i_student.academic_performance < i_score.academic_performance:
                    end_list.append(i_score)
                else:
                    if swith == 1:
                        end_list.append(i_student)
                        end_list.append(i_score)
                        swith = 0
                    else:
                        end_list.append(i_score)

    return end_list


students_list = []

with open('students.txt', 'r') as file:
    count_students = 0

    for i in file.readlines():
        i = i.split()
        count_students += 1
        students_list.append('student_{}'.format(count_students))
        name_student = i[0] + ' ' + i[1]
        summ = 0

        for i_number in i[3:]:
            for i_sym in i_number:
                if i_sym.isdigit():
                    summ += int(i_sym)
        score = summ / 5

        students_list[count_students - 1] = Students(name_student, i[2], score)

new_list = sorted_list(students_list)

for i_student in new_list:
        print_result(i_student)









