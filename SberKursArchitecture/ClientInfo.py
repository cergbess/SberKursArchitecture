from xmlrpc.server import SimpleXMLRPCServer

client_data = {
    "1": {"inn": "11111", "fio": "Корнеев Вадим Викторович"},
    "2": {"inn": "22222", "fio": "Жильцов Владимир Александрович"},
    "3": {"inn": "33333", "fio": "Сахаров Никита Михайлович"},
    "4": {"inn": "44444", "fio": "Кольцов Иван Борисович"},
    "5": {"inn": "55555", "fio": "Бардин Максим Сергеевич"}
}


def getINNByDealId(deal_id):
    return client_data.get(deal_id, {}).get("inn", "unknown")

def getFIOByINN(inn):
    for deal_id, data in client_data.items():
        if data.get("inn") == inn:
            return data.get("fio", "unknown")
    return "unknown"


server = SimpleXMLRPCServer(('localhost', 8001))
server.register_function(getINNByDealId, 'getINNByDealId')
server.register_function(getFIOByINN, 'getFIOByINN')
print("Client Info Server is ready to accept requests.")
server.serve_forever()
