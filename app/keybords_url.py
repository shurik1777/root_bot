"""Working with keyboard URL"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardButton

kbd_two = Router()


@kbd_two.message(Command("inline_url"))
async def cmd_inline_url(message: Message):
    """Working with keyboard Inline, URL"""
    """Для получения экземпляра бота уже в контексте вызова функции
     можно использовать контекстное хранилище,
    если оно поддерживается в вашей версии библиотеки.
    Например, используйте message.bot для доступа к экземпляру бота."""
    bot = message.bot

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )
    # Получает взаимодействие с конкретным пользователем
    # user_id = 1234567890
    user_id = message.from_user.id
    '''Чтобы получить user_id текущего пользователя, 
    который взаимодействует с ботом, вы можете использовать объект message в обработчике сообщений.'''
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(
            InlineKeyboardButton(
                text="Какой-то пользователь",
                url=f"tg://user?id={user_id}")
        )

    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )
