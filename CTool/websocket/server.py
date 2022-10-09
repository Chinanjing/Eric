#!/usr/bin/env python

import asyncio
import websockets
import websockets_routes

router = websockets_routes.Router()

@router.route("/light/{status}")
async def light_status(websocket, path):
    async for message in websocket:
        print(f"从客户端获取的信息：{message}-->{path.params['status']}")
        # await asyncio.sleep(1)
        if path.params["status"] == "on":
            await websocket.send("开灯")
        elif path.params["status"] == "off":
            await websocket.send("关灯")
        elif path.params["status"] == "quit":
            await websocket.close()
        else:
            await websocket.send("参数无效")
        
async def main():
    async with websockets.serve(lambda x, y: router(x, y), "localhost", 8765):
        print(60*"=")
        await asyncio.Future()  # run forever
        
if __name__ == "__main__":
    asyncio.run(main())
