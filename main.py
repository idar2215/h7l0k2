from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Constants
START_TEXT = "Привет, я робот, созданный МКОУ СОШ №27. Сюда ты можешь обратиться за помощью, если тебя обижают"
HELP_TEXT = "Чтобы тебе помогли, нажимай на кнопку «Начать» и заполняй анкету"
START_BUTTON = "Начать"
FIRST, SECOND, THIRD, FOURTH = range(4)

def start(update, context):
    # Отправляем пользователю приветственное сообщение и кнопку "Начать"
    reply_markup = ReplyKeyboardMarkup([[START_BUTTON]], resize_keyboard=True)
    update.message.reply_text(START_TEXT)
    update.message.reply_text(HELP_TEXT, reply_markup=reply_markup)
    return FIRST

def start_form(update, context):
    # Запускаем форму
    update.message.reply_text("Напиши свое имя и фамилию. Ты можешь записать голосовое сообщение, если хочешь. Если тебе удобнее, можешь писать и текстом!")
    return SECOND

def get_name(update, context):
    # Получаем имя пользователя и переходим к следующему вопросу
    context.user_data['name'] = update.message.text
    update.message.reply_text("Напиши в каком ты классе (цифру и букву). Например : 9А")
    return THIRD

def get_class(update, context):
    # Получаем класс пользователя и переходим к следующему вопросу
    context.user_data['class'] = update.message.text
    update.message.reply_text("Отлично. Теперь, расскажи мне кто тебя обижает и как тебя обижает. Напиши это в одном сообщении. Ты можешь записать голосовое сообщение, если тебе удобнее так.")
    return FOURTH

def get_complaint(update, context):
    # Получаем жалобу пользователя и отправляем ее администратору
    name = context.user_data['name']
    user_class = context.user_data['class']
    complaint = update.message.text
    context.bot.send_message(chat_id="6192875899", text=f"Новая жалоба от {name}, {user_class}:\n{complaint}")
    update.message.reply_text("Молодец! В течении двух дней посмотрят твою заявку!")
    return ConversationHandler.END

def cancel(update, context):
    # Выход из формы
    update.message.reply_text("До свидания! Надеюсь, я смог помочь!")
    return ConversationHandler.END
