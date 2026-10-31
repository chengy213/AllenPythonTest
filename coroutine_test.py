
import asyncio
import aiohttp
import time

"""
这个文件运行有问题
"""
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        'http://www.python.org',
        'http://www.google.com',
        'http://www.baidu.com'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # 创建任务列表
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        # gather 并发运行所有任务并收集结果
        results = await asyncio.gather(*tasks)

        for url, html in zip(urls, results):
            print(f"Read {len(html)} chars from {url}")


if __name__ == "__main__":
    start = time.time()
    # 注意：运行此代码需要安装 aiohttp (pip install aiohttp)
    # 某些环境（如 Jupyter）可能已有运行中的 loop，需特殊处理，
    # 标准脚本中直接用 asyncio.run(main()) 即可。
    try:
        asyncio.run(main())
    except RuntimeError:
        # 针对 Jupyter Notebook 等环境的兼容写法
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    print(f"Cost: {time.time() - start:.2f} seconds")