import input_n
import log
import excep
import summ
import sub
import mult
import div

from time import sleep
import logging
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
 
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(f"This example is not compatible with your current PTB version {TG_VER}. To view the "\
        f"{TG_VER} version of this bot, "\
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)



reply_keyboard_start = [["Калькулятор"],\
                  ["Вывод логов"],\
                  ["Выход"]]

reply_keyboard_choice_num = [["Целые"],\
                            ["Вещественные"],\
                            ["Комплексные"],\
                            ["Главное меню"],\
                            ["Выход"]]

reply_keyboard_action = [["Сумма"],\
                        ["Вычитание"],\
                        ["Умножение"],\
                        ["Деление"],\
                        ["Целочисленное деление"],\
                        ["Остаток от деления"],\
                        ["Главное меню"],\
                        ["Выход"]]

reply_keyboard_action_comp = [["Сумма"],\
                            ["Вычитание"],\
                            ["Умножение"],\
                            ["Деление"],\
                            ["Главное меню"],\
                            ["Выход"]]

reply_keyboard_next_action = [["Продожить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]

markup_start = ReplyKeyboardMarkup(reply_keyboard_start, one_time_keyboard=True)
markup_choice_num = ReplyKeyboardMarkup(reply_keyboard_choice_num, one_time_keyboard=True)
markup_action = ReplyKeyboardMarkup(reply_keyboard_action, one_time_keyboard=True)
markup_action_comp = ReplyKeyboardMarkup(reply_keyboard_action_comp, one_time_keyboard=True)
markup_next_action = ReplyKeyboardMarkup(reply_keyboard_next_action, one_time_keyboard=True)


main_menu, numbers_menu, action_menu, next_action, res_action, print_log, end_prog = range(7)


type_menu_1 = 0
type_menu_2 = 0
type_menu_3 = 0
type_menu_4 = 0
answer = 1

async def main_m (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text ('Выберите пункт меню\n\
1 - Калькулятор\n 2 - Вывод логов на экран\n 3 - Выход', reply_markup=markup_start)
    global type_menu_1
    type_menu_1 = excep.check_menu(4)
    if type_menu_1 == 1:
        log.universal_logger("Калькулятор", data_description = "Запуск")
        return numbers_menu
    elif type_menu_1 == 2:
        log.universal_logger("Вывод логов на экран", data_description = "Запуск")
        return print_log
    else:
        return end_prog



async def choice_num (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text ('С какими числами будем работать?\n \
1 - Целые\n 2 - Вещественные\n 3 - Комплексные\n 4 - Главное меню\n 5 - Выход',\
    reply_markup=markup_choice_num)
    global type_menu_2
    type_menu_2 = excep.check_menu(6)
    if type_menu_2 == 1:
        log.universal_logger("Целые числа", data_description = "Выбор")
        return input_n.int_num()
    elif type_menu_2 == 2:
        log.universal_logger("Вещественные числа", data_description = "Выбор")
        return input_n.float_num()
    elif type_menu_2 == 3:
        log.universal_logger("Комплексные числа", data_description = "Выбор")
        return input_n.complex_num()
    elif type_menu_2 == 4:
        log.universal_logger("Главное меню", data_description = "Возврат")
        return main_menu
    else:
        return end_prog


async def choice_action (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if type(input_n.x)==complex or type(input_n.y)==complex:
        await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{input_n.x}" и "{input_n.y}"?\n\
1 - Сумма\n 2 - Вычитание\n 3 - Умножение\n 4 - Деление\n\
5 - Главное меню\n 6 - Назад \n 7 - Выход',\
reply_markup=markup_action_comp)
    else:
        await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{input_n.x}" и "{input_n.y}"?\n\
1 - Сумма\n 2 - Вычитание\n 3 - Умножение\n 4 - Деление\n\
5 - Целочисленное деление\n 6 - Остаток от деления\n 7 - Главное меню\n 8 - Назад\
\n 9 - Выход', reply_markup=markup_action)
    global type_menu_3
    if type_menu_2 == 3:
        type_menu_3 = excep.check_menu(8)
    else:
        type_menu_3 = excep.check_menu(10)
    if type_menu_3 in range(1,4) or excep.excep_check_zero() is True:
        return res_action
    else:
        return excep.if_zero

async def res_act(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if type_menu_3 == 1:
        result = summ.summ
    elif type_menu_3 == 2:
        result = sub.sub
    elif type_menu_3 == 3:    
        result = mult.mult
    elif type_menu_3 == 4:
        result = div.float_div
    elif type_menu_3 == 5:    
        if type_menu_2 != 3:
            result = div.floor_div
        else:
            log.universal_logger("Главное меню", data_description = "Возврат")
            return main_menu
    elif type_menu_3 == 6:
        if type_menu_2 != 3:
            result = div.mod_div()
        else:
            log.universal_logger('Меню ввода данных', data_description = "Повторный ввод")
            return numbers_menu
    elif type_menu_3 == 7:      
        if type_menu_2 != 3:
            log.universal_logger("Главное меню", data_description = "Возврат")
            return main_menu
        else:
            return end_prog
    elif type_menu_3 == 8:      
        log.universal_logger('Меню ввода данных', data_description = "Повторный ввод")
        return numbers_menu
    else:
        return end_prog
    await update.message.reply_text(f'{action(type_menu_3)} чисел {input_n.x} и {input_n.y} составляет {result}')



async def next_act(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(f'Продолжить вычисления с числами "{input_n.x}" и "{input_n.y}"?\n \
1 - Продожить\n 2 - Новый ввод\n 3 - Главное меню\n 4 - Выход',\
 reply_markup=markup_next_action)
    global type_menu_4
    type_menu_4 = excep.check_menu(5)
    if type_menu_4 == 1:
        log.universal_logger((input_n.x, input_n.y), data_description = "Продолжить вычисления")
        return action_menu
    elif type_menu_4 == 2:
        log.universal_logger('Меню ввода данных', data_description = "Повторный ввод")
        return numbers_menu
    elif type_menu_4 == 3:
        log.universal_logger("Главное меню", data_description = "Возврат")
        return main_menu
    else:
        return end_prog


def action (ent_menu):
    if type_menu_2 == 3:
        action = {1: "Сумма", 2: "Разность", 3: "Произведение", 4: "Частное"}
    else:
        action = {1: "Сумма", 2: "Разность", 3: "Произведение", 4: "Частное",
                  5: "Частное от целочисленного деления", 6: "Остаток от деления"}
    return action.get(ent_menu)
    
    
async def ending (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    log.universal_logger("по команде пользователя", data_description = "Выход") 
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]
    await update.message.reply_text(f"Выполнение программы завершено! Спасибо!", reply_markup=ReplyKeyboardRemove())
    clear_data()
    user_data.clear()
    return ConversationHandler.END


def clear_data():
    global type_menu_1
    type_menu_1 = 0
    global type_menu_2
    type_menu_2 = 0
    global type_menu_3
    type_menu_3 = 0
    global type_menu_4
    type_menu_4 = 0
    global answer
    answer = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.universal_logger("Вход в программу", data_description = "Запуск")
    await update.message.reply_text('Добро пожаловать в программу-калькулятор🔥')
    sleep(1)
    await update.message.reply_text('Для начала работы выбери пункт меню:'),
    return main_menu




def main() -> None:
    application = Application.builder().token("5700119796:AAGgdI8yBQOzkBCRKkAhz4DpxBH6FNxMRFUсду").build()
    conv_handler = ConversationHandler\
        \
        (entry_points=[CommandHandler("start", start)],\
        \
        states={main_menu: [MessageHandler(filters.Regex("^(1|2|3|)$"), main_m)],\
                print_log: [MessageHandler(filters.TEXT & ~(filters.COMMAND), log.print_log)],\
                numbers_menu: [MessageHandler(filters.TEXT & ~(filters.COMMAND), choice_num)],\
                action_menu: [MessageHandler(filters.TEXT & ~(filters.COMMAND), choice_action)],\
                res_action: [MessageHandler(filters.Regex("^Новая игра$"), res_act)],\
                next_action: [MessageHandler(filters.Regex("^(1|2|3|)$"), next_act)],\
                end_prog: [MessageHandler(filters.Regex("^(1|2|3|)$"), ending)]},\
                
        fallbacks=[MessageHandler(filters.Regex("^Выход$"), ending)])
 
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()