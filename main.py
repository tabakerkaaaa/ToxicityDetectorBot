import telebot
import SentimentAnalysis as SA
bot = telebot.TeleBot('API-key')
ToxicDetector = SA.ToxicDetector()
ToxicDetector.fitPipeline()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! I'm going to control the toxicity in this chat!")

@bot.message_handler(content_types=['text'])
def send_response(message):
    toxicityLevel = ToxicDetector.resultedToxicity(message.text)
    print(message.text, ": ", toxicityLevel)
    if toxicityLevel != -1 and toxicityLevel > 0.99:
        response = message.from_user.username + ", please, be more friendly!"
        bot.send_message(message.chat.id, response, reply_to_message_id=message.message_id)
bot.polling()
