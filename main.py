from random import randint
import math

# Fill a group with random objects of a given list of elements.
def fill_group(groups, group_index, elements, groups_size, difference):
    while (len(groups[group_index]) < (groups_size + difference)) and (len(elements) > 0):
        random_element = randint(0, len(elements) - 1)
        groups[group_index].append(elements[random_element])
        del elements[random_element]

# Distribute the elements of a list into groups.
def distribute_elements(elements, groups_size, groups_max = float('inf')):
    groups_max = int(len(elements) / size) if groups_max == float('inf') else groups_max
    groups = [] # Store the elements in groups.

    # Generate groups of elements while all elements are placed in a group.
    while len(elements) > 0:
        groups_quantity = len(groups)
        exceeds_groups_max = groups_quantity >= groups_max

        # Distribute elements in the current group.
        if not exceeds_groups_max:
            groups.append([])
            fill_group(groups, groups_quantity, elements, groups_size, 0)
            groups_quantity += 1
        else:
            for i in range(len(elements)):
                random_group = randint(0, groups_quantity - 1)

                while len(groups[random_group]) >= groups_size + 1:
                    random_group = randint(0, groups_quantity - 1)

                fill_group(groups, random_group, elements, groups_size, 1)

    return groups

def print_list(element_list, list_name):
    greater_than_one = True if len(element_list) > 1 else False
    space = "     " if greater_than_one else ""
    new_line = "\n" if greater_than_one else ""
    s = "s" if greater_than_one else ""

    elements_count = 1
    print(f'  - {list_name}{s}: {new_line}', end=new_line)
    for value in element_list:    
        print(f'{space}{elements_count}.', value, end = '')
        elements_count += 1

# Request and store the quantity of groups.
print('N° estudiantes por grupo (auto): ', end = '')
size = input()

if len(size) == 0:
  size = "auto"

print('URL de archivo de estudiantes (students.txt): ', end = '')
students_url = str(input())

if len(students_url) == 0:
  students_url = "students.txt" 

print('URL de archivo de temas (topics.txt): ', end = '')
topics_url = str(input())

if len(topics_url) == 0:
  topics_url = "topics.txt" 


# Get the list of students.
with open(students_url) as f:
    students = f.readlines()

# Get the list of topics.
with open(topics_url) as f:
    topics = f.readlines()

# Distribute student in groups.
size = int(size) if size.lower() != "auto" else (len(students)/len(topics))
student_groups = distribute_elements(students, size)

# Distribute topics in student groups.
topics_groups_size = int(len(topics) / len(student_groups))
topics_groups_max = len(student_groups)

topic_groups = distribute_elements(topics, topics_groups_size, topics_groups_max)

# Print the result
print('')
count = 0
for i in range(len(student_groups)):
    print(f'Grupo {count + 1}:  | No. Estudiantes: {len(student_groups[i])} | No. Temas: {len(topic_groups[i])}\n---')

    print_list(student_groups[i], "Estudiante")

    print('')
    
    print_list(topic_groups[i], "Tema")

    print('')

    count += 1
