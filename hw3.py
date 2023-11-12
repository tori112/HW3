import numpy as np
def binary_predict(number:int=1) -> int:
    """Угадываем число с помощью алгоритма бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = (low + high) // 2 # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            low = predict_number + 1
        else:
            high = predict_number - 1
    return(count)
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
#Затем можно вызвать функцию score_game() с новой функцией binary_predict():
score_game(binary_predict)