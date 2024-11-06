from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


from config import TOKEN


BOT_TOKEN: str = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    print("Получена команда '/start'")
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    print("Получена команда '/help'")
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@dp.message()
async def send_echo(message: Message):
    print(f"Получено сообщение:{message.text}")
    if message.text:
        await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
