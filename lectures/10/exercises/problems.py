"""Lecture 10 practice problems: threading, multiprocessing, and async/await.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Use only the Python standard library.
"""

from __future__ import annotations

import asyncio
import time


def simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow blocking fetch and return the same input value."""
    time.sleep(0.1)
    return value


async def async_simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow async fetch and return the same input value."""
    await asyncio.sleep(0.1)
    return value


def locked_counter_total(num_threads: int, increments_per_thread: int) -> int:
    """Mission 1: thread-safe counter increment with `threading.Lock`.

    Required functions/classes:
        - `threading.Thread`
        - `threading.Lock`
        - `Thread.start()` and `Thread.join()`

    Expected result:
        num_threads * increments_per_thread
    """
    import threading

    class ThreadSafeCounter:
        def __init__(self) -> None:
            self.value = 0
            self.lock = threading.Lock()

        def increment(self) -> None:
            with self.lock:
                self.value += 1

    counter = ThreadSafeCounter()
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(
            target=lambda: [counter.increment() for _ in range(increments_per_thread)]
        )
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return counter.value


def threaded_square_map(values: list[int]) -> list[int]:
    """Mission 2: compute squares using one thread per element.

    Required functions/classes:
        - `threading.Thread`
        - `Thread.start()` and `Thread.join()`

    Notes:
        - Keep output index order the same as input order.

    Example:
        [2, -3, 4] -> [4, 9, 16]
    """
    import threading

    results = [None] * len(values)
    threads = []
    for i, value in enumerate(values):
        thread = threading.Thread(
            target=lambda i=i, value=value: results.__setitem__(i, value**2)
        )
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return results


def threadpool_sleep_map(delays: list[float], max_workers: int = 4) -> list[float]:
    """Mission 3: simulate blocking I/O with `ThreadPoolExecutor`.

    Requirements:
        - Use `ThreadPoolExecutor(max_workers=max_workers)`.
        - In each task, call `simulated_long_fetch(delay)` and return its result.
        - Preserve input order in returned list (for example via `executor.map`).
        - Raise `ValueError` if `max_workers < 1`.
    """
    from concurrent.futures import ThreadPoolExecutor

    if max_workers < 1:
        raise ValueError("max_workers must be at least 1")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(simulated_long_fetch, delays))
    return results


def processpool_square_map(values: list[int], max_workers: int = 2) -> list[int]:
    """Mission 4: compute squares with `ProcessPoolExecutor`.

    Requirements:
        - Use a process pool (`ProcessPoolExecutor`).
        - Use process-pool mapping (`executor.map` or equivalent).
        - Return squared values in the same order as input.
        - Raise `ValueError` if `max_workers < 1`.
    """
    raise NotImplementedError


async def async_tag_fetch(labels: list[str], delay: float = 0.01) -> list[str]:
    """Mission 5: run async tasks concurrently with `asyncio.gather`.

    Required functions:
        - `async_simulated_long_fetch`
        - `asyncio.gather`

    Behavior:
        - For each label, first fetch it with `async_simulated_long_fetch`.
        - Then return `f"done:{label}"`.
        - Preserve output order by label position.
        - `delay` is kept for API compatibility; you do not need to use it.
    """
    raise NotImplementedError


async def async_blocking_double(values: list[int]) -> list[int]:
    """Mission 6: bridge blocking work into async flow.

    Required functions:
        - `simulated_long_fetch`
        - `asyncio.to_thread`
        - `asyncio.gather`

    Return:
        - For each input value, run `simulated_long_fetch` via `to_thread`.
        - After fetch completes, double the value.
        - Return doubled values in input order.

        Example: [1, 2, 3] -> [2, 4, 6]
    """
    raise NotImplementedError
