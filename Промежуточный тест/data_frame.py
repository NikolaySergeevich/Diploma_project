import sqlite3 as sq
import pandas as pd
link = 'D:/Учёба в GB/Дипломный проект/Diploma_project/Промежуточный тест/testDB3.db'
con = sq.connect(link)
# ----метод получение data vrame по user_id
def give_data_frame(us_id):
    return pd.read_sql("SELECT * from value JOIN users ON users.id = value.user_id WHERE us_id = {}".format(us_id), con)
# --------------метод получения списка со результатами теста
def give_list_with_value(df):
    list = []
    for i in df.columns:
        list.append(i)
    list.remove('id')
    list.remove('user_id')
    list.remove('us_id')
    list.remove('imag')
    list_2 = []
    for i in list:
        list_2.append(df[i]. values [0])
    return list_2
# -------метод получения суммы очков
def sum_result(list):
    sum = 0
    for i in list:
        sum += i
    return sum
