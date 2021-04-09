from requests import request
from aiogram import Bot, Dispatcher, executor, types
import asyncio

bot = Bot(token='1788461202:AAE3p3SlKGnHss_W286PLpkA_LzZz_iCUKM')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
	userId = message.from_user.id
	await message.answer("Добро пожаловать, вы будете получать уведомления об изменении файла API Coinbase")
	File1 = open('coinbaseOriginal.txt', 'r')
	t = request('GET', 'https://api.pro.coinbase.com/currencies/').text
	with open('coinbaseNew.txt', 'w', encoding='utf-8') as File2:
		File2.write(t)


	async def scheduled(wait_for):
		while True:
			await asyncio.sleep(wait_for)
			if open(r'coinbaseOriginal.txt').read() == open(r'coinbaseNew.txt').read():
				await bot.send_message(userId, "Равны.")
			else:
				await bot.send_message(userId, "Не равны.")

	if __name__ == '__main__':
		loop = asyncio.get_event_loop()
		loop.create_task(scheduled(10))

	


executor.start_polling(dp, skip_updates=True)
	











	
#1 вариант
#myurl = urllib.urlopen("https://api.pro.coinbase.com/currencies/") 
#html_string = myurl.read()
#text = html2text(html_string)
#file = open("coinbase.txt", "w")
#file.write(text)
#file.close()
#2 вариант	
#urllib.request.urlretrieve(myurl, "coinbase.txt")
#3
#req = Request('https://api.pro.coinbase.com/currencies/', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()