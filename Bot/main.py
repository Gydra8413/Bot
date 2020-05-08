# - *-config: utf- 8 - *-
#import config
import telebot
from telebot import types

#sys.setdefaultencoding('utf-8')

token = '1170474994:AAHDwIL2EKfy23DVFSoGEOGfUPyIQ9Vfhg8'



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Ростовский наркошоп. В наличии качественный товар и шаговая доступность', reply_markup=markup1)


markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item1=('Комсомольская улица')
item2=('Невская улица')
item3=('Ленинская улица')
markup1.add(item1, item2, item3)

# markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# item4=('Медведково')
# item5=('Отрадное')
# item6= ('Речной вокзал') 
# item7=('Сходненская') 
# item8=('Митино')
# item9=('Преображенская площадь')
# item10=('Измайлово')
# item11=('Новогиреево')
# item12=('Достоевская')
# item13=('Дмитровксая')
# item14=('Молодежная')
# item15=('Озерная') 
# item16=('Рязань')
# item17=('Тула')
# item18=('Калуга')
# item19=('Волоколамск')
# item20=('Дмитровксая')
# item21=('Молодежная')
# item22=('Озерная') 
# item23=('Рассказовка')
# item24=('Киевская')
# item25=('Спортивная')
# item26=('Проспект Вернадского')
# item27=('Третьяковская')
# item28=('Тверская')
# item29=('Калужская') 
# item30=('Коломенская')
# item31=('Марьино')
# item32=('Теплый стан')
# item33=('Чертаново')
# item34=('Улица Скобелевская')
# item35=('Кузьминки')

# markup2.add(item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35)


markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item4=('Гашиш 0.5гр-700p')
item5=('Бошки 1гр-1790p')
item6= ('Амфетамин 1гр-1199p') 
item7=('Мефедрон 1гр-1790p')
markup4.add(item4,item5,item6,item7)


markup3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item8=('Гашиш 1гр-1300p')
item9=('Бошки 0.5гр-1099p')
item10=('Метамфетамин 1гр-2199p') 
item11=('Героин 1гр-1899p')
item12=('Экстази 1гр-1299p')
markup4.add(item8,item9,item10,item11,item12)

markup4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item13=('Гашиш 1гр-1300p')
item14= ('Амфетамин 1гр-1199p') 
item15=('Метамфетамин 1гр-2199p') 
item16=('Экстази 0.5гр-800p')
item17=('Мефедрон 1гр-1790p')
markup4.add(item13,item14,item15,item16,item17)

# markup3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
# item45=('Садовое')
# item46=('Площадь Восстания')
# item47= ('Обводный канал') 
# item48=('Балтийская') 
# item49=('Приморская')
# item50=('Старая деревня')
# item51=('Черная речка')
# item52=('Площадь мужества')
# item53=('Новочеркаская')
# item54=('Ломоносовкая')
# item55=('Международная')
# item56= ('Кировский завод') 

# markup3.add(item45,item46,item47,item48,item49,item50,item51,item52,item53,item54,item55,item56)

@bot.message_handler(content_types=['text'])
def send_message(message):
	if message.text == 'Комсомольская улица':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup2)
	elif message.text == 'Невская улица':	
 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup3)
	elif message.text == 'Ленинская улица':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
		
# 	elif message.text == 'Мытищи':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Королев':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Балашиха':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Одинцово':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Люберцы':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Великий Новгород':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Тверь':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Иваново':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Владимир':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Рязань':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Тула':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Калуга':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Волоколамск':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Медведково':
#  		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Отрадное':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Речной вокзал':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Сходненская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Митино':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Преображенская площадь':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Измайлово':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Новогиреево':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Достоевская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Дмитровксая':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Молодежная':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Озерная':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Рассказовка':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Киевская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Спортивная':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Проспект Вернадского':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Третьяковская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Тверская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Калужская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Коломенская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Марьино':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Теплый стан':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Чертаново':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Улица Скобелевская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Кузьминки':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Садовое':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Площадь Восстания':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Обводный канал':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Балтийская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Приморская':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Старая деревня':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Старая деревня':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Черная речка':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Площадь мужества':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
# 	elif message.text == 'Новочеркасcкая':
# 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Гашиш 0.5гр-700p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Гашиш 1гр-1300p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Амфетамин 1гр-1199p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Метамфетамин 1гр-2199p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Героин 1гр-1899p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Бошки 0.5гр-1099p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'ЛСД 1-2999p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Экстази 1гр-1299p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Бошки 1гр-1790p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Мефедрон 1гр-1790p':
		bot.send_message(message.chat.id,'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'После оплаты вам в телеграмме поступит смс  с фото o местонахождени товара. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар':
		bot.send_message(message.chat.id,'Выбрать другое место', reply_markup=markup1)								
	



bot.polling()
