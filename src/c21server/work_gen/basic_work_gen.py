import random
import time
from redis import Redis


def generateJobs(r):
    for _ in range(10):
        key = random.randint(0, 10000)
        value = random.randint(0, 10)
        r.hset("jobs_waiting", key, value)


def emulateJobCreation():
    r = Redis()
    for _ in range(5):
        generateJobs(r)
        time.sleep(30)


if __name__ == '__main__':
    emulateJobCreation()
