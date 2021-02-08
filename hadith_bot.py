import requests
import os
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

PORT = int(os.environ.get('PORT', 5000))
TOKEN = "1682743874:AAFe-9mXdjoM0l9_77SYAmn5AG0Kqo7pp4k"

updater = Updater(token = TOKEN, use_context= True)
dispatcher = updater.dispatcher


def get_hadith():

    # get api request link from sunnah.com
    url = "https://api.sunnah.com/v1/hadiths/random"

    # declaring data dictionary and required header key
    payload = "{}"
    headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

    # getting a random hadiths from the api call
    hadith_response = requests.request("GET", url, data=payload, headers=headers)

    # converting the response data into json format acting as a dictionary
    json_hadith_response = hadith_response.json()

    # cleaning the data
    hadith_collection = json_hadith_response['collection']
    hadith_book_number = json_hadith_response['bookNumber']
    hadith_topic = json_hadith_response['hadith'][0]['chapterTitle']
    hadith_body = json_hadith_response['hadith'][0]['body']
    hadith_body_edited = hadith_body.replace("<br/>","").strip("<p></p>").replace("<b>","").replace("</b>","")
    
    random_hadith = f"From Collection of {hadith_collection.title()}\n Book of {hadith_book_number} \
        \nUnder the topic:{hadith_topic}\n HADITH:{hadith_body_edited}"
    return random_hadith


def get_collection(collection_name):
    url = f"https://api.sunnah.com/v1/collections/{collection_name}"

    payload = "{}"
    headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

    response = requests.request("GET", url, data=payload, headers=headers)

    collections = response.json()
    collections_edited = collections['collection'][0]['shortIntro'].replace("<i>","").replace("</i>","")
    return collections_edited


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="Get a random hadiths")

def result(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_hadith())

def collections(update, context):
    collections_info = "You can get information about the top five collections of hadith is the islamic tradition.\n \
        They are listed below.\n 1. Bukhari\n 2. Muslim\n 3. Sunan Nasa-i\n 4. Sunan Abi Dawud\n 5. Jami` at-Tirmidhi\n 6. Sunan Ibn Majah"
    context.bot.send_message(chat_id = update.effective_chat.id, text = collections_info)

def get_bukhari(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('bukhari'))

def get_muslim(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('muslim'))

def get_sunan_nasai(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('nasai'))

def get_sunan_abudawud(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('adudawud'))

def get_jami_attirmidhi(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('tirmidhi'))

def get_sunan_ibnmajah(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('ibnmajah'))


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("randomhadith", result))
dispatcher.add_handler(CommandHandler("collections", collections))
dispatcher.add_handler(CommandHandler("bukhari",get_bukhari))
dispatcher.add_handler(CommandHandler("muslim",get_muslim))
dispatcher.add_handler(CommandHandler("nasai",get_sunan_nasai))
dispatcher.add_handler(CommandHandler("abudawud",get_sunan_abudawud))
dispatcher.add_handler(CommandHandler("tirmidhi",get_jami_attirmidhi))
dispatcher.add_handler(CommandHandler("ibnmajah",get_sunan_ibnmajah))


#updater.start_polling()
#updater.idle()

updater.start_webhook(listen = "0.0.0.0", port = int(PORT), url_path = TOKEN)
updater.bot.set_webhook('https://hadithsbot.herokuapp.com/' + TOKEN)
updater.idle()
