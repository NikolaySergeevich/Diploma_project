import data_frame as wor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import os


def plt_result(us_id):
    N = 15
    df = wor.give_data_frame(us_id)
    print(df)
    r = np.array(wor.give_list_with_value(df))
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = np.array([0.42] * N)
    title2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    color = '#9d54ff'

    lable = ['Экстраверт', 'Интроверт', 'Способность\nк монотонной работе', 'Наставничество', 'Аналитические навыки', 'Эмпатия', 'Любопытство', 
         'Ораторское\nискусство', 'Организаторские\nспособности', 'Критическое мышление', 'Многозадачность', 'Креативность', 'Стрессоустойчивость',
        'Контроль времени', 'Работа с большим\nобъёмом информации']
    plt.figure(figsize=(12,10))
    ax = plt.subplot(111, polar=True)

    plt.text(-1, -1, wor.sum_result(r), size = 30, horizontalalignment='center',
        verticalalignment='center', color = color)
    # --------------------Заполнение окружности по уровням 
    ycoord = 0.45
    for num in 1,2,3,4,5:
        xcoord = 0.20943951
        ygol = -85
        i = 0
        while i != N:
            plt.text(xcoord, ycoord, num, rotation=ygol, size=13, horizontalalignment='center', verticalalignment='center', alpha=0.5)
            xcoord += 0.41887902
            ygol += 24.8
            i += 1
        ycoord +=1
        
    #------------заполнение качеств по окружности
    ycoord = 0.20943951
    for lab in lable:
        xcoord = 6.3
        plt.text(ycoord, xcoord, lab, size=9, horizontalalignment='center', verticalalignment='center', weight='medium', family='serif')
        ycoord += 0.41887902

    ax.set_rlim(0)
    ax.set_rticks(np.arange(1, 6, 1))
    ax.set_rorigin(-1)
    ax.set_thetagrids(theta * 180 / np.pi, title2)
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.grid(color ="black", linewidth=3)


    ax.bar(x=theta, height=r-.0, width=width, bottom=0, alpha=0.8, tick_label=title2, align='edge', color = color)
    # plt.show()
    return plt
# ---------метод сохранения графика на диск
def save_plt_in_disc(plt, user_id):
    plt.savefig('D:/Учёба в GB/Дипломный проект/Diploma_project/Промежуточный тест/result_img/' + str(user_id) +'_result_test.png')

def remove_img(name_img): 
    path = name_img
    try:
        os.remove(path)
    except:
        print('Изображение отсутствует')