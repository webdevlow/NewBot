import telebot
from telebot import types
import requests
from requests import get

bot = telebot.TeleBot(f"5714088744:AAG4D1tHSHNDJva4ycK8-Hr-bjcTEplQRjM")






@bot.message_handler(commands=['start'])
def start_message(message):
	markup_reply = telebot.types.InlineKeyboardMarkup()
	tov = telebot.types.InlineKeyboardButton('🛍 Товары', callback_data='tovari')
	markup_reply.row(tov)
	dostavka = telebot.types.InlineKeyboardButton('📝 О доставке', callback_data='dostavka')
	obr = telebot.types.InlineKeyboardButton('📨 Обратная связь', callback_data='obr')
	markup_reply.row(dostavka, obr)
	otz = telebot.types.InlineKeyboardButton('📚 Отзывы', url = "https://t.me/+SAkY_kPOKjk0NjQ6")
	markup_reply.row(otz)

	img_path = "https://i.ibb.co/C2g80Ps/W3-Ao-O66qf-NA.jpg"
	bot.send_photo(message.chat.id, get(f"{img_path}").content, caption = f'<b>Вас приветствует магазин «HOOLIGAN STYLE USS»</b>\n\n<b>Уважаемые клиенты!</b>\n\n<b>Рады приветствовать вас в нашем магазине!</b>\n\n📌 <b>Мы</b> - интернет-магазин стильной мужской одежды 🔥\n📌 У нас вы можете найти <b>качественный, модный товар</b>\n📍 <b>Наш адрес:</b> г.Уссурийск\n\nНаш оператор: <b>@Hooligan_uss</b>', parse_mode='html', reply_markup = markup_reply)


