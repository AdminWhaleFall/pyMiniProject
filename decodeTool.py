'''
Author: whalefall
Date: 2021-04-10 21:10:29
LastEditTime: 2021-04-10 21:55:26
Description: 应朋友要求写的一个在`termux`上运行的解编码程序
'''
import base64
import traceback


def base64Encode(content):
    return str(base64.b64encode(content.encode("utf-8")), "utf-8")


def base64Decode(content):
    return str(base64.b64decode(content), "utf-8")


# print(base64Decode(base64Encode("鲸落")))

def unicodeDecode(content):
    return content.encode('utf-8').decode().encode('unicode_escape')


def unicodeEecode(content):
    return u"%s" % (content).encode('unicode-escape')


if __name__ == "__main__":
    while True:
        try:
            print('''
        ###########################
        #    Python解编码程序      #
        ###########################
        # 1. 输入1:base64编码
        # 2. 输入2:base64解码
        # 3. 输入3:unicode编码
        # 4. 输入4:unicode解码      
        ###########################
            ''')
            put = input("请输入功能号:")
            if put == "1":
                content = input("请输入将要base64加密的字符串:")
                print("结果:%s" % base64Encode(content))
            elif put == "2":
                content = input("请输入将要base64解密的字符串:")
                print("结果:%s" % base64Decode(content))
            elif put == "3":
                content = input("请输入将要unicode编码的字符串:")
                print("结果:%s" % unicodeEecode(content))
            elif put == "4":
                content = input("请输入将要unicode解码的字符串:")
                print("结果:%s" % unicodeDecode(content))
            else:
                print("非预期输入!")
        except Exception as e:
            print("未知错误,请检查输入的字符串")

            print(traceback.format_exc())
