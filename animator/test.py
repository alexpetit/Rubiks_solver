from rubik_solver import utils


K_1 =  (0, 0, 1)
K_3 = (0, 2, 1)
K_4 = (1, 0, 1)
K_6 = (1, 2, 1)
K_7 = (2, 0, 1)
K_9 = (2, 2, 1)
K_F1 = (0, 0, -1)
K_F3 = (0, 2, -1)
K_F4 = (1, 0, -1)
K_F6 = (1, 2, -1)
K_F7 = (2, 0, -1)
K_F9 = (2, 2, -1)

cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'

solution = utils.solve(cube, 'Kociemba')

kociemba_output = ["R'", "R", "L'", "L", "D'", "D", "U'", "U", "B'", "B", "F'", "F"]

keypad_code = ["K_1", "K_F1", "K_3", "K_F3", "K_4", "K_F4", "K_6", "K_F6", "K_7", "K_F7", "K_9", "K_F9"]

kociemba_output_double = ["R2", "L2", "D2", "U2", "B2", "F2"]

keypad_code_double = ["K_1", "K_3", "K_4", "K_6", "K_7", "K_9"]

touches_to_press_solve = []

for s in solution:
    if s in kociemba_output:
        index = kociemba_output.index(s)
        touches_to_press_solve.append(keypad_code[index])
    elif s in kociemba_output_double:
        index = kociemba_output_double.index(s)
        touches_to_press_solve.append(keypad_code_double[index])
        touches_to_press_solve.append(keypad_code_double[index])

print(solution)
print(touches_to_press_solve)

reversed_touches = reversed(touches_to_press_solve)

F = ["K_F1", "K_F3", "K_F4", "K_F6", "K_F7", "K_F9"]

result = []

for touch in reversed_touches:
    if touch in F:
        index = F.index(touch)
        result.append(keypad_code_double[index])
    else:
        index = keypad_code_double.index(touch)
        result.append(F[index])

print(result)


