from xmlrpc.server import SimpleXMLRPCServer

risks_data = {
    "11111": "Хорошая",
    "22222": "Хорошая",
    "33333": "Плохая",
    "44444": "Хорошая",
    "55555": "Плохая"
}

def getCreditHistoryByINN(inn):
    return risks_data.get(inn, "unknown")

server = SimpleXMLRPCServer(('localhost', 8002))
server.register_function(getCreditHistoryByINN, 'getCreditHistoryByINN')
print("Risks Info Server is ready to accept requests.")
server.serve_forever()
