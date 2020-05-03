import telebot
import SentimentAnalysis as SA
bot = telebot.TeleBot('898935402:AAEUV054hw-kyxD7rO0WmVk_nfTwGfH0tro')
ToxicDetector = SA.ToxicDetector()
ToxicDetector.fitPipeline()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, пидорасы, отныне я буду контролировать токсичность в этом чятике")

@bot.message_handler(content_types=['text'])
def send_response(message):
    toxicityLevel = ToxicDetector.resultedToxicity(message.text)
    print(message.text, ": ", toxicityLevel)
    if toxicityLevel != -1 and toxicityLevel > 0.99:
        response = "Ты че блять, " + message.from_user.username + "? Дружелюбнее сука будь."
        bot.send_message(message.chat.id, response, reply_to_message_id=message.message_id)
bot.polling()
