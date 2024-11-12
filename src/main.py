import telegram.ext as tl
import logging

from bot import bot_functions
from envparse import env
from utils.database.engine import engine
from utils.database.base import Base
Base.metadata.create_all(engine)


BOT_OPTIONS: dict = {
    'app language': 'RUS',
    'time zone/offset': '+7',
    'time of instance(s) in hours': (
        8, 20,
    ),
}
env.read_envfile("../.env")

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)

if __name__ == '__main__':
    bot = tl.ApplicationBuilder().token(env("TOKEN")).build()
    # tell the bot how it should react to certain things
    birthday_set_handler = tl.CommandHandler(
        'ya_rodilsa', bot_functions.birthday_set)
    birthday_loop_handler = tl.CommandHandler(
        'start', bot_functions.birthday_start)
    birthday_remove_handler = tl.CommandHandler(
        'ya_oshibsa', bot_functions.birthday_remove)

    birthday_button_handler = tl.CallbackQueryHandler(
        bot_functions.birthday_button)

    # POSITION MATTERS: the bot will check them in order of appearence
    bot.add_handler(birthday_button_handler)
    bot.add_handler(birthday_set_handler)
    bot.add_handler(birthday_remove_handler)
    bot.add_handler(birthday_loop_handler)
    print("Бот запущен!")
    bot.run_polling(poll_interval=2.0)
