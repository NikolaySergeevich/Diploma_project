import sqlite3 as sq

link = 'D:/Учёба в GB/Дипломный проект/Diploma_project/Промежуточный тест/testDB3.db'
with sq.connect(link) as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        us_id INTEGER,
        imag TEXT
        )""")
with sq.connect(link) as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS value(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id) ON UPDATE CASCADE,
        extrovert INTEGER DEFAULT 0,
        Introvert INTEGER DEFAULT 0,
        Ability_for_monotonous_work INTEGER DEFAULT 0,
        Mentoring INTEGER DEFAULT 0,
        Analytical_Skills INTEGER DEFAULT 0,
        Empathy INTEGER DEFAULT 0,
        Curiosity INTEGER DEFAULT 0,
        Oratory_art INTEGER DEFAULT 0,
        Organizational_ability INTEGER DEFAULT 0,
        Critical_Thinking INTEGER DEFAULT 0,
        Multitasking INTEGER DEFAULT 0,
        Creativity INTEGER DEFAULT 0,
        Stress_resistance INTEGER DEFAULT 0,
        Time_control INTEGER DEFAULT 0,
        Working_with_a_large_volume_of_information INTEGER DEFAULT 0
        )""")
# --------метод загрузки ссылки изображения в БД
def saved_img_in_db(us_id):
    linki = 'D:/Учёба в GB/Дипломный проект/Diploma_project/Промежуточный тест/result_img/' + str(us_id) +'_result_test.png'
    with sq.connect(link) as con:
        cur = con.cursor()
        cur.execute(f"UPDATE users SET imag = '{linki}' WHERE us_id = '{us_id}'")
# -------метод, который даёт ссылку картинки по user_id
def giv_link_img_from_db(us_id):
    with sq.connect(link) as con:
        cur = con.cursor()
        cur.execute(f"SELECT imag FROM users WHERE us_id = '{us_id}'")
        res = ""
        for i in cur:
            res = i[0]
    return res