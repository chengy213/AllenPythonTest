import threading
import asyncio

lock=asyncio.Lock()

# 传入name参数:
async def hello(name):
    #这里lock不是必须的
    async with lock:
        # 打印name和当前线程:
        print("Hello %s! (%s)" % (name, threading.current_thread))
        # 异步调用asyncio.sleep(1):模拟耗时操作
        await asyncio.sleep(1)
        print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name

async def main():
    #gather不带线程池玩？
    #原理是遇到IO就切换，多个任务的等待时间重叠，总耗时等于最慢单个耗时而非累加。
    L = await asyncio.gather(hello("Bob"), hello("Alice"), hello("Allen"))
    print(L)

asyncio.run(main())

