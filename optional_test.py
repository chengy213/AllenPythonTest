import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Optional


@dataclass
class FetchResult:
    url: str
    status: Optional[int]
    error: Optional[str]
    elapsed: float


def fetch_with_retry(url: str, retries: int = 3, timeout: int = 10) -> FetchResult:
    """带重试的抓取"""
    start = time.perf_counter()
    last_err = None
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=timeout)
            return FetchResult(url, r.status_code, None, time.perf_counter() - start)
        except Exception as e:
            last_err = str(e)
            if attempt < retries - 1:
                time.sleep(0.5 * (2 ** attempt))   # 指数退避
    return FetchResult(url, None, last_err, time.perf_counter() - start)


def batch_fetch(urls: list[str], max_workers: int = 10, timeout: int = 30):
    """批量抓取，带超时控制和进度报告"""
    total = len(urls)
    done = 0
    ok = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch_with_retry, url): url for url in urls}

        try:
            for future in as_completed(future_to_url, timeout=timeout):
                result = future.result()
                done += 1

                if result.status == 200:
                    ok += 1
                    mark = "✅"
                else:
                    failed += 1
                    mark = "❌"

                print(f"[{done}/{total}] {mark} {result.url} "
                      f"status={result.status} elapsed={result.elapsed:.2f}s")

        except TimeoutError:
            print(f"⚠️ 整体超时，已完成 {done}/{total}")
            # 取消未完成的任务
            for f in future_to_url:
                f.cancel()

    print(f"\n完成: 成功 {ok}, 失败 {failed}, 共 {total}")


if __name__ == "__main__":
    urls = [f"https://httpbin.org/delay/1?i={i}" for i in range(20)]

    start = time.perf_counter()
    batch_fetch(urls, max_workers=10, timeout=30)
    print(f"总耗时: {time.perf_counter() - start:.2f}s")
