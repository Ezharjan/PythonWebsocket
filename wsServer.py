from websocket_server import WebsocketServer


# Hint while the new client is connected
def new_client(client, server):
    print("To hint for the new cliented:%s" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


# 当旧的客户端离开
def client_left(client, server):
    print("A client with ID of %s has left." % client['id'])


# 接收客户端的信息。
def message_received(client, server, message):
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message_to_all(message)


if __name__ == '__main__':
    server = WebsocketServer(6789, "0.0.0.0")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()