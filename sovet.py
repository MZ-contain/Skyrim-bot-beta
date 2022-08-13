import logging
from aiogram import Bot, Dispatcher, executor, types
import random
import datetime
import asyncio
import time
from pyfiglet import Figlet
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
bot = Bot(token = '5553524618:AAH0fF1y7pHXTgjy56LvJAkHMpTwsbPJlc4')#Токен бота с расписанием
dp = Dispatcher(bot)
memstore = MemoryStorage()
logging.basicConfig(level=logging.INFO)
preview_text = Figlet(font='jazmine')
print(preview_text.renderText('Serkilo'))
class Кнопки():
    @dp.message_handler(commands="start")
    async def cmd_test1(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Культура")
        buttons = ["Общее", "География", 'История', 'Какую рассу выбрать?', 'Лучший сет', 'Мне повезет!']
        keyboard.add(*buttons)
        arr=["intro.jpg"]
        photo=open(random.choice(arr), "rb")
        await bot.send_photo(message.from_user.id, photo)
        time.sleep(2)
        await message.answer("Привет, ты попал в первый ТГ проводник в мир игры\nThe Elder Scrolls V: Skyrim.\nЭтот бот - быстрая википедия для игроков.\nПереодя по разделам ты сможешь найти ответ на любой вопрос, от истории персонажей и до гайдов по прохождения квестов")
        time.sleep(2)
        await message.answer("О чем хотите спрсосить?", reply_markup=keyboard)
class История():
    @dp.message_handler(lambda message: message.text =='История')
    async def cmd_inline_url(message: types.Message):
        buttons = [
            types.InlineKeyboardButton(text="До прихода Нордов", callback_data="До прихода Нордов"),
            types.InlineKeyboardButton(text="Приход нордов в Скайрим", callback_data="Приход нордов в Скайрим"),
            types.InlineKeyboardButton(text="Скайрим в Первую эру", callback_data="Скайрим в Первую эру"),
            types.InlineKeyboardButton(text="Скайрим во Вторую эру", callback_data="Скайрим во Вторую эру"),
            types.InlineKeyboardButton(text="Скайрим в Третью эру", callback_data="Скайрим в Третью эру"),
            types.InlineKeyboardButton(text="Скайрим в Четвёртую эру", callback_data="Скайрим в Четвёртую эру"),
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await message.answer(f'Что хотите?', reply_markup=keyboard)
    @dp.callback_query_handler(text="До прихода Нордов")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer('В раннюю Меретическую эру Скайрим населяли фалмеры, «снежные эльфы», вплоть до прибытия в Тамриэль переселенцев из Атморы и начала войн за территории.\nВместе с фалмерами в Скайриме проживали и двемеры. Они построили множество городов по всему Скайриму. В каких отношениях местный клан состоял со снежными эльфами — неясно, скорее всего, они смогли договориться друг с другом о мирном сосуществовании.\nТакже неясно, в каких отношениях оба народа были с проживавшими в Скайриме орками, чьи селения-крепости уже тогда были разбросаны по всему региону.')
    @dp.callback_query_handler(text="Приход нордов в Скайрим")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer('Скайрим находится ближе всего к Атморе и можно предположить, что переселенцы с севера часто приставали к его берегам, но, видимо, не задерживались здесь надолго. Археологические находки указывают на существование ранних человеческих поселений в Хаммерфелле, Хай-Роке и Морровинде, но не в Скайриме. К концу Меретической эры климатические условия в Атморе стали ухудшаться. Это вынудило обитателей континента искать себе новую родину. Переселение на Тамриэль приобретает массовый характер, начинают появляться чисто атморские поселения, жители которых предпочитают не подчиняться местным правителям-эльфам, а сохранять верность традициям своей родины. Одним из них был Саартал, основанный Исграмором недалеко от места его высадки — Головы Хсаарика.\nОпределённое время между атморцами и фалмерами сохранялся мир, но лишь до тех пор, пока фалмеры не напали на Саартал и не разграбили его. Это событие получило название Ночь слёз. Уцелевшие вернулись на Атмору, поклявшись отомстить мерам.\nВместе с Пятью сотнями Соратников Исграмор вернулся в Тамриэль и начал долгую войну со снежными эльфами, которая закончилась лишь в начале Первой эры (не ранее 140 года). Приблизительно в это же время началась Война драконов, в ходе которой власть Драконьего культа была свергнута.')
class Раса():
    @dp.message_handler(lambda message: message.text =='Какую рассу выбрать?')
    async def rassa(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Войн", "Маг", 'Лучник', 'Ассасин', 'Вор']
        keyboard.add(*buttons)
        await message.answer("Кем вы хотите играть?", reply_markup=keyboard)
    @dp.message_handler(lambda message: message.text =='Войн')
    async def rassa(message: types.Message):
        await message.answer("Подходящей для ближнего боя расой являются норды, орки, имперцы.\nПри выборе ближнего боя вам придется постоянно сталкиваться с противником в лобовую, нанося урон обычным оружием. Желательно при ближнем бое облачится в тяжелые доспехи, и взять щит.\nТакже можно пойти немного другим путем, и вооружится двуручным топором или молотом, ведь таким образом вы будете наносить вдвое больше урона, чем одноручным мечом или топором.\nГлавным преимуществом ближнего боя является простота, вам не нужно чему-то учиться, и большинство новичков выбирают именно эту тактику.\nСущественным минусом можно считать урон, который вы будете постоянно получать от врага, поэтому лучше всегда иметь несколько зелий для восстановления здоровья. ")    
    @dp.message_handler(lambda message: message.text =='Маг')
    async def rassa(message: types.Message):
        await message.answer('Подходящей для магии расой являются Бретонцы, Темные эльфы, Высокие эльфы, а также Имперцы.')
    @dp.message_handler(lambda message: message.text =='Лучник')
    async def rassa(message: types.Message):
        await message.answer(' Подходящей для стрельбы из лука расой являются лесные эльфы, редгарды, каджиты')
    @dp.message_handler(lambda message: message.text =='Ассасин')
    async def rassa(message: types.Message):
        await message.answer('Подходящей для ассасина расой являются Каджиты, Аргонианины и Лесные эльфы.')
    @dp.message_handler(lambda message: message.text =='Вор')
    async def rassa(message: types.Message):
        await message.answer('Для игры за вора хорошо подойдут Каджиты, Аргониане Темный и Лесной эльфы, так как они имеют пассивные навыки скрытности, карманных краж или взлома.')
class География():
    @dp.message_handler(lambda message: message.text =='География')
    async def cmd_inline_url(message: types.Message):
        buttons = [
            types.InlineKeyboardButton(text="Рельеф", callback_data="random_value"),
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await message.answer(f'Что хотите?', reply_markup=keyboard)
    @dp.callback_query_handler(text="random_value")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer('Рельеф\nПровинция имеет гористый рельеф, что делает передвижение по ней весьма проблематичным. Восточная граница Скайрима проходит по высоким и безжизненным горам Велоти. Существует два перевала, которые связывают Скайрим с Морровиндом. Первый перевал — это Данметское ущелье, которое путники пересекают при путешествии из Виндхельма в Блэклайт. Второй перевал расположен на дороге между Рифтеном и башней Силград. Южная граница проходит по не менее высоким горам Джерол. Перевал через горы Джерол — Белый Проход — исключительное, с исторической точки зрения, место. Существуют также и другие, менее известные перевалы через горные системы вдоль границ Скайрима. Граница с Хаммерфеллом и Хай Роком проходит по горам Друадах. В Скайриме расположена самая высокая гора Тамриэля — Глотка Мира, а также ещё пять чуть менее высоких горных вершин. Малые горные системы существуют и в глубине провинции — это горы во владениях Хаафингар, Винтерхолд, Хьялмарк и Фолкрит. Прибрежные территории Скайрима по большей части представляют собой равнины, опускающиеся к морю со стороны гор. Исключение составляет равнина в Хьялмарке. Это заболоченная низина, скорее всего сформированная наносами рек Карт и Хьял. Предел — это регион с крайне пересечённым ландшафтом — местные реки создали глубокие каньоны, по дну которых они протекают, образуя каскады водопадов. В центре провинции расположена огромная, лишённая лесов равнина, по которой кочуют племена великанов и их питомцы — мамонты. Многие называют эту равнину тундрой, хотя, скорее всего, это тундростепь. Владения Рифт и Фолкрит расположены на предгорных возвышенностях. Большая часть владения Истмарк лежит в заболоченной низине, где вовсю проявляется геотермальная активность, что свидетельствует об активных процессах вулканизма в этих краях. В целом рельеф Скайрима довольно разнообразный.')
class Cет():
    @dp.message_handler(lambda message: message.text =='Лучший сет')
    async def cmd_inline_url(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Легкие", "Тяжелые"]
        keyboard.add(*buttons)
        await message.answer(f'Какой тип брони?', reply_markup=keyboard)
    @dp.message_handler(lambda message: message.text =='Легкие')
    async def Ezarmor1(message: types.Message):
        qw=["Ez1.jpg"]
        photo=open(random.choice(qw), "rb")
        await bot.send_photo(message.from_user.id, photo)
        await message.answer('I -Соловьиный доспех. Магический комплект легкой брони, который повышает запас выносливости (Stamina) и улучшает урон, наносимый одноручным оружием (One-Handed)')
        ww=["Ez2.jpg"]
        photo=open(random.choice(ww), "rb")
        await message.answer('II - Драконий чешуйчатый доспех. По своим показателям защищенности эта легкая броня является лучшей в своем классе. С ней достигнуть максимального уровня защиты проще всего. К тому же она очень круто выглядит')
        await bot.send_photo(message.from_user.id, photo)
    @dp.message_handler(lambda message: message.text =='Тяжелые')
    async def Heavy2(message: types.Message):
        qq=["Hv1.jpg"]
        photo=open(random.choice(qq), "rb")
        await bot.send_photo(message.from_user.id, photo)
        await message.answer('I - Даэдрическая броня. Этот комплект снаряжения имеет очень высокий показатель брони, фактически это лучшая броня в Skyrim, если не учитывать содержимое официальных дополнений. Выглядит она тоже очень эффектно.')
        await message.answer('II - Доспех Азидала. Можно получить за прохождение задания «Раскопки» (Unearthed). Доспех имеет несколько очень полезных зачарований. Прежде всего он дает шанс, что противники, атакующие персонажа игрока, будут парализованы. Заклинания школы Колдовства (Conjuration) и рунные заклинания стоят на 25% больше, но имеют увеличенный радиус действия.')
        jj=["Hvv.png"]
        photo=open(random.choice(jj), "rb")
        await bot.send_photo(message.from_user.id, photo)    
class Общее():
    @dp.message_handler(lambda message: message.text =='Общее')
    async def history(message: types.Message):
        await message.answer('Эта провинция — родина нордов. Скайрим, известный также как Старое Королевство или Отчизна, был регионом Тамриэля, заселённым людьми, бежавшими с замерзающего континента Атмора.\nПравителем Скайрима является Верховный король, которого выбирает Собрание ярлов. Эта традиция была установлена после разрушительной войны Престолонаследия. Нарушение этой традиции карается смертью, как в случае убийства Ульфриком Буревестником короля Торуга. Верховному королю подчиняются все ярлы. В целом модель власти в Скайриме напоминает федерацию, так как владения имеют некое подобие автономии, но при этом подчиняются Королю.')
class Мне_повезет():
    @dp.message_handler(lambda message: message.text =='Мне повезет!')
    async def rassa(message: types.Message):
        buttons = ["Войн", "Маг", 'Лучник', 'Ассасин', 'Вор']
        f = random.choice(buttons)
        await message.answer(f'Начните играть с : {f}')



























if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)