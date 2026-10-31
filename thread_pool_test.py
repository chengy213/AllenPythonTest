import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [f"https://httpbin.org/delay/1?i={i}" for i in range(20)]

def fetch(url: str) -> tuple[str, int]:
    """抓取单个 URL，返回 (url, status_code)"""
    r = requests.get(url, timeout=10)
    return url, r.status_code

def fetch_all(urls: list[str], max_workers: int = 10):
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务，返回 Future 列表(dict字典)
        future_to_url = {executor.submit(fetch, url): url for url in urls}

        # 谁先完成先处理谁
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                _, status = future.result(timeout=15)
                results[url] = status
            except Exception as e:
                print(f"失败: {url} -> {e}")
                results[url] = None
    return results

if __name__ == "__main__":
    start = time.perf_counter()
    results = fetch_all(URLS, max_workers=10)
    print(f"耗时: {time.perf_counter() - start:.2f}s")
    print(f"成功: {sum(1 for v in results.values() if v == 200)}/{len(results)}")
