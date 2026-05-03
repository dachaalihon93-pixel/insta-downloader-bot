import telebot
from telebot import types

# Token probelsiz holatda
TOKEN = '8763501142:AAFH-YJbXI_GDx7YGRDjg'
bot = telebot.TeleBot(TOKEN)

texts = {
    'start': "Assalomu alaykum! Botimizga xush kelibsiz! 😊\nsiz bu bot orqali Instagram videolarini yuklashingiz va musiqalar qidirishingiz mumkin.",
    'select_lang': "Iltimos, tilni tanlang / Пожалуйста, выберите язык / Please select a language:",
    'send_link': {
        'uz': "Menga Instagram havolasini yuboring, men sizga video yuklab beraman 📥",
        'ru': "Отправьте мне ссылку на Instagram, я скачаю вам видео 📥",
        'en': "Send me an Instagram link, I will download the video for you 📥"
    },
    'error_found': {
        'uz': "Uzur, ma'lumot topolmadik ❌",
        'ru': "Извините, информация не найдена ❌",
        'en': "Sorry, no information found ❌"
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, texts['start'])
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("O'zbek tili 🇺🇿", callback_data='lang_uz'),
        types.InlineKeyboardButton("Русский язык 🇷🇺", callback_data='lang_ru'),
        types.InlineKeyboardButton("English 🇺🇸", callback_data='lang_en')
    )
    bot.send_message(message.chat.id, texts['select_lang'], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def language_selection(call):
    lang = call.data.split('_')[1]
    bot.answer_callback_query(call.id)
    bot.edit_message_text(chat_id=call.message.chat.id, 
                         message_id=call.message.message_id, 
                         text=texts['send_link'][lang])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "instagram.com" in message.text:
        bot.reply_to(message, "Video tayyorlanmoqda... 🔄")
    else:
        bot.send_message(message.chat.id, "Musiqa qidirilmoqda: " + message.text + " ✨")

if __name__ == "__main__":
    bot.polling(none_stop=True)
