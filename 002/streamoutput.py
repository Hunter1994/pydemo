from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
import io

app = FastAPI()

# 一个生成流数据的生成器
def generate_large_file():
    for i in range(1, 60):  # 模拟流数据
        yield f"Chunk {i}\n"
        time.sleep(1)  # 模拟延时，表示流的生成

@app.get("/stream")
async def stream_response():
    # 返回流式响应，设置生成器作为响应体
    return StreamingResponse(generate_large_file(), media_type="text/plain")

