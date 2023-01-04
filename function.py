import telegram
from flask import request

def handler(request):
    bot = telegram.Bot(token=TOKEN)

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        message = update.message.text
        bot.send_message(chat_id=chat_id, text="You said: {}".format(message))

    return "ok"
