import logging
from aiogram import Bot, Dispatcher, executor, types


from oxfordLookup import getDefinitions
from googletrans import Translator
translator = Translator()


API_TOKEN = '5874275443:AAGz2PQOjNG4Inu5q4x5qMJr6sDjLANrgIQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\ I'm helping for you")




@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup, audio = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            try:
                await message.reply_voice(voice=audio)
            except:
                pass
            # if lookup.get('audio'):
            #     await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
