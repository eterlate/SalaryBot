import telebot
from buttons import *
import re
from config import TOKEN
from db_connect import *
from sql_requests import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    check = exist_check(message.chat.id)
    if(check):
        bot.send_message(message.chat.id, 'Здравствуйте ' + message.chat.first_name + '!', reply_markup=main_buttons())
    else: 
        bot.send_message(message.chat.id, 'Для создания учетной записи нужен ваш номер телефона, вы согласны?', reply_markup=reg_buttons())

@bot.message_handler(content_types="contact")
def contact(message):
    phone = "".join(symbol for symbol in re.findall("\d+", message.contact.phone_number))
    reg_check = new_user(message.chat.id, message.chat.last_name, message.chat.first_name, phone, message.chat.username)
    if (reg_check):
        bot.send_message(message.chat.id, 'Вы зарегистрированы', reply_markup=main_buttons())
    else:
        bot.send_message(message.chat.id, 'Данные обновлены', reply_markup=main_buttons())

@bot.message_handler(func=lambda m: True)
def main_listener(m):
    if(m.text == 'Изменить ставку в час'):
        msg = bot.send_message(m.chat.id, 'Введите ставку в час(только число):')
        bot.register_next_step_handler(msg, change_salary_step)

def change_salary_step(msg):
    chat_id = msg.chat.id
    salary = msg.text
    check = change_salary(chat_id, salary)
    if(check):
        bot.send_message(msg.chat.id, 'Данные обновлены', reply_markup=main_buttons())
    else:
        bot.send_message(msg.chat.id, 'Данные введены неверно', reply_markup=main_buttons())


    








# @bot.message_handler()
# def user_commands(message):
#     if message.text == "Ввести часы":
#         bot.send_message(message.chat.id, 'Ввести часы')
#     elif message.text == "Посмотреть часы":
#         bot.send_message(message.chat.id, 'Глянуть')
#     elif message.text == "Регистрация":
#         bot.send_message(message.chat.id, 'Глянуфыть')
#     elif message.text == "Помощь":
#         bot.send_message(message.chat.id, 'ыф')

bot.polling(none_stop=True)