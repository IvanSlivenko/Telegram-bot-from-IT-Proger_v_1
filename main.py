import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'qq'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Привіт')

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler(commands=['info'])
def cmd_info(message):
    bot.send_message(message.chat.id,f'{message.from_user.first_name}\n Вітаємо у нас на платформі' )         
    

bot.polling(non_stop=True)    
