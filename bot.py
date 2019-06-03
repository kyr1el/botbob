from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, человек по фамилии {}, хочешь знать ответ на это: {}?".format(update.message.chat.last_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main ():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('К вашим услугам')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
  