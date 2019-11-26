# 题目描述
# 密码要求:

# 1.长度超过8位

# 2.包括大小写字母.数字.其它符号,以上四种至少三种

# 3.不能有相同长度超2的子串重复

# 说明:长度超过2的子串

# 输入描述:
# 一组或多组长度超过2的子符串。每组占一行

# 输出描述:
# 如果符合要求输出：OK，否则输出NG

# 示例1
# 输入
# 021Abc9000
# 021Abc9Abc1
# 021ABC9000
# 021$bc9000
# 输出
# OK
# NG
# NG
# OK

while True:
    try:
        temp = input()
        if len(temp) <= 8:
            print('NG')
            continue
        digit = 0
        Cletter = 0
        letter = 0
        other = 0
        for char in temp:
            if char.isdigit():
                digit = 1
            elif char.isalpha() and char.isupper():
                Cletter = 1
            elif char.isalpha() and char.islower():
                letter = 1
            else:
                other = 1
        if digit + Cletter + letter + other < 3:
            print('NG')
            continue
        wrong = False
        for i in range(0, len(temp)-3):
            if temp[i:i+3] in temp[i+3:]:
                print('NG')
                wrong = True
                break
        if wrong:
            continue
        print('OK')
    except:
        break
        