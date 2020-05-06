from random import randint
import math

def fill_group(elements_groups, current, difference, placed_elements, elements, groups_size):
    elements_quantity = len(elements)

    # Add students to the new or current group.
    while len(elements_groups[current]) < (groups_size + difference):
        student_is_located = True
        all_students_are_placed = len(placed_elements) >= elements_quantity

        while(student_is_located and not all_students_are_placed):
            random_student = randint(0, elements_quantity - 1)

            # Know if this selected student is placed in a group or not.
            if placed_elements.get(random_student) == None:
                student_is_located = False
                placed_elements[random_student] = True
                elements_groups[current][random_student] = elements[random_student]
                break
            else:
                student_is_located = True

def distribute_elements(elements, groups_size, groups_max = float('inf')):
    elements_groups = []

    difference = 0 # The amount of extra elements a group will have.
    elements_quantity = len(elements)

    # Generate groups of elements.
    placed_elements = {}
    while len(placed_elements) < elements_quantity:
        # Create a new group of elements.
        unplaced_elements = elements_quantity - len(placed_elements) 
        enough_to_create_new_group =  unplaced_elements >= groups_size
        exceeds_groups_max = len(elements_groups) >= groups_max

        current = len(elements_groups) - 1

        if enough_to_create_new_group and not exceeds_groups_max:
            elements_groups.append({})
            current += 1
            fill_group(elements_groups, current, 0, placed_elements, elements, groups_size)    
        else:
            difference = 0
            
            for i in range(unplaced_elements):
                random_group = randint(0, current)
                fill_group(elements_groups, random_group, 1, placed_elements, elements, groups_size)    

            break

    return elements_groups

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
    
