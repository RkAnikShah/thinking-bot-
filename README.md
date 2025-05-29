 # thinking-bot-from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text("হ্যালো! আমি Thinker Bot 🤖\nআমি মানুষের আচরণ বিশ্লেষণ করতে পারি। টাইপ করো /behavior")

def behavior(update, context):
    update.message.reply_text("তুমি যদি বারবার রেগে যাও, তাহলে তুমি ইমপালসিভ টাইপ।\nআর যদি ঠান্ডা মাথায় চিন্তা করে কাজ করো, তুমি এনালিটিকাল টাইপ।")

def main():
    TOKEN = os.getenv("BOT_TOKEN")  # এই TOKEN Render.com এর মাধ্যমে আসবে
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("behavior", behavior))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    python-telegram-bot==13.15
    services:
  - type: web
    name: thinker-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: BOT_TOKEN
        value: 7267078621:AAGbBNKBAYbEPVNLLTmtb1TKrSU0NhIfRFM
