import time
import requests
import telebot
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6718990200:AAFW7ugnaUoU6V0l270AnBv9QRmsOx113bE')
id_channel = '@voanewset'

last_processed_news = ''


@bot.message_handler(content_types=['text'])
def command(message):
    global last_processed_news
    if message.text == "Start":
        while True:
            post_text = parser()

            if post_text is not None and post_text != last_processed_news:
                bot.send_message(id_channel, post_text, disable_web_page_preview=True)
                last_processed_news = post_text
            time.sleep(300)
    else:
        bot.send_message(message.from_user.id, "write start")


def parser():
    url = 'https://amharic.voanews.com/ethiopia'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    post = soup.find("div", class_="media-block")
    if post:
        title = post.find("h4", class_="media-block__title").text.strip()
        return f"{title}\n link: {'https://amharic.voanews.com/ethiopia'}"
    return None


bot.polling()
