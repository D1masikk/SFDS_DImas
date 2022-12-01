import numpy as np
def random_predict(number: int=1)->int: # задается функция с аргументом number = 1
    count = 0 # счетчик попыток для угадывания числа
   
    while True:
       count+=1 # при каждой итерации цикла счетчик попыток будет увеличиваться на 1
       predict_number = np.random.randint(1,101) # задаем рандомное число
       if number == predict_number: # если оно = number, цикл заканчивается
           break
    return(count) # передаем значение количества попыток при выводе функции
print(f'Количество попыток {random_predict()}')

def score_game(random_predict) -> int: # создаем функцию с аргументом количества попыток для угадывания числа алгоритмом
    count_Is=[] # список для сохранения количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000)) # загадали список чисел
    
    for number in random_array:
        count_Is.append(random_predict(number)) # добавляем в список поочередно количество попыток для угадывания каждого числа из списка random_array
        
    score = int(np.mean(count_Is))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)    
