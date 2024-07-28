from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# استبدل هذا بالتوكن الخاص بك
TOKEN = '7125736457:AAHaV8Ie3E6-TBGHBoHYpzfu5ZPah179UFU'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا هنا لأكرر رسائلك.')

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(text * 2)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
