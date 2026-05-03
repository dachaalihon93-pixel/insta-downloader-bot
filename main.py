import telebot
from telebot import types

# ENG YANGI VA TO'G'RI TOKENINGIZ
TOKEN = '8763501142:AAEo-i-PWgbqgta9Sblbx4iCXepRlB9RY7c'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("O'zbek tili 🇺🇿", callback_data='lang_uz'),
        types.InlineKeyboardButton("Русский язык 🇷🇺", callback_data='lang_ru'),
        types.InlineKeyboardButton("English 🇺🇸", callback_data='lang_en')
    )
    bot.send_message(message.chat.id, "Assalomu alaykum! Tilni tanlang:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def language_selection(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Menga Instagram havolasini yuboring!")

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)
