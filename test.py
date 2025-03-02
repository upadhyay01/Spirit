# import os
# import re
# import datetime
# import logging
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from apscheduler.schedulers.background import BackgroundScheduler
# from groq import Groq

# # Configure logging for debugging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize Groq client
# client =Groq(api_key="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")

# # === In-Memory Data Stores ===
# user_data = {}
# analytics = {}

# # === Generate Bhagavad Gita Response ===
# def generate_gita_response(message):
#     print("messagemessagemessage",message)
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""You have given this question {message}.
#                     Act as a Bhagavad Gita scholar and provide a mantra from the Bhagavad Gita along with its meaning.
#                     You have to give in response the output in the Hindi language as well as English language.

#                     OUTPUT FORMAT:-
#                       Mantra: [Mantra from the Bhagavad Gita in Hindi]
#                       Meaning: [Meaning of this Mantra in Hindi]
#                       Mantra: [Mantra from the Bhagavad Gita in English]
#                       Meaning: [Meaning of this Mantra in English]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
    
#     response = chat_completion.choices[0].message.content
#     cleaned_response=re.sub(r"<think>.*?</think>", "",response, flags=re.DOTALL).strip()

#     return cleaned_response

# # === Crisis Redirection ===
# def check_crisis_keywords(message):
#     crisis_keywords = ["suicidal", "depressed", "hopeless"]
#     return any(word in message.lower() for word in crisis_keywords)

# # === Telegram Bot Setup ===
# TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7699349471:AAHvEbh-YOGoy80Vp42T8YUmXpMdJ7oQXh0")
# updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # /start command handler
# def start(update: Update, context: CallbackContext):
#     user_id = update.effective_user.id
#     update.message.reply_text("Welcome to the Bhagavad Gita Chatbot! Ask me anything about the Gita.")

# # Message handler for processing incoming texts
# def handle_message(update: Update, context: CallbackContext):
#     user_id = update.effective_user.id
#     text = update.message.text.strip()

#     analytics[user_id] = analytics.get(user_id, 0) + 1

#     if check_crisis_keywords(text):
#         update.message.reply_text("It sounds like you're going through a tough time. Please reach out to a trusted friend or professional. If you need immediate help, please contact your local emergency services.")
#         return

#     response = generate_gita_response(text)
#     update.message.reply_text(response)

# # Add handlers to the dispatcher
# dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# # Start polling for updates
# updater.start_polling()
# updater.idle()

# import os
# import re
# import datetime
# import logging
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from apscheduler.schedulers.background import BackgroundScheduler
# from groq import Groq

# # Configure logging for debugging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize Groq client
# client = Groq(api_key="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")

# # === In-Memory Data Stores ===
# user_data = {}
# analytics = {}

# # === Background Scheduler Setup ===
# scheduler = BackgroundScheduler()
# scheduler.start()

# # === Emotion Scoring System ===
# def analyze_emotions(message):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""Analyze the following message for emotional state. 
#                     Provide a score from 1 to 5 for each category: Stress, Sadness, Happiness, Anxiety, Depression. 
#                     Message: {message}
#                     Output format:
#                     Stress: [score]
#                     Sadness: [score]
#                     Happiness: [score]
#                     Anxiety: [score]
#                     Depression: [score]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
#     response = chat_completion.choices[0].message.content
#     scores = {key: int(value) for key, value in re.findall(r"(\w+): (\d+)", response)}
#     return scores

# # === Generate Bhagavad Gita Response Based on Emotions ===
# def generate_gita_response(emotions):
#     highest_emotion = max(emotions, key=emotions.get)
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""Based on the highest emotional score being {highest_emotion}, provide a Bhagavad Gita mantra
#                     that addresses this emotion, along with its meaning in Hindi and English.

#                     OUTPUT FORMAT:
#                     Mantra: [Mantra from the Bhagavad Gita in Hindi]
#                     Meaning: [Meaning of this Mantra in Hindi]
#                     Mantra: [Mantra from the Bhagavad Gita in English]
#                     Meaning: [Meaning of this Mantra in English]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
#     response = chat_completion.choices[0].message.content
#     return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

# # === Scheduled Task to Reply Based on Emotion Score ===
# def scheduled_reply(user_id, message, context: CallbackContext):
#     emotions = analyze_emotions(message)
#     response = generate_gita_response(emotions)
#     context.bot.send_message(chat_id=user_id, text=response)

# # === Crisis Redirection ===
# def check_crisis_keywords(message):
#     crisis_keywords = ["suicidal", "depressed", "hopeless"]
#     return any(word in message.lower() for word in crisis_keywords)

