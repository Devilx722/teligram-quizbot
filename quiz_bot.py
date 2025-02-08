import telebot
from telebot import types

# अपना Telegram Bot API Token यहाँ डालें
API_TOKEN = "8129447385:AAFKM1SrUQe2sN_op-Ul2K98T_tltIAPgeY"

bot = telebot.TeleBot(API_TOKEN)

# क्विज़ डेटा (डेमो क्वेश्चन)
quiz_data = {
    "What is the capital of India?": ["Delhi", "Mumbai", "Kolkata", "Chennai", "Delhi"],
    "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Venus", "Mars"]
}

# स्टार्ट कमांड
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to QuizBot! Use /quiz to start a quiz.")

# क्विज़ शुरू करें
@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    for question, options in quiz_data.items():
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for option in options[:-1]:  # लास्ट ऑप्शन सही जवाब होता है
            markup.add(types.KeyboardButton(option))
        bot.send_message(message.chat.id, question, reply_markup=markup)
        bot.register_next_step_handler(message, check_answer, question)

# जवाब चेक करें
def check_answer(message, question):
    correct_answer = quiz_data[question][-1]
    if message.text == correct_answer:
        bot.send_message(message.chat.id, "✅ Correct!")
    else:
        bot.send_message(message.chat.id, f"❌ Wrong! The correct answer is {correct_answer}")

# बॉट को रन करें
bot.polling()
