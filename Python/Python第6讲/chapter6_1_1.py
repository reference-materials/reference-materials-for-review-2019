import randomteams = ('信科','经管','体育','物理')try:    fs = open(r'd:\scores.txt','w') # 在d盘根目录创建一个文件    nums = len(teams)    for n in range(nums):        fs.write(teams[n])          # 输出队名到文件        if n < nums-1:            fs.write(',')        fs.write('\n')        for i in range(4):        # 随机生成四组数据        for j in range(10):   # 每组10个数据            tem_score = random.randint(70,99)         # 生成一个70-90之间的随机数            fs.write('{0:<3}'.format(tem_score)) # 保存随机分数到文件            if(j != 9): fs.write(',')            # 逗号分隔        fs.write('\n')   # 每10个数据一换行except:    print('文件读写错误')finally:    fs.close()           #关闭文件    print('文件关闭')