import re
from aiogram import Router, F, html
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, LinkPreviewOptions
from aiogram.enums import ParseMode
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag, Text
)

router = Router()


# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(f'Hello {message.from_user.first_name}')


# Хэндлер на команду /test1 подключаем через декоратор
@router.message(Command("test1"))
async def cmd_test1(message: Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2 подключаем через точечную аннатацию
async def cmd_test2(message: Message):
    await message.reply("Test 2")


router.message.register(cmd_test2, Command("test2"))


@router.message(Command("answer"))
async def cmd_answer(message: Message):
    await message.answer("Это простой ответ")


@router.message(Command("reply"))
async def cmd_reply(message: Message):
    await message.reply('Это ответ с "ответом"')


@router.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command("add_to_list"))
async def cmd_add_to_list(message: Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@router.message(Command("show_list"))
async def cmd_show_list(message: Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


@router.message(Command("info"))
async def cmd_info(message: Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


# Если не указать фильтр F.text,
# то хэндлер сработает даже на картинку с подписью /test
@router.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, <b>world</b>!",
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!",
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await message.answer("Сообщение с <u>HTML-разметкой</u>")
    # чтобы явно отключить форматирование в конкретном запросе,
    # передайте parse_mode=None
    await message.answer(
        "Сообщение без <s>какой-либо разметки</s>",
        parse_mode=None
    )


@router.message(Command("hello"))
async def cmd_hello(message: Message):
    """Не будет работать с ников м тегах"""
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
    )


@router.message(Command("hello2"))
async def cmd_hello(message: Message):
    """Второе чуть сложнее, но более продвинутое:
    воспользоваться специальным инструментом,
    который будет собирать отдельно текст и отдельно
    информацию о том, какие его куски должны быть
    отформатированы."""
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name)
    )
    await message.answer(
        **content.as_kwargs()
    )


@router.message(Command("advanced_example"))
async def cmd_advanced_example(message: Message):
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())


# @router.message(F.text)
# async def echo_with_time(message: Message):
#     # Получаем текущее время в часовом поясе ПК
#     time_now = datetime.now().strftime('%H:%M')
#     # Создаём подчёркнутый текст
#     added_text = html.underline(f"Создано в {time_now}")
#     # Отправляем новое сообщение с добавленным текстом
#     await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")


@router.message(Command("settimer"))
async def cmd_settimer(
        message: Message,
        command: CommandObject
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/settimer <time> <message>"
        )
        return
    await message.answer(
        "Таймер добавлен!\n"
        f"Время: {delay_time}\n"
        f"Текст: {text_to_send}"
    )


@router.message(Command("custom1", prefix="%"))
async def cmd_custom1(message: Message):
    await message.answer("Вижу команду!")


# Можно указать несколько префиксов....vv...
@router.message(Command("custom2", prefix="/!"))
async def cmd_custom2(message: Message):
    await message.answer("И эту тоже вижу!")


# @router.message(F.text)
# async def extract_data(message: Message):
#     data = {
#         "url": "<N/A>",
#         "email": "<N/A>",
#         "code": "<N/A>"
#     }
#     entities = message.entities or []
#     for item in entities:
#         if item.type in data.keys():
#             # Неправильно
#             # data[item.type] = message.text[item.offset : item.offset+item.length]
#             # Правильно
#             data[item.type] = item.extract_from(message.text)
#     await message.reply(
#         "Вот что я нашёл:\n"
#         f"URL: {html.quote(data['url'])}\n"
#         f"E-mail: {html.quote(data['email'])}\n"
#         f"Пароль: {html.quote(data['code'])}"
#     )


@router.message(Command("help"))
@router.message(CommandStart(
    deep_link=True, magic=F.args == "help"
))
async def cmd_start_help(message: Message):
    await message.answer("Это сообщение со справкой")


@router.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'book_(\d+)'))
))
# https://t.me/yyyee2e_bot?start=book_255
async def cmd_start_book(
        message: Message,
        command: CommandObject
):
    book_number = command.args.split("_")[1]
    await message.answer(f"Sending book №{book_number}")


@router.message(Command("links"))
async def cmd_links(message: Message):
    links_text = (
        "https://nplus1.ru/news/2024/05/23/voyager-1-science-data"
        "\n"
        "https://t.me/telegram"
    )
    # Ссылка отключена
    options_1 = LinkPreviewOptions(is_disabled=True)
    await message.answer(
        f"Нет превью ссылок\n{links_text}",
        link_preview_options=options_1
    )

    # -------------------- #

    # Маленькое превью
    # Для использования prefer_small_media обязательно указывать ещё и url
    options_2 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_small_media=True
    )
    await message.answer(
        f"Маленькое превью\n{links_text}",
        link_preview_options=options_2
    )

    # -------------------- #

    # Большое превью
    # Для использования prefer_large_media обязательно указывать ещё и url
    options_3 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_large_media=True
    )
    await message.answer(
        f"Большое превью\n{links_text}",
        link_preview_options=options_3
    )

    # -------------------- #

    # Можно сочетать: маленькое превью и расположение над текстом
    options_4 = LinkPreviewOptions(
        url="https://nplus1.ru/news/2024/05/23/voyager-1-science-data",
        prefer_small_media=True,
        show_above_text=True
    )
    await message.answer(
        f"Маленькое превью над текстом\n{links_text}",
        link_preview_options=options_4
    )

    # -------------------- #

    # Можно выбрать, какая ссылка будет использоваться для предпосмотра,
    options_5 = LinkPreviewOptions(
        url="https://t.me/telegram"
    )
    await message.answer(
        f"Предпросмотр не первой ссылки\n{links_text}",
        link_preview_options=options_5
    )
