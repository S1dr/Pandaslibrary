import pandas as pd
import matplotlib


df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')

print(type(df)) #Класс Dataframe используется для представления двумерных крассов (строки и колонки)

print(df)

newDf = pd.DataFrame.from_dict({'Name': ['Stas' , 'Alex' ] , 'Surname' : ['Sidorenko' , 'Sidorov']}) # создаем Dataframe c помощью словаря. Ключ - название коронки. Словать значение

print(newDf)

#newDF_to... (Функция, которая записывает датафрейм в файл нужного формата.


print(df.info()) # выводит информацию о датаврейме


print(newDf['Name']) # вывод всех значений с колонки имена.

print(df[['Name' , 'Age']].head(3)) # Выборка имени и возраста (первые 3 записи)

print(df.loc[[5,10,15],['Name', 'Age']]) #выборка и имени и возраста одновременно (5 10 15) - индекс строки

print(df.iloc[[5, 10, 15], [0, 1]]) # Выборка по индексу колонки

print(df.columns) # название колонок и порядок

print(df['Age'] > 18) # для каждой строчки проверят правда или нет


print(df[(df['Age'] == 5) | (df['Age'] == 10)]) # соединение двух условий


print(df[df['Age'].notna()]) # Проверка есть ли элемент на этом месте

df['Age'].isna().sum() # Подсчет колличества пропусков по возрасту

print(df.sort_values('Age').head(10)) # сотрировка возраста первые 10 записей


# АНАЛИТИКА

print(df.count())  # посчитается колличество не пустых элементов.

print(df['Age'].describe()) # возвращает сразу несколько статистик


df.groupby('Sex')['Age'].mean() #групировка данных по гендеру и возрасту



print(df['Age'].plot(kind='hist', bins=20)) # построение гистограммы





