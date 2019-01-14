import asyncio
import websockets
import logging
import json
import atexit
import time
import concurrent

PORT = 5679
logging.basicConfig(level="INFO")

sockets = set()
loop = asyncio.get_event_loop()

markers = [
    {
        "id": 0,
        "position": {
            "x": 400,
            "y": 200,
            "bearing": 0
        }
    },
    {
        "id": 1,
        "position": {
            "x": 400,
            "y": 300,
            "bearing": 0
        }
    },
    {
        "id": 2,
        "position": {
            "x": 100,
            "y": 200,
            "bearing": 0
        }
    },
    {
        "id": 3,
        "position": {
            "x": 300,
            "y": 200,
            "bearing": 0
        }
    }
]


async def on_connect(socket, path):
    logging.info('Socket connected')
    sockets.add(socket)
    await socket.send(json.dumps(markers))

    try:
        while True:
            message = await socket.recv()
            logging.warning('Ignoring received message: %s', message)
    except:
        sockets.remove(socket)
        logging.info(
            'Socket disconnected (maybe in response to closing handshake)')


async def send_markers():
    await socket.send(markers)


if __name__ == "__main__":

    logging.info("Starting websocket server...")
    start_server = websockets.serve(on_connect, port=PORT)

    loop.run_until_complete(start_server)

    logging.info('All started. Listening on port: %d', PORT)
    loop.run_forever()
