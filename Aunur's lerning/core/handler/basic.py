from aiogram import Bot
from aiogram.types import Message
async def get_start(Mes: Message, bot: Bot):
    await bot.send_message(Mes.from_user.id, f'<b>Привет</b> {Mes.from_user.first_name}. Рад тебя видеть!')
    await Mes.answer(f'<s>Привет {Mes.from_user.first_name}. Как дела?</s>')
    await Mes.reply(f'<tg-spoiler>Смотри, {Mes.from_user.first_name}, как я умею.</tg-spoiler>')