@bot.callback_query_handler(func=lambda message: True)
def KeyboardInline(call):
	if call.message:
		if call.data == "tovari":



			markup_reply = telebot.types.InlineKeyboardMarkup()
			tov = telebot.types.InlineKeyboardButton('Футболки', callback_data='fut')
			dostavka = telebot.types.InlineKeyboardButton('Кроссовки', callback_data='kros')
			obr = telebot.types.InlineKeyboardButton('Шорты', callback_data='cap')
			complect = telebot.types.InlineKeyboardButton('Спортивные комплекты', callback_data='comp')
			markup_reply.row(tov)
			markup_reply.row(dostavka)
			markup_reply.row(obr)
			markup_reply.row(complect)
			bot.send_message(call.message.chat.id, '<b>Выберите категорию: </b>', parse_mode='html', reply_markup=markup_reply)

		if call.data == "fut":

			markup_reply = telebot.types.InlineKeyboardMarkup()
			tov = telebot.types.InlineKeyboardButton('Купить', url = "t.me/Hooligan_uss")
			markup_reply.row(tov)
			back = telebot.types.InlineKeyboardButton('Вернуться назад', callback_data= "back")
			markup_reply.row(back)

			img_path = "https://i.ibb.co/CHwfQpg/1.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#1.</b>\n\n🔥 Футболка - оверсайз, состав : 100% хлопок\n\n💣 Качественные эмблемы и свободная посадка\n✅ Размер: 46🔹\n\n Цена: <b>1800</b>', parse_mode='html', reply_markup=markup_reply)
			img_path = "https://i.ibb.co/MVgyJCX/2.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#2.</b>🔹Пополнение футболок\n⚡ Материал: 100% - хлопок, свободная посадка и прямой крой\n⚡ Размер:46\n\n Цена: <b>1800</b>', parse_mode='html', reply_markup=markup_reply)
			img_path = "https://i.ibb.co/zPWTP2G/3.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#3.</b>🔹 Оверсайз футболки с вышитыми эмблемами\n🔹 Состав: 100-% хлопок, прямой крой, свободная посадка🔹\n Размер: 46🔹\n\nЦена: <b>1800</b>', parse_mode='html', reply_markup=markup_reply)
			img_path = "https://i.ibb.co/0KcF168/4.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#4.</b>🔹 Футболка - оверсайз, материал: эластичный хлопок🔹\n Качественные эмблемы, Турецкое производство🔹\n Свободная посадка и прямой крой🔹\n Размер: 46🔹\n\n Цена: <b>1800</b>', parse_mode='html', reply_markup=markup_reply)

		def back(message):

			bot.send_message(call.message.chat.id, "Вы вернулись назад")
			start_message(call.message)

		if call.data == "back":
			back(call.message)



		if call.data == "kros":
			markup_reply = telebot.types.InlineKeyboardMarkup()
			tov = telebot.types.InlineKeyboardButton('Купить', url = "t.me/Hooligan_uss")
			markup_reply.row(tov)
			back = telebot.types.InlineKeyboardButton('Вернуться назад', callback_data= "back")
			markup_reply.row(back)



			img_path = "https://i.ibb.co/7NyyrBg/4.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f"<b>#1.</b>\n\nКроссовки <b>Adidas Original Nite Jogger</b>\n\nСезон🍃🍂Весна Лето\n\n 🍂🍃Материал верх сетка и ЗамшШикарная подошва\n\n Лёгкие и очень удобные\nРазмер: 41/42/43/43/44/44/45/46\n\n Цена: <b>2500</b>", parse_mode='html', reply_markup=markup_reply)
		






		if call.data == "cap":
			markup_reply = telebot.types.InlineKeyboardMarkup()
			tov = telebot.types.InlineKeyboardButton('Купить', url = "t.me/Hooligan_uss")
			markup_reply.row(tov)
			back = telebot.types.InlineKeyboardButton('Вернуться назад', callback_data= "back")
			markup_reply.row(back)
			img_path = "https://i.ibb.co/56yKXrC/VGGw-YAWWUIs.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#1.</b>\n\n🔥 Материал: трикотаж - хлопок\n\n📌 Размеры 46 / 48\n\n 📌 Цена: <b>1800</b>', parse_mode='html', reply_markup=markup_reply)
		

		if call.data == "comp":
			markup_reply = telebot.types.InlineKeyboardMarkup()
			tov = telebot.types.InlineKeyboardButton('Купить', url = "t.me/Hooligan_uss")
			markup_reply.row(tov)
			back = telebot.types.InlineKeyboardButton('Вернуться назад', callback_data= "back")
			markup_reply.row(back)
			img_path = "https://i.ibb.co/n8CVCyY/e-Yt-NQ-Ce-ME4.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#1.</b>\n\nСочетания двух красивых цветов 🤤 \n\n🔹 Размеры: 48, 50\n🔹 Цена: <b>4990</b>', parse_mode='html', reply_markup=markup_reply)
			img_path = "https://i.ibb.co/HXKTX2d/2.jpg"
			bot.send_photo(call.message.chat.id, get(f"{img_path}").content, caption = f'<b>#2.</b>\n\n🔹 Стильный костюм 90х годах\n🔹 Все эмблемы вышиты, турецкое производство\n🔹 Размеры: 50, 52\n Цена: <b>4990</b>', parse_mode='html', reply_markup=markup_reply)



		if call.data == "obr" or call.data == "buy":
			bot.send_message(call.message.chat.id, '<b>Наш оператор - @Hooligan_uss [обращаться по поводу заказов и других вопросов]</b>', parse_mode='html')


		if call.data == "dostavka":
			bot.send_message(call.message.chat.id, '<b>✈ Отправка:</b>\n\n🚝 <b>Транспортной компанией (Почта России, СДЭК и т.д.).</b>\n<b>Отправим как вам удобно.</b>\n<b>Заказы принимаем круглосуточно 24/7</b>\n\n<b>Отзывы нашего магазина (жмите кнопку снизу)</b> 👇', parse_mode='html')



			








bot.polling(none_stop=True)

      