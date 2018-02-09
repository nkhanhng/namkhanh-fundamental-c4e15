from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    quiz_list = []
    pick_color = choice(["RED","BLUE","GREEN","YELLOW"])
    hex_color = choice(["#3F51B5",'#C62828','#FFD600','#4CAF50'])

    quiz_list.append(pick_color)
    quiz_list.append(hex_color)
    quiz_list.append(randint(0,1))
    return quiz_list
    # return [
    #             'RED',
    #             '#4CAF50',
    #             randint(0, 1) # 0 : meaning, 1: color
    #         ]

def mouse_press(x, y, text, color, quiz_type):
    print(x, y, text, color, quiz_type)
    quiz_list = generate_quiz()
    print(quiz_list)
    if color == quiz_list[0]:
        return True
    else:
        return False
