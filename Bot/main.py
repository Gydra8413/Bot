# - *-config: utf- 8 - *-
#import config
import telebot
from telebot import types

#sys.setdefaultencoding('utf-8')

token = '1170474994:AAHDwIL2EKfy23DVFSoGEOGfUPyIQ9Vfhg8'



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Мы, Крупнейший в телеграмме наркошоп рады приветствовать вас. У нас в наличии качественный товар и шаговая доступность', reply_markup=markup1)


markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item1=('Санкт-Петербург')
item2=('Москва')
item3=('Калуга')


markup1.add(item1, item2, item3)

markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item4=('Медведково')
item5=('Отрадное')
item6= ('Речной вокзал') 
item7=('Сходненская') 
item8=('Митино')
item9=('Преображенская площадь')
item10=('Измайлово')
item11=('Новогиреево')
item12=('Достоевская')
item13=('Дмитровксая')
item14=('Молодежная')
item15=('Озерная') 
item16=('Рязань')
item17=('Тула')
item18=('Калуга')
item19=('Волоколамск')
item20=('Дмитровксая')
item21=('Молодежная')
item22=('Озерная') 
item23=('Рассказовка')
item24=('Киевская')
item25=('Спортивная')
item26=('Проспект Вернадского')
item27=('Третьяковская')
item28=('Тверская')
item29=('Калужская') 
item30=('Коломенская')
item31=('Марьино')
item32=('Теплый стан')
item33=('Чертаново')
item34=('Улица Скобелевская')
item35=('Кузьминки')

markup2.add(item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35)



markup4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item36=('Гашиш 0.5гр-700')
item37=('Марихуана 0.5гр-1099')
item38= ('Амфетамин 1гр-1199') 
item39=('Метамфетамин 1гр-2199') 
item40=('Героин 1гр-1899')
item41=('Псилоцибиновые грибы 1гр-999')
item42=('ЛСД 1-2999')
item43=('Экстази 1гр-1299')
item44=('Кокаин 1гр-8699')
markup4.add(item36,item37,item38,item39,item40,item41,item42,item43,item44)

markup3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item45=('Садовое')
item46=('Площадь Восстания')
item47= ('Обводный канал') 
item48=('Балтийская') 
item49=('Приморская')
item50=('Старая деревня')
item51=('Черная речка')
item52=('Площадь мужества')
item53=('Новочеркаская')
item54=('Ломоносовкая')
item55=('Международная')
item56= ('Кировский завод') 

markup3.add(item45,item46,item47,item48,item49,item50,item51,item52,item53,item54,item55,item56)

@bot.message_handler(content_types=['text'])
def send_message(message):
	if message.text == 'Москва':
		bot.send_message(message.chat.id,'Выберите ближайщий район', reply_markup=markup2)
	elif message.text == 'Санкт-Петербург':	
 		bot.send_message(message.chat.id,'Выберите ближайщий район', reply_markup=markup3)
	elif message.text == 'Химки':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)	
	elif message.text == 'Мытищи':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Королев':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Балашиха':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Одинцово':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Люберцы':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Великий Новгород':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Тверь':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Иваново':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Владимир':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Рязань':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Тула':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Калуга':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Волоколамск':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Медведково':
 		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Отрадное':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Речной вокзал':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Сходненская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Митино':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Преображенская площадь':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Измайлово':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Новогиреево':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Достоевская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Дмитровксая':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Молодежная':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Озерная':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Рассказовка':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Киевская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Спортивная':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Проспект Вернадского':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Третьяковская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Тверская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Калужская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Коломенская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Марьино':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Теплый стан':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Чертаново':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Улица Скобелевская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Кузьминки':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Садовое':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Площадь Восстания':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Обводный канал':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Балтийская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Приморская':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Старая деревня':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Старая деревня':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Черная речка':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Площадь мужества':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Новочеркасcкая':
		bot.send_message(message.chat.id,'Выберите товар', reply_markup=markup4)
	elif message.text == 'Гашиш 0.5гр-700':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Марихуана 0.5гр-1099':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Амфетамин 1гр-1199':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Метамфетамин 1гр-2199':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Героин 1гр-1899':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Псилоцибиновые грибы 1гр-999':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'ЛСД 1-2999':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Экстази 1гр-1299':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс на указанный вами аккаунт в телеграмме . Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
	elif message.text == 'Кокаин 1гр-8699':
		bot.send_message(message.chat.id,'После оплаты вам поступит смс уведомление на указанный вами номер. Оплата осуществляется  через qiwi терминал пополнением яндекс кошелька или переводом на номер карты 4100 1151 0476 2539. В комментарии укажите ваш аккаунт в телеграмме и выбранный товар')
					
	


bot.polling()
