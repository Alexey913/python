# from progress.bar import Bar
# import time

# -------------------------------

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# ------------------------------

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,5,8,9]
# plt.plot(list)

# plt.show()

# -------------------------------
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comands import hi_command, help_command, time_command, sum_command
from spy import *



app = ApplicationBuilder().token("5747903332:AAFpvCsAEjqmJ1-Lf5dkeSTZs0uiy04aL20").build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


print ('server start')
app.run_polling()
