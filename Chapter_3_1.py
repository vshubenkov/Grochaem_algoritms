import numpy as np

#box_count = int(input('Enter box count: '))
#if box_count <= 1:
#    box_count = int(input('Enter box count more than one: '))

'''Box creation'''
def box_creation(box_count):
    box = []
    main_box = [box]
    while box_count > 0:
        if not main_box[0]:
            main_box[0].append('level 1')
        else:
            pass
        box_count -= 1
    return main_box

def get_array_level(array, level=0):
    if array[0]:
        level = level + get_array_level(array[0], 1)
    else:
        return level

#print(box_creation(box_count))
box_3 = []
box_2 = []
box_1 = [box_2]
box_2 = [box_3]
array = [box_1]
print(get_array_level(array))

