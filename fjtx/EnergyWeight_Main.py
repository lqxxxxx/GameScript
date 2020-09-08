''' 模拟能量slot '''

import random



''' 配置 '''
# 配置免费能量
freeEnergy = 0
# 配置付费能量
payEnergy = 6000
# 人数
UserCount = 1000
# 主题活动进度
themeActivitiesStep = {1:1,2:2,3:3,4:5,5:6,6:8,7:11,8:12,9:15,10:19,
                   11:25,12:30,13:38,14:45,15:55,16:85,17:90,18:160,
                   19:300,20:320,21:540,22:580,23:870,24:1380,25:1395,
                   26:2145,27:2220,28:3320,29:4820,30:4860,31:8660
                       }


''' {1:1,2:1,3:1,4:2,5:1,6:2,7:3,8:2,9:3,10:3,
                   11:6,12:5,13:8,14:8,15:10,16:30,17:5,18:70,
                   19:140,20:20,21:220,22:40,23:290,24:510,25:15,
                   26:750,27:75,28:1100,29:1500,30:40,31:3800
                       }'''
# 主题活动奖励
themeActivitiesReward = {1:(1,10),2:(0,0),3:(2,100000),4:(1,20),5:(0,0),6:(2,300000),
                          7:(1,25),8:(0,0),9:(2,400000),10:(1,30),11:(2,600000),12:(1,50),
                          13:(0,0),14:(1,60),15:(2,1250000),16:(1,160),17:(0,0),18:(1,300),
                          19:(1,520),20:(2,5000000),21:(1,850),22:(2,8000000),23:(1,1400),
                          24:(1,2100),25:(0,0),26:(1,3800),27:(2,10000000),28:(1,4200),
                          29:(1,5580),30:(0,0),31:(1,12500)
                         }
# 锦标赛里程碑进度
tournamentStep = {1:10,2:30,3:50,4:60,5:120,6:150,7:330,8:250,9:600,10:1350,11:5500}
# 锦标赛里程碑奖励
tournamentReward = {1:(1,5),2:(2,30000),3:(1,10),4:(2,80000),5:(1,15),6:(2,200000),7:(1,30),8:(2,400000),9:(1,50),10:(1,75),11:(1,300)}

# 能量1倍权重
freeEnergyWeightByOne = {3:168,4:280,6:311,5:691,23:726,13:782,22:1661,12:1761,21:896,11:896,0:1828,7:0}
PayEnergyWeightByOne = {3:300,4:500,6:311,5:691,23:800,13:900,22:1200,12:1300,21:1600,11:1600,0:798,7:0}




# 摇奖结果
EnergyResult = {3:50000,4:25000,6:10,5:1,23:20000,13:16000,22:10000,12:8000,21:6000,11:5000,0:0,7:0}


''' 存储变量 '''
# 当前积分
CurScore = 0
CurTournamentScore = 0
# 当前免费能量
CurfreeEnergy = freeEnergy
# 当前付费能量
CurpayEnergy = payEnergy
# 当前权重队列
CurfreeEnergyWeight = []
CurPayEnergyWeight = []

# 已完成任务列表
CurThemeActivitiesStep = []
CurTournamentStep = []



''' 数据记录 '''
# 主题活动获得能量奖励
themeActivitiesRewardEnergyTotal = 0
# 主题活动获得金币奖励
themeActivitiesRewardGoldTotal = 0
# 锦标赛里程碑获得金币奖励
tournamentRewardGoldTotal = 0
# 锦标赛里程碑获得能量奖励
tournamentRewardEnergyTotal = 0

# 总金币产出
TotalOutGold = 0
# 总玩局数
TotalBetCount = 0
# 总能量产出
TotalOutCount = 0

CountTotal = 0
scoretotal = 0


#金币产出
zhutou  = 0
gongji = 0
putong = 0

zhutougailv = 0
gongjigailv = 0

