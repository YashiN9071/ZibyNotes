# t.me/ziby_notes_bot
import logging

from telegram.ext import Updater, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
TOKEN = '5387683486:AAEHQB94zVgmg3JcYPQFmgHR_ZcmCy47SOU'

# keyboards
reply_keyboard = [['/notes', '/reminds'],
                  ['/help', '/stop']]
main_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

notes_reply_keyboard = [['/create_note', '/view_notes'],
                        ['/delete_note', '/come_back']]
notes_markup = ReplyKeyboardMarkup(notes_reply_keyboard, one_time_keyboard=True)

reminds_reply_keyboard = [['/create_remind', '/view_reminds'],
                          ['/delete_remind', '/come_back']]
reminds_markup = ReplyKeyboardMarkup(reminds_reply_keyboard, one_time_keyboard=True)


# functions and commands
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('notes', notes))
    dp.add_handler(CommandHandler('reminds', reminds))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('stop', stop))
    updater.start_polling()

    updater.idle()


def start(update, context):
    update.message.reply_text(
        'Давайте начнём!',
        reply_markup=main_markup
    )


def stop(update, context):
    update.message.reply_text('Значит на этом всё, надеюсь был полезен')
    return ConversationHandler.END


def help(update, context):
    update.message.reply_text('У меня есть следующие функции: ')


def notes(update, context):
    update.message.reply_text('Здесь вы можете посмотреть все ваши существующие заметки, добавить новую\
     или удалить старую заметку', reply_markup=notes_markup)


def create_note(update, context):
    update.message.reply_text('Напишите новую заметку')


def view_notes(update, context):
    update.message.reply_text('Вот ваши заметки')


def delete_note(update, context):
    update.message.reply_text('')


def reminds(update, context):
    update.message.reply_text('Напишите новую заметку')


def create_remind(update, context):
    update.message.reply_text('Напишите новую напоминалку')


def view_reminds(update, context):
    update.message.reply_text('Вот ваши напоминалки')


def delete_remind(update, context):
    update.message.reply_text('')


# start program
if __name__ == '__main__':
    main()
