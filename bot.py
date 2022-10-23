import logger as lg
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


bot = Bot(token='5656950277:AAFTa0QT8fGeajyl5YlEXzEOOncRlDc7cgs')
updater = Updater(token='5656950277:AAFTa0QT8fGeajyl5YlEXzEOOncRlDc7cgs')
dispatcher = updater.dispatcher


lg.logging.info('Start')


INPUT_RAT, INPUT_COMPLEX, END_CALC, INIT_CALC, CALC = range(5)


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f'To launch a calculator enter /init_calc \nFor exit enter /cancel')


def init_calc(update, context):
    lg.logging.info('User entered: {init_calc}')
    context.bot.send_message(update.effective_chat.id, 'Welcome to rational and complex number calculator!\n'
                                                      'Choose the type of numbers??\n'
                                                      'For rational - enter "/1"\n'
                                                      'For complex - enter "/2"')
    return CALC

def calc(update, context):
    lg.logging.info('User entered: {calc}')
    number = update.message.text
    if number == "/1":
        lg.logging.info('User entered 1')
        context.bot.send_message(update.effective_chat.id, 'Enter expression: \n (Example: 1 + 3)')
        return INPUT_RAT
    elif number == "/2":
        lg.logging.info('User entered 2')
        context.bot.send_message(update.effective_chat.id, 'Enter complex expression: \n (Example: 1+4j + 2+3j)')
        return  INPUT_COMPLEX


def rac_calc(update, context):
    example = update.message.text
    example1 = example.split()

    if "+" in example1:
        lg.logging.info('User entered {add_operation}')
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} + {int(example1[2])} = {int(example1[0]) + int(example1[2])} ')
    elif "-" in example1:
        lg.logging.info('User entered {substract_operation}')
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} - {int(example1[2])} = {int(example1[0]) - int(example1[2])} ')
    elif "*" in example1:
        lg.logging.info('User entered {multiply_operation}')
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} * {int(example1[2])} = {int(example1[0]) * int(example1[2])} ')
    elif "/" in example1:
        lg.logging.info('User entered {divide_operation}')
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} / {int(example1[2])} = {int(example1[0]) / int(example1[2])} ')
    context.bot.send_message(update.effective_chat.id, 'Enter anything to exit')
    return END_CALC

    

def complex_calc(update, context):
    number1 = update.message.text
    number1_1 = number1.split()
    if  "+" in number1_1:
        lg.logging.info('User entered {add_operation}')
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} + {complex(number1_1[2])} = {complex(number1_1[0]) + complex(number1_1[2])} ')
    elif  "-" in number1_1:
        lg.logging.info('User entered {substract_operation}')
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} - {complex(number1_1[2])} = {complex(number1_1[0]) - complex(number1_1[2])} ')
    elif  "*" in number1_1:
        lg.logging.info('User entered {multiply_operation}')
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} * {complex(number1_1[2])} = {complex(number1_1[0]) * complex(number1_1[2])} ')
    elif  "/" in number1_1:
        lg.logging.info('User entered {divide_operation}')
        numb = complex(number1_1[0])/ complex(number1_1[2])
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} / {complex(number1_1[2])} = {complex(round(numb.real, 2),round(numb.imag, 2))}')
    context.bot.send_message(update.effective_chat.id, 'Enter anything to exit')
    return END_CALC

def end_calc(update, context):
    lg.logging.info('User entered {end}')
    context.bot.send_message(update.effective_chat.id, 'Exited from calculator')
    return ConversationHandler.END

def cancel(update, _):
    lg.logging.info('User entered {cancel}')
    update.message.reply_text(
        'You have cancelled the operation'        
    )
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('init_calc', init_calc)],
    states={
        CALC: [MessageHandler(Filters.text, calc)],
        INPUT_RAT: [MessageHandler(Filters.text, rac_calc)],
        INPUT_COMPLEX: [MessageHandler(Filters.text, complex_calc)],
        END_CALC: [MessageHandler(Filters.text, end_calc)]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
dispatcher.add_handler(conv_handler)



start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle() 
