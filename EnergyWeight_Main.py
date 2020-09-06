''' 模拟能量slot '''

''' 配置 '''
# 配置免费能量
freeEnergy = 0
# 配置付费能量
payEnergy = 3240
# 人数
UserCount = 1000
# 主题活动进度
themeActivitiesStep = {1:1,2:1,3:1,4:2,5:1,6:2,7:3,8:2,9:3,10:3,
                   11:6,12:5,13:8,14:8,15:10,16:30,17:5,18:70,
                   19:140,20:20,21:220,22:40,23:290,24:510,25:15,
                   26:750,27:75,28:1100,29:1500,30:40,31:3800
                       }
# 主题活动奖励
themeActivitiesReward = {1:{1:10},2:{0:0},3:{2:100000},4:{1:20},5:{0:0},6:{2:300000},
                          7:{1:20},8:{0:0},9:{2,400000},10:{1:30},11:{2:600000},12:{1:35},
                          13:{0:0},14:{1:40},15:{2:1250000},16:{1:100},17:{0:0},18:{1:200},
                          19:{1:520},20:{2:5000000},21:{1:850},22:{2:8000000},23:{1:1400},
                          24:{1:1500},25:{0:0},26:{1:3000},27:{2:10000000},28:{1:4200},
                          29:{1:4400},30:{0:0},31:{1:9000}
                         }
# 锦标赛里程碑进度
tournamentStep = {1:10,2:30,3:50,4:60,5:120,6:150,7:330,8:250,9:600,10:1350,11:5500}
# 锦标赛里程碑奖励
tournamentReward = {1:{1:5},2:{2:30000},3:{1:10},4:{1:80000},5:{1:15},6:{2:200000},7:{1:30},8:{2:400000},9:{1:50},10:{1:75},11:{1:300}}

#



''' 存储变量 '''
# 当前积分
CurScore = 0
# 当前免费能量
CurfreeEnergy = 0
# 当前付费能量
CurpayEnergy = 0
# 当前权重队列




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


''' 主循环 '''
while UserCount > 0:
    pass


