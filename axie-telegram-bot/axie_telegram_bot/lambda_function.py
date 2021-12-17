import os
import telebot
import cryptocompare as cc

API_KEY = os.environ['API_KEY']
print(API_KEY)
bot = telebot.TeleBot(API_KEY)
print(bot)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
    """bot.send_message(message.chat.id, "Hello!!")"""
    print(message.chat)
    print(message.chat.id)
    bot.forward_message(1302041567, message.chat.id, message)


@bot.message_handler(commands=['qr'])
def qr(message):
    bot.send_message(message.chat.id,
                     "## QR Code ##\n\n- For get your QR Code, you need to DM to [@TitanOS_Bot] with this command: [ /get_qr \'scholar_wallet\' \'scholar_pin\' ]\n\n- Para obtener tu QR Code, necesitas enviar un DM a [@TitanOS_Bot] con el siguiente comando: [ /get_qr \'scholar_wallet\' \'scholar_pin\']\n\n## Sample / Ejemplo ##\n/get_qr ronin:91b7f95c76777dbe0d4d330a4f7ab58ad415c17 258710")


@bot.message_handler(commands=['get_qr'])
def get_qr(message):
    """print(message)"""
    print(message.chat)
    print("\n\n")
    print(message.chat.id)
    if message.chat.id == 1302041567:
        print("Es posible entregar QR")
        bot.send_message(message.chat.id, "## QR Code #")
    else:
        print("No es posible entregar QR")
        bot.send_message(message.chat.id, "## NO QR Code #")


# @bot.message_handler(commands=['wsb'])
# def get_stocks(message):
#     resp = ""
#     stocks = ['gme', 'amc', 'nok', 'tsla', 'aapl']
#     stock_data = []
#     for stock in stocks:
#         data = yf.download(tickers=stock, period='2d', interval='1d')
#         data = data.reset_index()
#         resp += f"-----{stock}-----\n"
#         stock_data.append([stock])
#         columns = ['STOCKs']
#         for index, row in data.iterrows():
#             stock_position = len(stock_data) - 1
#             price = round(row['Close'], 2)
#             format_date = row['Date'].strftime('%m/%d')
#             resp += f"{format_date}: {price}\n"
#             stock_data[stock_position].append(price)
#             columns.append(format_date)
#         print()
#
#     resp = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
#     for row in stock_data:
#         resp += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
#     resp += "\nStock Data"
#     print(resp)
#     bot.send_message(message.chat.id, resp)


def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True


# @bot.message_handler(func=stock_request)
# def send_price(message):
#     price = cc.get_price('BTC', 'USD')
#     print(price)
#     price = cc.get_price('MBOX', 'USD')
#     print(price)
#     price = cc.get_price('ADA', 'USD')
#     print(price)
#
#     request = message.text.split()[1]
#     data = yf.download(tickers=request, period='5m', interval='1m')
#     if data.size > 0:
#         data = data.reset_index()
#         data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
#         data.set_index('format_date', inplace=True)
#         print(data.to_string())
#         bot.send_message(message.chat.id, data['Close'].to_string(header=False))
#     else:
#         bot.send_message(message.chat.id, "No data!?")


bot.polling()
