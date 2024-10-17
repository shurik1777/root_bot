"""Function for keyboard"""
from aiogram.types import ReplyKeyboardMarkup


def create_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    """Creates keyboard"""
    return ReplyKeyboardMarkup(keyboard=buttons)
