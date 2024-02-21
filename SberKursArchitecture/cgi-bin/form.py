import cgi
from CreditPaymentsModule import CreditPayments
import xmlrpc.client
from lxml import etree
import requests


def get_usd(month_and_year):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/' + month_and_year
    response = requests.get(url)
    root = etree.fromstring(response.content)
    usd_rate = 1.0
    for value in root.xpath('//Valute[CharCode="USD"]'):
        usd_rate = float(value.findtext('Value').replace(',', '.'))
    return usd_rate


form = cgi.FieldStorage()
deal_id = form.getfirst("deal_id", "none")
date = form.getfirst("date", "none")
str = date.replace('.', '/')

client_client_info = xmlrpc.client.ServerProxy('http://localhost:8001')
client_risks_info = xmlrpc.client.ServerProxy('http://localhost:8002')

inn = client_client_info.getINNByDealId(deal_id)
fio = client_client_info.getFIOByINN(inn)
credit_history = client_risks_info.getCreditHistoryByINN(inn)
credit_calc = CreditPayments()

usd_exchange_rate = get_usd(str)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Обработка данных формы</title>
</head>
<body>
    <h1>Остаток кредита по договору = {} Тысяч долларов</h1>
    <h1>Сумма кредита = {} Тысяч долларов</h1>
    <h2>ИНН клиента: {}</h2>
    <h2>ФИО клиента: {}</h2>
    <h2>Кредитная история: {}</h2>
    <h2>Курс доллара США: {} RUB</h2>
</body>
</html>
""".format(
    credit_calc.getRestOfCredit(deal_id, date) / usd_exchange_rate,
    credit_calc.getSummOfCredit(deal_id) / usd_exchange_rate,
    inn,
    fio,
    credit_history,
    usd_exchange_rate
))
