import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram.enums import ParseMode

bot = Bot(token="7765313806:AAHABbgUBKGBY1Q82LIgxkBPFi-FXcFqcxc")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🧪 Пройти тест",
            web_app=WebAppInfo(url="https://q3t8.ru")
        )]
    ])
    await message.answer(
        "<b>🧠 Добро пожаловать!</b>\n\n"
        "Ты на шаг ближе к пониманию того, <i>как работает твой мозг</i>.\n\n"
        "🔬 Пройди быстрый <u>нейрохимический тест</u>, чтобы определить:\n"
        "• твой <b>доминирующий нейромедиатор</b> 🧬\n"
        "• твой <b>дефицитный нейромедиатор</b> 🧪\n\n"
        "<b>🌐 Нажми кнопку ниже, чтобы начать:</b>\n\n"
        "<i>Результаты помогут лучше понять свою личность, привычки и поведение.</i>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