# # === Telegram Bot Setup ===
# TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7699349471:AAHvEbh-YOGoy80Vp42T8YUmXpMdJ7oQXh0")
# updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # /start command handler
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Welcome to the Bhagavad Gita Chatbot! Ask me anything about the Gita.")

# # Message handler for processing incoming texts
# def handle_message(update: Update, context: CallbackContext):
#     user_id = update.effective_user.id
#     text = update.message.text.strip()
#     analytics[user_id] = analytics.get(user_id, 0) + 1

#     if check_crisis_keywords(text):
#         update.message.reply_text(
#             "It sounds like you're going through a tough time. Please reach out to a trusted friend or professional. "
#             "If you need immediate help, please contact your local emergency services."
#         )
#         return

#     scheduler.add_job(scheduled_reply, 'date', run_date=datetime.datetime.now() + datetime.timedelta(minutes=5),
#                       args=[user_id, text, context])
#     update.message.reply_text("I will analyze your emotions and send a relevant Bhagavad Gita mantra in 5 minutes.")

# # Add handlers to the dispatcher
# dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# # Start polling for updates
# updater.start_polling()
# updater.idle()


# import os
# import re
# import datetime
# import logging
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from apscheduler.schedulers.background import BackgroundScheduler
# from groq import Groq

# # Configure logging for debugging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize Groq client
# client = Groq(api_key="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")

# # === In-Memory Data Stores ===
# user_data = {}
# analytics = {}

# # === Background Scheduler Setup ===
# scheduler = BackgroundScheduler()
# scheduler.start()

# # === Emotion Scoring System ===
# def analyze_emotions(message):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""Analyze the following message for emotional state. 
#                     Provide a score from 1 to 5 for each category: Stress, Sadness, Happiness, Anxiety, Depression. 
#                     Message: {message}
#                     Output format:
#                     Stress: [score]
#                     Sadness: [score]
#                     Happiness: [score]
#                     Anxiety: [score]
#                     Depression: [score]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
#     response = chat_completion.choices[0].message.content
#     scores = {key: int(value) for key, value in re.findall(r"(\w+): (\d+)", response)}
#     return scores

# # === Generate Bhagavad Gita Response Based on Emotions ===
# def generate_gita_response(emotions):
#     highest_emotion = max(emotions, key=emotions.get)
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""Based on the highest emotional score being {highest_emotion}, provide a Bhagavad Gita mantra
#                     that addresses this emotion, along with its meaning in Hindi and English.

#                     OUTPUT FORMAT:
#                     Mantra: [Mantra from the Bhagavad Gita in Hindi]
#                     Meaning: [Meaning of this Mantra in Hindi]
#                     Mantra: [Mantra from the Bhagavad Gita in English]
#                     Meaning: [Meaning of this Mantra in English]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
#     response = chat_completion.choices[0].message.content
#     return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

# # === Generate Direct Bhagavad Gita Response ===
# def generate_direct_gita_response(message):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": (
#                     f"""You have given this question {message}.
#                     Act as a Bhagavad Gita scholar and provide a mantra from the Bhagavad Gita along with its meaning.
#                     You have to give in response the output in the Hindi language as well as English language.

#                     OUTPUT FORMAT:-
#                       Mantra: [Mantra from the Bhagavad Gita in Hindi]
#                       Meaning: [Meaning of this Mantra in Hindi]
#                       Mantra: [Mantra from the Bhagavad Gita in English]
#                       Meaning: [Meaning of this Mantra in English]"""
#                 )
#             }
#         ],
#         model="deepseek-r1-distill-llama-70b",
#     )
#     response = chat_completion.choices[0].message.content
#     return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

# # === Scheduled Task to Reply Based on Emotion Score ===
# def scheduled_reply(user_id, message, context: CallbackContext):
#     emotions = analyze_emotions(message)
#     response = generate_gita_response(emotions)
#     context.bot.send_message(chat_id=user_id, text=response)

# # === Crisis Redirection ===
# def check_crisis_keywords(message):
#     crisis_keywords = ["suicidal", "depressed", "hopeless"]
#     return any(word in message.lower() for word in crisis_keywords)

# # === Telegram Bot Setup ===
# TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7699349471:AAHvEbh-YOGoy80Vp42T8YUmXpMdJ7oQXh0")
# updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # /start command handler
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Welcome to the Bhagavad Gita Chatbot! Ask me anything about the Gita or use /score to analyze your emotions.")

# # /score command handler
# def score(update: Update, context: CallbackContext):
#     user_id = update.effective_user.id
#     update.message.reply_text("Please send me a message describing how you feel, and I will analyze your emotions and send a relevant Bhagavad Gita mantra.")

