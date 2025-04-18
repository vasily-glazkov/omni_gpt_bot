from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Чат')],
    [KeyboardButton(text='Генерация картинок')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отмена')]
    ]
)
