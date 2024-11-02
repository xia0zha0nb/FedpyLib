from .. import timer

@timer.timer
def example(n):
    for i in range(n):
        print(i)
    return "Done"

result,micro,nano = example(1000000)
print(f"Result: {result}, Time taken: {micro} microseconds, {nano} nanoseconds.")