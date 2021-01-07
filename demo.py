import time


# 自定义统计方法执行
def decorate(func):
    def wrapper(*args, **kwargs):
        print("定义一个装饰器")
        func(*args, **kwargs)

    return wrapper


def utils(params):
    def wrapper(func):
        def sub_wrapper(*args, **kwargs):
            print("定义一个带参数的装饰器", params)
            print(id(sub_wrapper))
            func(*args, **kwargs)

        return sub_wrapper

    return wrapper


@utils(params="zs")
def test():
    print(id(test))


test()


def test_time():
    print("要睡觉了")
    time.sleep(2)
    print("睡了2秒")


test_time()
