import requests
from bs4 import BeautifulSoup
from telegram import Bot, ParseMode
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
bot_token = '6718990200:AAFW7ugnaUoU6V0l270AnBv9QRmsOx113bE'

# Replace 'YOUR_CHAT_ID' with your Telegram chat ID
chat_id = '@voanewsetbot'

# Replace this URL with the one you want to scrape
url = 'https://amharic.voanews.com/z/3303'

# Web scraping function
def scrape_website():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Customize this part based on the structure of the website
    news_titles = soup.find_all('h3', class_='title')

    # Extract titles
    titles = [title.text.strip() for title in news_titles]
    
    return titles

# Command to trigger web scraping and send data to Telegram
def start(update, context):
    news_titles = scrape_website()
    message = "\n".join(news_titles)

    context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher
    
    # Command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()