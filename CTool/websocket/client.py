#!/usr/bin/env python

import websockets

async def light(set_status = "on"):
    if set_status == "on":
        light_status = "on"
    elif set_status == "off":
        light_status == "off"
    elif set_status == "quit":
        light_status = "quit"
    else:
        light_status == "Nothing"
            
    try:
        async with websockets.connect(f"ws://localhost:8765/light/{light_status}") as websocket:
            light_addr = "e4-3a-6e-14-4b-5b"
            await websocket.send(light_addr)
            recv_msg = await websocket.recv()
            print(f"从服务端获取的信息：{recv_msg}")
            return recv_msg
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"关闭websocket连接出错：{e}")
    except Exception as e:
        print(f"服务端已断开：{e}")
