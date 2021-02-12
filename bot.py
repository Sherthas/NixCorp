from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola puta, ¿Querés que te la ponga?')


if __name__ == '__main__':

    updater = Updater(token='Yourtoken', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
