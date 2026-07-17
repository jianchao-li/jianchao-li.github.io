---
title: "Rate Limiters"
summary: "I will explain five algorithms for rate limiters with example Python implementation: token bucket, leaky bucket, fixed window counter, sliding window log and sliding window counter."
tags: ["software-engineering", "system-design", "rate-limiting"]
description: "An explanation of five rate limiting algorithms."
date: 2026-06-19T14:45:22+02:00
lastmod: 2026-07-17
draft: false
---

I recently read about [rate limiting](https://en.wikipedia.org/wiki/Rate_limiting) in Alex Xu's [System Design Interview - An Insider's Guide](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF) (you can find a copy [here](https://bytes.usc.edu/~saty/courses/docs/data/SystemDesignInterview.pdf)). The book provides a nice illustration of five rate-limiting algorithms: token bucket, leaky bucket, fixed window counter, sliding window log, and sliding window counter.

Reading about a concept from a great book can easily give me the illusion that I understand it. So, I decided to implement the five algorithms myself to verify whether I have truly grasped the nitty-gritty details.

**Disclaimer**: I won't go into the algorithms in detail in this post. You can read about them on pages 54 to 62 in the copy above. Moreover, all the implementations that follow are based on my own understanding and are intended to explain the algorithms rather than replicate what production implementations look like in real-world systems.

# Interface

For rate limiters, the core interface boils down to the following: it takes a `request` containing a `timestamp` and decides whether to accept or reject it.

```python
from dataclasses import dataclass

@dataclass
class Request:
	timestamp: int

class RateLimiter:
	def accept(self, request: Request) -> bool:
	    pass
```

# Token bucket

In the token bucket algorithm, you have a bucket that contains a specified number of tokens (`bucket_size`; note that these are unrelated to the tokens in LLMs). When a request arrives, it consumes one token and is processed. Tokens are refilled at a specified rate (`refill_rate`). **In the following implementations, all rates are defined per minute.**

```python
SECONDS_TO_MINUTES = 1 / 60

class TokenBucket:
    def __init__(self, bucket_size: int, refill_rate: float):
        self.bucket_size = bucket_size
        self.refill_rate = refill_rate
        self.tokens = bucket_size  # Number of remaining tokens
        self.last = None  # Timestamp of the last arrived request

    def accept(self, request: Request) -> bool:
        if self.last is None:
            # First request
            self.last = request.timestamp
            self.tokens -= 1
            return True
		 
        # Compute how many tokens are refilled
        delta = request.timestamp - self.last
        self.tokens = min(
            self.bucket_size,
            self.tokens + self.refill_rate * delta * SECONDS_TO_MINUTES,
        )
        
        self.last = request.timestamp

        if self.tokens < 1:
            return False

        self.tokens -= 1
        return True
```

# Leaky bucket

The leaky bucket algorithm is similar to the token bucket algorithm. You have a bucket with a specified size (`bucket_size`), and it leaks at a specified rate (`leak_rate`). You can think of it as a fixed-size queue where incoming requests are added and then processed and dequeued at a certain rate. The code is very similar to that of the token bucket implementation.

```python
class LeakyBucket:
    def __init__(self, bucket_size: int, leak_rate: float) -> None:
        self.bucket_size = bucket_size
        self.leak_rate = leak_rate
        self.level = 0.0  # Current number of requests in the bucket
        self.last = None

    def accept(self, request: Request) -> bool:
        if self.last is None:
            self.last = request.timestamp
            self.level = 1
            return True

        # Compute how many requests are leaked out
        delta = request.timestamp - self.last
        self.level = max(0.0, self.level - self.leak_rate * delta * SECONDS_TO_MINUTES)
        self.last = request.timestamp

        if self.level >= self.bucket_size:
            return False

        self.level += 1
        return True
```

# Fixed window counter

The fixed window counter algorithm divides time into fixed-size windows (**we use 60-second windows for all the following algorithms**). A counter (`count`) tracks how many requests have been accepted within each window. A request is accepted only if the counter does not exceed the limit (`limit`).

```python
class FixedWindowCounter:
    def __init__(self, limit: int, window: int = 60) -> None:
        self.limit = limit
        self.window = window
        self.start = None  # The stating timestamp of the current window
        self.count = 0

    def accept(self, request: Request) -> bool:
        window_start = int(request.timestamp // self.window)

        if self.start != window_start:
            self.start = window_start
            self.count = 0

        if self.count >= self.limit:
            return False

        self.count += 1
        return True
```

# Sliding window log

The fixed window counter has the problem of accepting too many requests when there is a burst of requests near the window boundaries. The sliding window log algorithm fixes this by using a sliding window: when a request arrives, we treat its timestamp as the end of the window and check whether the number of accepted requests within this window has exceeded the limit.

```python
class SlidingWindowLog:
    def __init__(self, limit: int, window: int = 60) -> None:
        self.limit = limit
        self.window = window
        self.q = deque()

    def accept(self, request: Request) -> bool:
        cutoff = req.timestamp - self.window

        # Remove requests that fall outside the window ending at the current timestamp
        while self.q and self.q[0] <= cutoff:
            self.q.popleft()

        if len(self.q) >= self.limit:
            return False

        self.q.append(request.timestamp)
        return True
``` 

# Sliding window counter

The sliding window counter algorithm is a combination of the fixed window counter and sliding window log algorithms. It calculates the number of accepted requests in the sliding window as the sum of the number of requests in the current fixed window and the number of requests in the previous fixed window multiplied by the overlap percentage between the sliding window and the previous fixed window.

If this explanation is difficult to follow, Figure 4-11 in the copy of Alex's book should make it clear.

```python
class SlidingWindowCounter:
    def __init__(self, limit: int, window: int = 60) -> bool:
        self.limit = limit
        self.window = window
        self.curr_start = None  # Index of the current fixed window
        self.curr = 0  # Number of requests in the current fixed window
        self.prev = 0  # Number of requests in the previous fixed window

    def _start(self, t: float) -> int:
        # Get the index of the fixed window containing t
        return int(t // self.window)

    def accept(self, request: Request) -> bool:
        w = self._start(req.timestamp)

        if self.curr_start is None:
            # First request
            self.curr_start = w
            self.curr = 0

        if w != self.curr_start:
            # A new fixed window
            self.prev = self.curr
            self.curr = 0
            self.curr_start = w

        # Clamp the weight to be [0, 1]
        weight = max(0.0, min(1.0, 1 - ((request.timestamp % self.window) / self.window)))
        effective = self.curr + self.prev * weight

        if effective >= self.limit:
            return False

        self.curr += 1
        return True
```

# Simulation: burst of traffic near window boundaries

An interesting case to simulate is a burst of traffic near window boundaries. This should reveal the weakness of the fixed window counter algorithm. The simulation is performed as follows.

```python
def generate_requests():
    requests = []
    # Burst right before the window boundary
    for _ in range(100):
        requests.append(Request(59.9))
    # Burst immediately after the window boundary
    for _ in range(100):
        requests.append(Request(60.1))
    return requests

def run():
    reqs = generate_requests()

    algorithms = {
        "token": TokenBucket(100, 100),
        "leaky": LeakyBucket(100, 100),
        "fixed": FixedWindowCounter(100),
        "sliding_log": SlidingWindowLog(100),
        "sliding_counter": SlidingWindowCounter(100),
    }

    results = {k: 0 for k in algorithms}

    for r in reqs:
        for name, alg in algorithms.items():
            if alg.accept(r):
                results[name] += 1

    for k, v in results.items():
        print(f"{k:15s}: {v}")


if __name__ == "__main__":
    run()
```

The following is the result we obtain. As can be seen, the fixed window counter allows all 200 requests, while all other algorithms allow rougly 100 requests as intended.

```
token          : 100
leaky          : 101
fixed          : 200
sliding_log    : 100
sliding_counter: 101
```