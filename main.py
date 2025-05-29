from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text("হ্যালো! আমি তোমার থিংকার বট। 😊 টাইপ করো /behavior")

def behavior(update, context):
    responses = [
        "তুমি কিছু না বললেও আমি তোমার চেহারা থেকে আন্দাজ করতাম!",
        "এই মুহূর্তে তুমি দ্বিধায় আছো, তাই না?",
        "তোমার সিদ্ধান্তে ৭০% সম্ভাবনা যে তুমি পরে মত পাল্টাবে।"
    ]
    import random
    update.message.reply_text(random.choice(responses))

def main():
    token = os.getenv("BOT_TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("behavior", behavior))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
