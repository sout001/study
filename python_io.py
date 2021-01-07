import io

# try:
#     file = io.open('test.txt', 'w', encoding='utf-8')
#     file.write('hello,python-io')
# except Exception as e:
#     print('执行程序出错')
# finally:
#     file.close()


if __name__ == '__main__':
    try:
        file = io.open('test.txt', 'r', encoding='utf-8')
        content = file.read()
        print(content)
    except Exception as e:
        print("程序执行出错")
    finally:
        file.close()
