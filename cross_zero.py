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
 
list_res = [1,2,3,4,5,6,7,8,9]
fields = [1,2,3,4,5,6,7,8,9]
count_steps = 1

new_steps, naming_1, naming_2, repeating = range(4)


reply_keyboard = [["1", "2", "3"],\
                  ["4", "5", "6"],\
                  ["7", "8", "9"],\
                  ["Выход"],\
                  ["Начать сначала"]]


reply_keyboard_end = [["Выход"],\
                     ["Новая игра"]]


markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup_end = ReplyKeyboardMarkup(reply_keyboard_end, one_time_keyboard=True)


def check_end(list_res):
    check_status = 0
    for i in range (9):
        if list_res[i] in range (1,10):
            check_status+=1
    if check_status>0:
        return 0
    else:
        return 1


def check_win(list_res):
    if list_res[0] == list_res[1] == list_res[2] or\
       list_res[3] == list_res[4] == list_res[5] or\
       list_res[6] == list_res[7] == list_res[8] or\
       list_res[0] == list_res[3] == list_res[6] or\
       list_res[1] == list_res[4] == list_res[7] or\
       list_res[2] == list_res[5] == list_res[8] or\
       list_res[0] == list_res[4] == list_res[8] or\
       list_res[2] == list_res[4] == list_res[6]:
        return 0
    else:
        return 1
 
 
def clear_data():
    for i in range (9):
        list_res[i] = fields[i] = i+1
    global count_steps
    count_steps = 1


def print_board() -> None:
    global  list_res
    global fields
    for i in range (0,9):
        if list_res[i] in range(10):
            fields[i] = '  ' + str(list_res[i]) + ' '
        else:
            fields[i] = list_res[i]
    return f'\
о-----о-----о-----о\n\
| {fields[0]} | {fields[1]} | {fields[2]} |\n\
о-----+-----+-----о\n\
| {fields[3]} | {fields[4]} | {fields[5]} |\n\
о-----+-----+-----о\n\
| {fields[6]} | {fields[7]} | {fields[8]} |\n\
о-----о-----о-----о'


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ввод крестиков и ноликов"""
    step = int(update.message.text)
    context.user_data["choice"] = step
    global count_steps
    if count_steps%2 != 0:
        figure = '❌'
        player_name = name_2
        next_fig = '⭕'
    else:
        figure = '⭕'
        player_name = name_1
        next_fig = '❌'
    if count_steps < 9:
        if list_res[step-1] not in range(1,10):
            await update.message.reply_text (f"Поле занято! Выберите другое поле!", reply_markup=markup)
            return new_steps
        else:
            list_res[step-1] = figure
        if check_win(list_res):
            await update.message.reply_text(\
f"{print_board()}\n{player_name}, выбирай поле для {next_fig}",\
            reply_markup=markup)
            count_steps+=1
            return new_steps
        else:
            await update.message.reply_text(f"{print_board()}", reply_markup=markup_end)
            if count_steps%2 != 0:
                await update.message.reply_text (f"ПОЗДРАВЛЯЮ! {name_1} ВЫИГРАЛ(А)!", reply_markup=markup_end)
            else:
                await update.message.reply_text (f"ПОЗДРАВЛЯЮ! {name_2} ВЫИГРАЛ(А)!", reply_markup=markup_end)
            return repeating
    else:
        list_res[step-1] = figure
        if check_win(list_res):
            await update.message.reply_text (f"{print_board()}\n ИГРА ОКОНЧЕНА! НИЧЬЯ!", reply_markup=markup_end)
        else:
            await update.message.reply_text (f"{print_board()}\nПОЗДРАВЛЯЮ! {name_1} ВЫИГРАЛ(А)!", reply_markup=markup_end)
        return repeating 
 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Добро пожаловать в игру 🔥"Крестики-нолики"🔥\n\
Вначале давайте познакомимся!')
    sleep(1)
    await update.message.reply_text('Введите имя первого игрока'),
    return naming_1


async def namer_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global name_1
    name_1 = update.message.text
    await update.message.reply_text(f'Приятно познакомиться, {name_1}!\nТы будешь играть ❌')
    sleep(1)
    await update.message.reply_text('Введите имя второго игрока')
    return naming_2


async def namer_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    global name_2
    name_2 = update.message.text
    if name_2 == name_1:
        await update.message.reply_text(f'Имена не должны совпадать! Введите заново!')
        return naming_2
    else:
        await update.message.reply_text(f'Великолепно!\nПриятно познакомиться, {name_2}!\nТы будешь играть ⭕')
        sleep(1)
        await update.message.reply_text('А теперь...')
        sleep(1)
        await update.message.reply_text('... начнем игру!🔥')
        sleep(1)
        await update.message.reply_text(f'{name_1}, жамкай на цифру, где будет стоять первый ❌\n\
{print_board()}', reply_markup=markup)
        return new_steps


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]
    await update.message.reply_text(f"Результат игры\n{print_board()}\n\
Отлично поиграли! Приходите еще!", reply_markup=ReplyKeyboardRemove())
    clear_data()
    user_data.clear()
    return ConversationHandler.END


async def repeat_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"] 
    await update.message.reply_text('Наша песня хороша, начинай сначала!🔥')
    clear_data()
    sleep(1)
    await update.message.reply_text('Введите имя первого игрока'),
    user_data.clear()
    return naming_1


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"] 
    clear_data()
    await update.message.reply_text('Введите имя первого игрока'),
    user_data.clear()
    return naming_1


def main() -> None:
    application = Application.builder().token("5702807852:AAFkiieEG1g5gFOB9xZ3Pj0E4l5izJadRWg").build()
    conv_handler = ConversationHandler\
        \
        (entry_points=[CommandHandler("start", start)],\
        \
        states={new_steps: [MessageHandler(filters.Regex("^(1|2|3|4|5|6|7|8|9)$"), game),\
                            MessageHandler(filters.Regex("^Начать сначала$"), repeat_game)],\
                naming_1: [MessageHandler(filters.TEXT & ~(filters.COMMAND), namer_1)],\
                naming_2: [MessageHandler(filters.TEXT & ~(filters.COMMAND), namer_2)],\
                repeating: [MessageHandler(filters.Regex("^Новая игра$"), new_game)]},\
        \
        fallbacks=[MessageHandler(filters.Regex("^Выход$"), cancel)])
 
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()