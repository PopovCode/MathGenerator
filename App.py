import random


def save_five(filename, list):
    file = open(filename, 'w')
    for line in list:
        file.write(line + '\n')
    file.close()
    print(f'[INFO] {filename} saved.')

def rand_operand_generator(lower, upper):
    return random.randint(lower, upper)

def calc(a, operand, b):
    if operand == "+":
        return a+b
    elif operand == "-":
        return a-b

def get_random_action(ACTIONS):
    return ACTIONS[random.randint(0, len(ACTIONS) - 1)]

def math_operations(LOWER, UPPER, ACTIONS, AMOUND_TASKS):
    mathTask = []
    mathAnswers = []
    count = 0

    while count < AMOUND_TASKS:
        random_action = get_random_action(ACTIONS)

        a = rand_operand_generator(lower=LOWER, upper=UPPER)
        b = rand_operand_generator(lower=LOWER, upper=UPPER)

        c = calc(a, random_action, b)
        if (c >= 0 and c < UPPER):
            mathTask.append(f"{a} {random_action} {b} = ")
            mathAnswers.append(f"{a} {random_action} {b} = {c}")
            # print(f"[SAVED] {a} {randOperand} {b} = ")
            count = count + 1

    save_five('MathTasks.txt', mathTask)
    save_five('MathAnswers.txt', mathAnswers)

def logical_operations(LOWER, UPPER, AMOUND_TASKS):
    log_operations = []
    count = 0
    while count < AMOUND_TASKS:
        a = rand_operand_generator(lower=LOWER, upper=UPPER)
        b = rand_operand_generator(lower=LOWER, upper=UPPER)
        log_operations.append(f'{a}    {b}')
        count = count + 1

    save_five('LogicalOperations.txt', log_operations)

def main():
    # Нижняя и верхняя границы чисел (в каком пределе умеем считать)
    LOWER_OPERAND = 1
    UPPER_OPERAND = 20

    # Операции с числами
    ACTIONS = ['+', '-']

    # Количество генерируемых задач
    AMOUND_TASKS = 20

    math_operations(LOWER_OPERAND,UPPER_OPERAND, ACTIONS, AMOUND_TASKS)
    logical_operations(LOWER_OPERAND, UPPER_OPERAND, AMOUND_TASKS)

if __name__ == "__main__":
    main()