import time
import random
import hashlib
import uuid

local_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))[2:]
str1 = str(random.randint(10000, 99999))
file_name = "11-1-01.png"
print(uuid.uuid1())

print(local_time + str1 + file_name)
print(time.localtime())
print(time.mktime(time.localtime()))


def get_file_name():
    local_time = time.strftime('%Y%m%d%H%M%S', time.time())
