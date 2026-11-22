import time


def clamp(value, low, high):
    return max(low, min(value, high))


def chunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def sleep(seconds):
    time.sleep(seconds)