# # Message handler for processing incoming texts
# def handle_message(update: Update, context: CallbackContext):
#     user_id = update.effective_user.id
#     text = update.message.text.strip()
#     analytics[user_id] = analytics.get(user_id, 0) + 1

#     if check_crisis_keywords(text):
#         update.message.reply_text(
#             "It sounds like you're going through a tough time. Please reach out to a trusted friend or professional. "
#             "If you need immediate help, please contact your local emergency services."
#         )
#         return

#     direct_response = generate_direct_gita_response(text)
#     update.message.reply_text(direct_response)

#     scheduler.add_job(scheduled_reply, 'date', run_date=datetime.datetime.now() + datetime.timedelta(minutes=5),
#                       args=[user_id, text, context])
#     update.message.reply_text("I will analyze your emotions and send a relevant Bhagavad Gita mantra in 5 minutes.")

# # Add handlers to the dispatcher
# dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(CommandHandler("score", score))
# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# # Start polling for updates
# updater.start_polling()
# updater.idle()


import os
import re
import datetime
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
from groq import Groq

# Configure logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Groq client
client = Groq(api_key="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")

# === In-Memory Data Stores ===
user_data = {}
analytics = {}
user_scores = {}

# === Background Scheduler Setup ===
scheduler = BackgroundScheduler()
scheduler.start()

# === Emotion Scoring System ===
def analyze_emotions(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    f"""Analyze the following message for emotional state. 
                    Provide a score from 1 to 5 for each category: Stress, Sadness, Happiness, Anxiety, Depression. 
                    Message: {message}
                    Output format:
                    Stress: [score]
                    Sadness: [score]
                    Happiness: [score]
                    Anxiety: [score]
                    Depression: [score]"""
                )
            }
        ],
        model="deepseek-r1-distill-llama-70b",
    )
    response = chat_completion.choices[0].message.content
    scores = {key: int(value) for key, value in re.findall(r"(\w+): (\d+)", response)}
    return scores

# === Generate Bhagavad Gita Response Based on Emotions ===
def generate_gita_response(emotions):
    highest_emotion = max(emotions, key=emotions.get)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    f"""Based on the highest emotional score being {highest_emotion}, provide a Bhagavad Gita mantra
                    that addresses this emotion, along with its meaning in Hindi and English.

                    OUTPUT FORMAT:
                    Mantra: [Mantra from the Bhagavad Gita in Hindi]
                    Meaning: [Meaning of this Mantra in Hindi]
                    Mantra: [Mantra from the Bhagavad Gita in English]
                    Meaning: [Meaning of this Mantra in English]"""
                )
            }
        ],
        model="deepseek-r1-distill-llama-70b",
    )
    response = chat_completion.choices[0].message.content
    return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

# === Scheduled Task to Reply Based on Emotion Score ===
def scheduled_reply(user_id, message, context: CallbackContext):
    emotions = analyze_emotions(message)
    user_scores[user_id] = emotions
    response = generate_gita_response(emotions)
    context.bot.send_message(chat_id=user_id, text=response)

# === Check User Score ===
def check_score(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in user_scores:
        scores = user_scores[user_id]
        score_message = "Your current emotional scores:\n"
        score_message += "\n".join([f"{key}: {value}" for key, value in scores.items()])
        update.message.reply_text(score_message)
    else:
        update.message.reply_text("No emotional scores recorded yet. Send a message to analyze your emotions.")

# === Telegram Bot Setup ===
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7699349471:AAHvEbh-YOGoy80Vp42T8YUmXpMdJ7oQXh0")
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# /start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Bhagavad Gita Chatbot! Ask me anything about the Gita or use /score to analyze your emotions.")

# /score command handler
def score(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update.message.reply_text("Please send me a message describing how you feel, and I will analyze your emotions and send a relevant Bhagavad Gita mantra.")

# Message handler for processing incoming texts
def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    text = update.message.text.strip()
    analytics[user_id] = analytics.get(user_id, 0) + 1

    direct_response = generate_gita_response(analyze_emotions(text))
    update.message.reply_text(direct_response)

    scheduler.add_job(scheduled_reply, 'date', run_date=datetime.datetime.now() + datetime.timedelta(minutes=5),
                      args=[user_id, text, context])
    update.message.reply_text("I will analyze your emotions and send a relevant Bhagavad Gita mantra in 5 minutes.")

# Add handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("score", score))
dispatcher.add_handler(CommandHandler("checkscore", check_score))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# Start polling for updates
updater.start_polling()
updater.idle()