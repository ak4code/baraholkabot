from PIL import Image, ImageDraw, ImageFont
import telebot
import textwrap
from dotenv import load_dotenv
import os
load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def baner_maker(text):
    im = Image.open("./template.jpg")
    xsize, ysize = im.size
    font = ImageFont.truetype("./fonts/Roboto-Medium.ttf", 70)
    d = ImageDraw.Draw(im)
    text = textwrap.wrap(text, width=26)        
    d.multiline_text((xsize / 2, ysize / 2), text="\n".join(text), fill="black", anchor="mm", font=font, align="center")
    return im

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_photo(message.chat.id, baner_maker(message.text))

if __name__ == '__main__':
    bot.polling()