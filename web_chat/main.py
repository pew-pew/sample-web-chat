import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


class MessageBus:
    def __init__(self):
        self.new_event = asyncio.Event()
        self.messages = []

    async def all_events(self):
        sent = 0
        while True:
            if len(self.messages) == sent:
                await self.new_event.wait()
            new_size = len(self.messages)
            for msg in self.messages[sent:new_size]:
                yield msg
            sent = new_size
    
    def send(self, event):
        self.messages.append(event)
        self.new_event.set()
        self.new_event.clear()


app = FastAPI()
app.mount("/static", StaticFiles(directory="web_chat/static"), name="static")


@app.get("/")
def root():
    return FileResponse("web_chat/static/index.html")


messages = MessageBus()


@app.websocket("/ws")
async def websocket_smt(websocket: WebSocket):
    await websocket.accept()

    async def sender():
        async for msg in messages.all_events():
            await websocket.send_text(msg)

    async def receiver():
        while True:
            msg = await websocket.receive_text()
            messages.send(msg)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(sender())
            tg.create_task(receiver())
    except* WebSocketDisconnect:
        pass
