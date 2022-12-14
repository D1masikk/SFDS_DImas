# SFDS_DImas
SF homework
# [**Проект 0. Угадай число**](https://github.com/D1masikk/SFDS_DImas/blob/main/game_v3.py)

## *Оглавление*  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### *Описание проекта*    
Угадать загаданное компьютером число за минимальное число попыток.




### *Какой кейс решаем?*    
Нужно написать программу, которая угадывает число за минимальное число попыток(20)

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### *Краткая информация о данных*
Сначала пишем функцию random_predict, которая угадывает число и возвращает количество попыток
После пишем функцию score_game, которая возвращает среднее количество попыток из 1000 подходов
  



### *Этапы работы над проектом*
В первой функции `random_predict` компьютер перебирает все числа от 0 до 100 в цикле 
```Python
while True:     
        count+=1
        predict_number = np.random.randint(1, 101)
```
Для снижения количества попыток компьютер после неудачи должен перебирать числа не в диапазоне от 0 до 100, а в диапазоне, приближающего его к загадонному числу:
```Python
if predict_number > number:
            max = predict_number
            predict_number = max - (max - min)//1.25 
        if predict_number < number:
            min = predict_number
            predict_number = min + (max - min)//1.25 
        if predict_number == number:
            break
```
Суть функции `score_game` заключается в следующем. Нужно создать список из 1000 случайных чисел от 0 до 100
```Python
random_array = np.random.randint(1, 101, size = (1000))
```
Затем, создать пустой список, для добавления туда количества попыток угадывания для каждого числа
```Python
Count_Is = []
```
После, каждое из этих чисел закидывается в аргумент функции `random_predict`, где `number`, аргумент этой функции.
Результат функции добавляется в созданный нами пустой список
```Python
for number in random_array:                              
        Count_Is.append(random_predict(number))

```
Функция `score_game` возвращает среднее арифметическое всех числе в этом списке
```Python
score = int(np.mean(Count_Is))
return(score)
```








### *Результаты:*  
```Python
score_game(random_predict)
```
Ваш алгоритм угадывает число в среднем за: 17 попыток




### *Выводы:*  
  Для оптимизации программы, то есть уменьшения среднего количества попыток угадывания числа, необходимо написать алгоритм,
  в результате котрого, после каждой неудачной попытки компютер должен уменьшать диапазон для потенциально загаданного числа




Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
