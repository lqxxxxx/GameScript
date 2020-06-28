import win32con
import win32gui
import win32api
import game_Window
import game_functions
import setting

'''
   通过句柄类名和标题名打开软件，定义鼠标位置进行一次单击
'''

#主程序
def runMain():
    gw = game_Window.GameWindow("《梦幻西游》手游")
    gw.getGameWindow()



    game_functions.mounse_click_xy(game_functions.MOUNSE_DOUBLE_CLICK,1400 ,200)



runMain()