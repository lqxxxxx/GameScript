''' 水果元素排列组合生成脚本 '''


''' 配置 '''
# 线数
line = 9
#
rate_list = [1,3,10,75]

''' 变量 '''
# 队列容器
random_list = []
# 循环元素变量
a1,a2,a3,a4,a5,a6,a7,a8,a9 = 0,0,0,0,0,0,0,0,0
# 循环队列变量
rate_temp = []
# 最终数值队列
end_rate_dict = {}
end_rate_list = []

''' 函数 '''
# 下次循环队列元素判断
def create_rate_temp(rate):
    return_list = []
    for x in rate_list:
        if rate<=x:
            return_list.append(x)
    return return_list



# 插入数值队列
def add_rate_dict(random_list):
    end_rate_dict[sum(random_list)] = random_list
    end_rate_list.append(sum(random_list))



''' 主循环 最高9次 '''
'''    1线    '''
for x1 in rate_list:
    # 第一条线赋值
    a1 = x1
    # 插入队列容器
    random_list.append(a1)
    # 判断线数是否已结束
    if line > 1 :
        # 获取下一条线循环队列
        rate_temp = create_rate_temp(a1)
        '''    2线    '''
        for x2 in rate_temp:
            a2 = x2
            random_list.append(a2)
            if line > 2 :
                rate_temp = create_rate_temp(a2)
                '''    3线    '''
                for x3 in rate_temp:
                    a3 = x3
                    random_list.append(a3)
                    if line > 3:
                        rate_temp = create_rate_temp(a3)
                        '''    4线    '''
                        for x4 in rate_temp:
                            a4 = x4
                            random_list.append(a4)
                            if line > 4:
                                rate_temp = create_rate_temp(a4)
                                '''    5线    '''
                                for x5 in rate_temp:
                                    a5 = x5
                                    random_list.append(a5)
                                    if line > 5:
                                        rate_temp = create_rate_temp(a5)
                                        '''    6线    '''
                                        for x6 in rate_temp:
                                            a6 = x6
                                            random_list.append(a6)
                                            if line > 6:
                                                rate_temp = create_rate_temp(a6)
                                                '''    7线    '''
                                                for x7 in rate_temp:
                                                    a7 = x7
                                                    random_list.append(a7)
                                                    if line > 7:
                                                        rate_temp = create_rate_temp(a7)
                                                        '''    8线    '''
                                                        for x8 in rate_temp:
                                                            a8 = x8
                                                            random_list.append(a8)
                                                            if line > 8:
                                                                rate_temp = create_rate_temp(a8)
                                                                '''    9线    '''
                                                                for x9 in rate_temp:
                                                                    a9 = x9
                                                                    random_list.append(a9)
                                                                    if line > 9:
                                                                        rate_temp = create_rate_temp(a9)

                                                                    else:
                                                                        add_rate_dict(random_list)
                                                                        random_list = []

                                                            else:
                                                                add_rate_dict(random_list)
                                                                random_list = []


                                                    else:
                                                        add_rate_dict(random_list)
                                                        random_list = []

                                            else:
                                                add_rate_dict(random_list)
                                                random_list = []


                                    else:
                                        add_rate_dict(random_list)
                                        random_list = []


                            else:
                                add_rate_dict(random_list)
                                random_list = []


                    else:
                        add_rate_dict(random_list)
                        random_list = []


            else :
                add_rate_dict(random_list)
                random_list = []

    # 插入最终队列
    else :
        add_rate_dict(random_list)
        random_list = []

print (end_rate_list)
print (len(end_rate_list))

print (end_rate_dict)













