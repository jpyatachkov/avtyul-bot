import os

import telebot
from telebot.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

TOKEN = os.getenv('AVTYUL_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

AVAILABLE_VARIANTS = {
    'Почти не Автюль': 1,
    'Немного Автюль': 2,
    'Автюль': 3,
    'Чуть больший Автюль, чем можно было бы': 4,
    'АВТЮЛЬ!!!!!1!': 5,
}

HEAD = 'ААААААА'
TAIL = 'втюль'


def generate_markup():
    variants = []

    for num, item in enumerate(AVAILABLE_VARIANTS.items()):
        k, v = item

        head = HEAD * v
        tail = TAIL
        response = '{}{}'.format(head, tail)

        variants.append(InlineQueryResultArticle(str(num), k, InputTextMessageContent(response)))

    return variants


@bot.inline_handler(lambda query: True)
def handle_avtyul_action(inline_query: InlineQuery):
    try:
        bot.answer_inline_query(inline_query.id, generate_markup())
    except Exception as e:
        print(e)


def main():
    bot.polling()


if __name__ == '__main__':
    main()
