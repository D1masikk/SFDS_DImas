"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def random_predict(number: int=1) -> int:  
    """Угазываем число за количество попыток не более 7

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 100
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if predict_number > number:
            max = predict_number
            predict_number = max - (max - min)//1.25 
        if predict_number < number:
            min = predict_number
            predict_number = min + (max - min)//1.25 
        if predict_number == number:
            break
        
    return(count)


def score_game(random_predict) -> int:
    Count_Is = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        Count_Is.append(random_predict(number))
        score = int(np.mean(Count_Is))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return(score)


if __name__ == "__main__":
    score_game(random_predict)    

    