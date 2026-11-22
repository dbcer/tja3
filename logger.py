import datetime


def log(level, msg):
    ts = datetime.datetime.now().isoformat()
    print(f"[{ts}] [{level}] {msg}")


def info(msg):
    log("INFO", msg)


def warn(msg):
    log("WARN", msg)
