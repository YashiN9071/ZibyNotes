# t.me/ziby_notes_bot
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
TOKEN = '5143073002:AAFw3VjKfzbW75aDOmOpFxawN6QZxfP5ZX0'

# keyboard
reply_keyboard = [['/create_note', '/create_remind'],
                  ['/view_notes', '/view_reminds'],
                  ['/help', '/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


# functions and commands
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('create_note', create_note))
    dp.add_handler(CommandHandler('create_remind', create_remind))
    dp.add_handler(CommandHandler('view_notes', view_notes))
    dp.add_handler(CommandHandler('view_reminds', view_reminds))
    updater.start_polling()

    updater.idle()


def start(update, context):
    update.message.reply_text(
        'Давайте начнём!',
        reply_markup=markup
    )


def stop(update, context):
    update.message.reply_text('Значит на этом всё, надеюсь был полезен')
    return ConversationHandler.END


def help(update, context):
    update.message.reply_text("""Я имею следующие функции: 
    /create_note
    /create_remind 
    /view_notes 
    /view_remind""")


def create_note(update, context):
    update.message.reply_text('Напишите новую заметку')


def create_remind(update, context):
    update.message.reply_text('Напишите новую напоминалку')


def view_notes(update, context):
    update.message.reply_text('Вот ваши заметки')


def view_reminds(update, context):
    update.message.reply_text('Вот ваши напоминалки')


# start program
if __name__ == '__main__':
    main()
