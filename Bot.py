#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import random
from telebot import types
from Config import *

markup = types.ReplyKeyboardMarkup(row_width=2)

file = open('data','r')
Data = file.read().strip().split("\n")


bot = telebot.TeleBot(TOKEN)

def yiyan(message):
	Index=random.randint(0,len(Data)-1)
	print("Log: " + "一言: " + Data[Index])
	bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text=Data[Index],reply_markup=markup)

@bot.message_handler(commands=['yiyan'])
def send_welcome(message):
	yiyan(message);

if __name__ == '__main__':
	bot.polling()