import log
import excep
import main


from telegram import __version__ as TG_VER
from telegram import Update
from telegram.ext import (ContextTypes)

x = 0
y = 0

def init(a, b):
    global x 
    global y 
    x = a
    y = b
    log.universal_logger((x,y), data_description = "Ввод данных")
    return main.action_menu
        

async def int_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите число 1:')
    a = excep.check_int()
    await update.message.reply_text('Введите число 2:')
    b = excep.check_int()
    init (a, b)


async def float_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите число 1:')
    a = excep.check_float()
    await update.message.reply_text('Введите число 2:')
    b = excep.check_float()
    init (a, b)


async def complex_num (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('\nВведите действительную часть числа 1:')
    d_1 = excep.check_float()
    await update.message.reply_text('Введите мнимую часть числа 1:')
    m_1 = excep.check_float()
    a = complex(d_1, m_1)
    await update.message.reply_text('\nВведите действительную часть числа 2:')
    d_2 = excep.check_float()
    await update.message.reply_text('Введите мнимую часть числа 2: ')
    m_2 = excep.check_float()
    b = complex(d_2, m_2)
    init (a, b)