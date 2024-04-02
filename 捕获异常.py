# 当我们的程序遇到了bug，接下来2种情况
# 整个程序因为一个BUG停止运行
# 对BUG进行提醒，整个程序继续运行

# 如果没有文件，就创建文件
try:
    f = open('linux.txt', 'r')
except:
    f = open('linux.txt', 'w')

