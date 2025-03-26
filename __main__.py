import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('8155444485:AAHsDhrq5ji-IJolWwUHjRtDR-HhiltwBJs')

import telebot

BOT_TOKEN = "8155444485:AAHsDhrq5ji-IJolWwUHjRtDR-HhiltwBJs"
bot = telebot.TeleBot(BOT_TOKEN)

questions = {
    "дошкольный и начальная школа": {
        "лёгкий": [
            {
                "question": "Где нельзя находиться в наушниках?",
                "options": ["В машине", "Вблизи ж/д путей", "На природе", "Дома"],
                "correct_answer": "Вблизи ж/д путей"
            },
            {
                "question": "Что нельзя делать в железнодорожном транспорте?",
                "options": ["Спать", "Играть в карты", "Высовываться из окна"],
                "correct_answer": "Высовываться из окна"
            },
            {
                "question": "Что делать, если вы потерялись на вокзале?",
                "options": ["Обратиться к прохожему за помощью", "Ждать, когда придёт помощь",
                            "Обратиться к работнику вокзала или полицейскому", "Самому искать родителей"],
                "correct_answer": "Обратиться к работнику вокзала или полицейскому"
            }
        ],
        "средний": [
            {
                "question": "Что из данных утверждений НЕЛЬЗЯ делать на ж/д путях или в железнодорожном транспорте?",
                "options": ["Есть на платформе в ожидании поезда", "Открывать окно в вагоне",
                            "Слушать музыку или смотреть в телефон вблизи железнодорожных путей",
                            "Ждать поезд за ограничительной линией, держась ближе к центру платформы"],
                "correct_answer": "Слушать музыку или смотреть в телефон вблизи железнодорожных путей"
            },
            {
                "question": "В какие игры можно играть возле поездов?",
                "options": ["Во все, это же весело", "В подвижные игры(футбол, прятки, догонялки)",
                            "Не играть в игры вообще", "В неподвижные игры(слова, города, ассоциации)"],
                "correct_answer": "В неподвижные игры(слова, города, ассоциации)"
            },
            {
                "question": "Где должен находиться пассажир, передвигаясь на железнодорожном транспорте?",
                "options": ["В вагоне", "На подножках в переходных площадках вагонов", "На крыше вагона",
                            "Цепляться за движущийся железнодорожный состав, маневренные тепловозы и другие подвижные составы"],
                "correct_answer": "В вагоне"
            }
        ],
        "сложный": [
            {
                "question": "Какая железная дорога считается первой?",
                "options": ["Московская", "Царскосельская", "Дальневосточная", "Забайкальская"],
                "correct_answer": "Царскосельская"
            }
        ]
    },
    "средняя школа": {
        "лёгкий": [
            {
                "question": "Какое напряжение в проводах контактной сети на железной дороге?",
                "options": ["10 тысяч вольт", "220 вольт", "600 вольт", "27 тысяч вольт"],
                "correct_answer": "27 тысяч вольт"
            },
            {
                "question": "Твои друзья решили развлечься, разрисовать вагоны поезда и положить камни на рельсы, что будешь делать?",
                "options": ["Пойду с ними и постою рядом", "Сделаю тоже, что и они, мы же друзья",
                            "Сделаю вид, что не слышал об этом", "Сделаю замечание и расскажу взрослым"],
                "correct_answer": "Сделаю замечание и расскажу взрослым"
            },
            {
                "question": "Что делать, если торопишься на важное мероприятие и нужно перейти ж/д пути?",
                "options": ["Перейду там, где считаю безопасным", "Посмотрю, что нет поездов и перейду по путям",
                            "Найду ближайший пешеходный настил, мост или виадук",
                            "Попрошу взрослого перевести меня через пути"],
                "correct_answer": "Попрошу взрослого перевести меня через пути"
            }
        ],
        "средний": [
            {
                "question": "Что делать, если вы оказались между двух движущихся поездов?",
                "options": ["Встать ровно, спиной к одному составу и лицом к другому, ждать, когда они проедут",
                            "Бежать в направлении большего поезда", "Лечь на землю на одинаковом расстоянии от поездов",
                            "Звать на помощь"],
                "correct_answer": "Лечь на землю на одинаковом расстоянии от поездов"
            },
            {
                "question": "Для чего нужен стоп-кран?",
                "options": ["Для экстренной остановки поезда", "Для управления поездом",
                            "Для того, чтобы остановить поезд на нужной остановке",
                            "Для того, чтобы вызвать проводника"],
                "correct_answer": "Для экстренной остановки поезда"
            },
            {
                "question": "Что делать, если вы увидели оголённый провод?",
                "options": ["Подойти, посмотреть и сообщить взрослым", "Потрогать и проверить есть ли электричество",
                            "Не подходить ближе, чем на 8 метров и сообщить взрослым", "Оставить его так"],
                "correct_answer": "Не подходить ближе, чем на 8 метров и сообщить взрослым"
            }
        ],
        "сложный": [
            {
                "question": "Что делать, если вы приехали на маленький остановочный пункт, где нет пешеходного настила, виадука и подземного перехода. Вам нужно пересечь железнодорожные пути. Как вы будете это делать?",
                "options": [
                    "Пройду по насыпи вдоль железнодорожных путей до удобного на мой взгляд места и там пересеку железную дорогу",
                    "Пересеку железнодорожные пути под прямым углом и отправлюсь дальше", "Выкопаю подземный переход",
                    "Не буду пересекать железнодорожные пути"],
                "correct_answer": "Пересеку железнодорожные пути под прямым углом и отправлюсь дальше"
            }
        ]
    }
}

user_states = {}


def create_keyboard(options):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for option in options:
        keyboard.add(option)
    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    user_states[user_id] = {}
    markup = create_keyboard(["дошкольный и начальная школа", "средняя школа"])
    bot.send_message(message.chat.id, "Выберите возраст:", reply_markup=markup)
    bot.register_next_step_handler(message, process_age)


def process_age(message):
    user_id = message.chat.id
    age = message.text
    user_states[user_id]['age'] = age
    markup = create_keyboard(["лёгкий", "средний", "сложный"])
    bot.send_message(message.chat.id, "Выберите уровень:", reply_markup=markup)
    bot.register_next_step_handler(message, process_level)


def process_level(message):
    user_id = message.chat.id
    level = message.text
    user_states[user_id]['level'] = level
    user_states[user_id]['question_index'] = 0
    ask_question(message)


def ask_question(message):
    user_id = message.chat.id
    age = user_states[user_id]['age']
    level = user_states[user_id]['level']
    question_index = user_states[user_id]['question_index']

    if question_index < len(questions[age][level]):
        question_data = questions[age][level][question_index]
        question = question_data["question"]
        options = question_data["options"]
        markup = create_keyboard(options)
        bot.send_message(message.chat.id, question, reply_markup=markup)
        bot.register_next_step_handler(message, process_answer)
    else:
        bot.send_message(message.chat.id, "Вы ответили на все вопросы!",
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def process_answer(message):
    user_id = message.chat.id
    answer = message.text
    age = user_states[user_id]['age']
    level = user_states[user_id]['level']
    question_index = user_states[user_id]['question_index']

    question_data = questions[age][level][question_index]
    correct_answer = question_data["correct_answer"]

    if answer == correct_answer:
        bot.send_message(message.chat.id, "Это правильный ответ", reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {correct_answer}",
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    user_states[user_id]['question_index'] += 1
    ask_question(message)


if __name__ == "__main__":
    bot.infinity_polling()