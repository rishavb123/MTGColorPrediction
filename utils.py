import time

def time_func(func, msg, *args, **kwargs):
    print(msg)
    stamp = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - stamp
    print(msg.replace("ing", "ed").replace(" . . .", f"! Took {int(1000 * elapsed) / 1000} seconds"))
    return result