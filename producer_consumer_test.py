import asyncio

async def producer(queue, n):
    for i in range(n):
        await asyncio.sleep(0.1)
        await queue.put(i)
        print(f"生产 {i}")
    await queue.put(None)   # 结束信号

async def consumer(queue, name):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(0.2)
        print(f"消费者 {name} 处理 {item}")

async def main():
    queue = asyncio.Queue(maxsize=5)
    await asyncio.gather(
        producer(queue, 10),
        consumer(queue, "A"),
        consumer(queue, "B"),
    )

asyncio.run(main())
