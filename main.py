import telebot
from telebot import types

# Bot tokeningni shu yerga yoz
TOKEN = '8763501142:AAFH YJbXI_GDx7YGRDjg' # Tokeningni o'zingniki bilan tekshirib ol
bot = telebot.TeleBot(TOKEN)

# --- MATNLAR LUG'ATI ---
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

# --- START BUYRUG'I ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, texts['start'])
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_uz = types.InlineKeyboardButton("O'zbek tili 🇺🇿", callback_data='lang_uz')
    btn_ru = types.InlineKeyboardButton("Русский язык 🇷🇺", callback_data='lang_ru')
    btn_en = types.InlineKeyboardButton("English 🇺🇸", callback_data='lang_en')
    
    markup.add(btn_uz, btn_ru, btn_en)
    bot.send_message(message.chat.id, texts['select_lang'], reply_markup=markup)

# --- TILLARNI TANLASH ---
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def language_selection(call):
    lang = call.data.split('_')[1]
    bot.answer_callback_query(call.id)
    bot.edit_message_text(chat_id=call.message.chat.id, 
                         message_id=call.message.message_id, 
                         text=texts['send_link'][lang])

# --- MUSIQA QIDIRISH VA LINKLAR BILAN ISHLASH ---
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    
    if "instagram.com" in text:
        # Bu yerda video yuklash mantiqi bo'ladi
        bot.reply_to(message, "Video tayyorlanmoqda... 🔄")
    else:
        # Musiqa qidirish mantiqi (Hozircha namunaviy)
        # Kelajakda bu yerga musiqa qidirish API sini ulaymiz
        bot.send_message(message.chat.id, "Musiqa qidirilmoqda: " + text + " ✨")
        # Agar musiqa topilmasa:
        # bot.send_message(message.chat.id, texts['error_found']['uz'])

# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling(none_stop=True)
