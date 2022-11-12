import excep
import main
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (ContextTypes)

from datetime import datetime as dt


reply_keyboard_repeat_bot = [["Калькулятор"],\
                            ["Вывод логов"],\
                            ["Выход"]]
markup_repeat = ReplyKeyboardMarkup(reply_keyboard_repeat_bot, one_time_keyboard=True) 



def universal_logger(data, data_description = "действие"):
    """Функция логинит любые данные
    при вызове функциив в data_description подставляется строковое описание
    действия(например, 'ввод значения а', 'ввод значения в'), который 
    сопровождает появление переменной data) 
    """  
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('log_calc.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data))
                    
async def print_log (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    with open('log_calc.csv', 'r', encoding='utf-8') as file:
        for line in file:
            await update.message.reply_text (line, end='')
    await update.message.reply_text ('Хотите выполнить новую операцию?\n\
 1 - Да\n\
 2 - Нет', reply_markup=markup_repeat)
    answer = excep.check_menu(3)
    if answer == 1:
        return main.main_menu
    else:
        return main.end_prog