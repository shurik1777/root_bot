"""Function for keyboard"""
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup


def create_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    """Creates keyboard RKM"""
    return ReplyKeyboardMarkup(keyboard=buttons)


def create_keyboard_in(buttons: list) -> InlineKeyboardMarkup:
    """Creates keyboard IKM"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[button] for button in buttons]  # Каждая кнопка на отдельной строке
    )
