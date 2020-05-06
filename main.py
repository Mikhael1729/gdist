from random import randint
import math

def fill_group(groups, current, difference, placed_elements, elements, groups_size):
    elements_quantity = len(elements)

    # Add students to the new or current group.
    while len(groups[current]) < (groups_size + difference):
        student_is_located = True
        all_students_are_placed = len(placed_elements) >= elements_quantity

        while(student_is_located and not all_students_are_placed):
            random_student = randint(0, elements_quantity - 1)

            # Know if this selected student is placed in a group or not.
            if placed_elements.get(random_student) == None:
                student_is_located = False
                placed_elements[random_student] = True
                groups[current][random_student] = elements[random_student]
                break
            else:
                student_is_located = True

def distribute_elements(elements, groups_size, groups_max = float('inf')):
    groups = [] # Store the elements in groups.
    placed_elements = {} # It's used to know if an element is placed or not yet.
    elements_quantity = len(elements)

    # Generate groups of elements while all elements are placed in a group.
    while len(placed_elements) < elements_quantity:
        unplaced_elements = elements_quantity - len(placed_elements) # Knows the placed elements in the randomly groups distribution
        enough_to_create_new_group =  unplaced_elements >= groups_size
        exceeds_groups_max = len(groups) >= groups_max

        current = len(groups) - 1

        if enough_to_create_new_group and not exceeds_groups_max:
            groups.append({})
            current += 1
            fill_group(groups, current, 0, placed_elements, elements, groups_size)
        else:
            for i in range(unplaced_elements):
                random_group = randint(0, current)
                fill_group(groups, random_group, 1, placed_elements, elements, groups_size)

            break

    return groups

# Request and store the quantity of groups.
print('N° estudiantes por grupo: ', end = '')
size = int(input())

print('URL de archivo de estudiantes: ', end = '')
students_url = str(input())

print('URL de archivo de temas: ', end = '')
topics_url = str(input())

# Get the list of students.
with open(students_url) as f:
    students = f.readlines()

# Get the list of topics.
with open(topics_url) as f:
    topics = f.readlines()

# Compute groups.
students_groups = distribute_elements(students, size)
topic_groups = distribute_elements(topics, int(len(topics) / len(students_groups)), len(students_groups))

count = 0
for i in range(len(students_groups)):
    print(f'Grupo {count + 1}:')

    print('  - Estudiantes')
    for key, value in students_groups[i].items():
        print('    - ', value, end = '')

    print('  - Temas')
    for key, value in topic_groups[i].items():
        print('    - ', value, end = '')

    count += 1

    print('')

