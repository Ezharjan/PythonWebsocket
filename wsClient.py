import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time

url = "ws://127.0.0.1:6789"


def on_message(ws, message):
    print("####### on_message #######")
    print(ws)
    print(message)


def on_error(ws, error):
    print("####### on_error #######")
    print(ws)
    print(error)


def on_close(ws):
    print("####### on_close #######")
    print(ws)
    print("####### closed #######")


def on_open(ws):
    print("####### on_open #######")

    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    # thread.start_new_thread(run, ()) # for test-only


if __name__ == '__main__':
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(http_proxy_host="127.0.0.1", http_proxy_port=6789)