a = 0
''' 主循环 '''
while UserCount > 0:
    #print(CurpayEnergy,CurfreeEnergy)
    # 权重队列判断
    if len(CurfreeEnergyWeight ) == 0:
        for key in freeEnergyWeightByOne:
            CurfreeEnergyWeight = CurfreeEnergyWeight + [key] * freeEnergyWeightByOne[key]
        random.shuffle(CurfreeEnergyWeight)

    if len(CurPayEnergyWeight ) == 0:
        for key in PayEnergyWeightByOne:
            CurPayEnergyWeight = CurPayEnergyWeight + [key] * PayEnergyWeightByOne[key]
        random.shuffle(CurPayEnergyWeight)


    # 摇奖
    # 1.判断剩余能量情况并摇奖
    FreeOrPay = 0
    if CurpayEnergy >0 :
        randomInt = random.randint(1,len(CurPayEnergyWeight))
        result = CurPayEnergyWeight[randomInt-1]
        CurPayEnergyWeight.pop(randomInt-1)
        FreeOrPay = 1
        CurpayEnergy = CurpayEnergy -1
    else:
        randomInt = random.randint(1,len(CurfreeEnergyWeight))
        result = CurfreeEnergyWeight[randomInt-1]
        CurfreeEnergyWeight.pop(randomInt-1)
        FreeOrPay = 0
        CurfreeEnergy = CurfreeEnergy -1

    #总局数增加
    TotalBetCount = TotalBetCount+1

    # 2.判断摇奖情况
    if result == 3:
        # 猪头主题 1积分
        CurScore = CurScore + 1
        # 猪头里程碑 6积分
        CurTournamentScore = CurTournamentScore + 6
        scoretotal = scoretotal+ 1
        zhutougailv = zhutougailv+1
    elif result == 4:
        # 里程碑 4积分
        CurTournamentScore = CurTournamentScore + 4
        gongjigailv = gongjigailv + 1


    # 金币增加
    if result not in (6,5):
        if result not in (3,4):
            TotalOutGold = TotalOutGold + EnergyResult[result]*2
        if result == 3:
            TotalOutGold = TotalOutGold + EnergyResult[result]*1.5
            zhutou = zhutou + EnergyResult[result]*1.5
        if result == 4:
            TotalOutGold = TotalOutGold + EnergyResult[result]*2
            gongji = gongji + EnergyResult[result]*2
        if result not in (3,4):
            putong = putong + EnergyResult[result]*2

    # 能量增加
    else:
        if FreeOrPay == 0:
            CurfreeEnergy = CurfreeEnergy + EnergyResult[result]
        else:
            CurpayEnergy = CurpayEnergy + EnergyResult[result]
        TotalOutCount = TotalOutCount + EnergyResult[result]




    # 主题活动判断
    for x in themeActivitiesStep:
        #判断是否完成并且是否领奖
        if CurScore*1.69 >= themeActivitiesStep[x] and x not in CurThemeActivitiesStep:
            #print(CurScore*1.69)
            CurThemeActivitiesStep.append(x)
            # 奖励类型 1能量 2金币
            if themeActivitiesReward[x][0] == 1:
                CurfreeEnergy = CurfreeEnergy + themeActivitiesReward[x][1]
                themeActivitiesRewardEnergyTotal = themeActivitiesRewardEnergyTotal+themeActivitiesReward[x][1]
                TotalOutCount = TotalOutCount+ themeActivitiesReward[x][1]
                #print ('主题',themeActivitiesRewardEnergyTotal)
            if themeActivitiesReward[x][0] == 2:
                TotalOutGold = TotalOutGold + themeActivitiesReward[x][1]
                themeActivitiesRewardGoldTotal = themeActivitiesRewardGoldTotal+ themeActivitiesReward[x][1]

            #重置
            if len(CurThemeActivitiesStep) >= len(themeActivitiesStep):
                CurThemeActivitiesStep = []
                CurScore = 0
                CountTotal = CountTotal+ 1

    # 锦标赛里程碑
    '''for x in tournamentStep:
        #判断是否完成并且是否领奖
        if CurTournamentScore >= tournamentStep[x] and x not in CurTournamentStep:
            CurTournamentStep.append(x)
            # 奖励类型 1能量 2金币
            if tournamentReward[x][0] == 1:
                CurfreeEnergy = CurfreeEnergy + tournamentReward[x][1]
                tournamentRewardEnergyTotal = tournamentRewardEnergyTotal+tournamentReward[x][1]
                TotalOutCount = TotalOutCount+ tournamentReward[x][1]
                #print ('里程碑',tournamentRewardEnergyTotal)
            if tournamentReward[x][0] == 2:
                TotalOutGold = TotalOutGold + tournamentReward[x][1]
                tournamentRewardGoldTotal = tournamentRewardGoldTotal+tournamentReward[x][1]

            #重置
            if len(CurTournamentStep) >= len(tournamentStep):
                CurTournamentStep = []
                CurTournamentScore = 0
'''

    # 判断是否已无能量
    if CurfreeEnergy == 0 and CurpayEnergy == 0:
        print(UserCount)
        UserCount = UserCount - 1
        CurfreeEnergy = freeEnergy
        CurpayEnergy = payEnergy
        CurTournamentStep = []
        CurThemeActivitiesStep = []
        CurScore = 0
        CurTournamentScore = 0



print(gongjigailv,zhutougailv,TotalOutGold,TotalBetCount,TotalOutCount,CountTotal,scoretotal,TotalOutGold/(TotalBetCount*40000),
      themeActivitiesRewardEnergyTotal/TotalBetCount,(TotalOutCount-themeActivitiesRewardEnergyTotal)/TotalBetCount,putong/(TotalBetCount*40000),zhutou/(TotalBetCount*40000) ,gongji/(TotalBetCount*40000))


