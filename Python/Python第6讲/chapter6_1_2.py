scores = []lines  = []max_score = 0winner=''try:        fr = open('d:\\scores.txt','r')    line=fr.readline()     #读取第一行队名    teams=line.split(',')  #分隔成队名列表数组    print(teams)        lines=fr.readlines()   #读取所有后续内容    print(lines)    for line in lines:     # 处理每一行数据                print(line)        ls_score = line.split(',')        print(ls_score)# 每行数据分割成一维数组        fscore=[]                for j in range(len(ls_score)):      # 转换成数值列表            fscore.append(int(ls_score[j]))          scores.append(fscore)               # 当前行添加到二维数组            ave_scores = []           for i in range(len(scores)):            # 计算每一个队伍的平均分        ave_tem = ( sum(scores[i]) - max(scores[i]) - min(scores[i]) )/(len(scores[i])-2)        ave_scores.append(ave_tem)                max_score = max(ave_scores)             # 查找平均分最高的队伍    idx = ave_scores.index(max_score)       # 查找对应的队伍下标    winner = teams[idx]                     # 获胜者队名    print(ave_scores)                                   print('获得最高得分的院系是：{0},得分为：{1}'.format(winner,max_score)) #输出finally:    fr.close()